"""
basic: spawn ego_vehicle and add camera and lidar 2023/04-27

"""
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, DurabilityPolicy

import carla
import numpy as np
import math
from cv_bridge import CvBridge
import sys
import time

import queue
import threading
# for lidar point cloud
import struct
import ctypes

# 接口
from transforms3d.euler import quat2euler, euler2quat
from geometry_msgs.msg import Pose 
from sensor_msgs.msg import Image
from sensor_msgs.msg import PointCloud2, PointField
from std_msgs.msg import Header

# for waypoint publish
from waypoints_types.srv import GetWaypointsList
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped, Quaternion
from agents.navigation.global_route_planner import GlobalRoutePlanner
import carla_common.transforms as trans

CARLA_FPS = 60.0
CARLA_SCENE_NAME = "Bend03"
CARLA_EGO_MODEL_FILTER = "model3"
CARLA_EGO_STATE_TOPIC_NAME = "ego_vehicle"
CARLA_EGO_INIT_X = 417.495391845703
CARLA_EGO_INIT_Y = 252.950531005859
CARLA_EGO_INIT_Z = 0.1
CARLA_EGO_INIT_YAW = -12.729858/180.*math.pi
CARLA_SPECTATOR_DX = 0.10
CARLA_SPECTATOR_DY = -0.35
CARLA_SPECTATOR_DZ = 1.2
EGO_VEHICLE_IN_LEFTLANE = 1    # 记录是否在左侧车道，1表示在左侧车道；0表示在右侧车道

CARLA_ADJACENT0_MODEL_FILTER = "model3"
CARLA_ADJACENT0_STATE_TOPIC_NAME = "adjacent0"
CARLA_ADJACENT0_INIT_X = 437.027161
CARLA_ADJACENT0_INIT_Y = 252.122574
CARLA_ADJACENT0_INIT_Z = 0.1
CARLA_ADJACENT0_INIT_YAW = -12.742323/180.*math.pi

CARLA_ADJACENT1_MODEL_FILTER = "model3"
CARLA_ADJACENT1_STATE_TOPIC_NAME = "adjacent1"
CARLA_ADJACENT1_INIT_X = 427.273407
CARLA_ADJACENT1_INIT_Y = 254.328049
CARLA_ADJACENT1_INIT_Z = 0.1
CARLA_ADJACENT1_INIT_YAW = -12.740445/180.*math.pi

LEFT_CAMERA_X = 0.3
LEFT_CAMERA_Y = -1.0
LEFT_CAMERA_Z = 1.3
LEFT_CAMERA_ROLL = 0.0
LEFT_CAMERA_PITCH = 20.0
LEFT_CAMERA_YAW = -150.0
LEFT_CAMERA_IMAGE_SIZE_X = str(640)
LEFT_CAMERA_IMAGE_SIZE_Y = str(400)
LEFT_CAMERA_FOV = str(110)

RIGHT_CAMERA_X = 0.3
RIGHT_CAMERA_Y = 1.0
RIGHT_CAMERA_Z = 1.3
RIGHT_CAMERA_ROLL = 0.0
RIGHT_CAMERA_PITCH = 20.0
RIGHT_CAMERA_YAW = 150.0
RIGHT_CAMERA_IMAGE_SIZE_X = str(640)
RIGHT_CAMERA_IMAGE_SIZE_Y = str(400)
RIGHT_CAMERA_FOV = str(110)


# for point cloud
_DATATYPES = {}
_DATATYPES[PointField.INT8] = ('b', 1)
_DATATYPES[PointField.UINT8] = ('B', 1)
_DATATYPES[PointField.INT16] = ('h', 2)
_DATATYPES[PointField.UINT16] = ('H', 2)
_DATATYPES[PointField.INT32] = ('i', 4)
_DATATYPES[PointField.UINT32] = ('I', 4)
_DATATYPES[PointField.FLOAT32] = ('f', 4)
_DATATYPES[PointField.FLOAT64] = ('d', 8)

# for carla_waypoint publish
WAYPOINT_DISTANCE = 0.2
WAYPOINTDISTANCE = 150
WAYPOINTRESOLUTION = 0.1


class CarlaRosBridge(Node):
    """
    Carla Ros bridge
    """
    def __init__(self, name):
        """
        Constructor

        :param carla_world: carla world object
        :type carla_world: carla.World
        :param params: dict of parameters, see settings.yaml
        :type params: dict
        """
        super().__init__(name)
        # while rclpy.ok():
        self.get_logger().info("-----Successfully create my bridge node!-----")

        self.declare_parameter("host", "localhost")
        self.declare_parameter("port", 2000)
        self.declare_parameter("timeout", 10)
        self.declare_parameter("synchronous_mode", True)
        self.declare_parameter("fixed_delta_seconds", 1.0/CARLA_FPS)
        self.declare_parameter("town", CARLA_SCENE_NAME)
        self.declare_parameter("ego_vehicle_role_name", CARLA_EGO_STATE_TOPIC_NAME)
    
    def initialize_bridge(self, carla_world):
        """
        Initialize the simulator
        """
        self.bridge = CvBridge()
        self.synchronous_mode = self.get_parameter("synchronous_mode").value
        self.fixed_delta_seconds = self.get_parameter("fixed_delta_seconds").value
        self.role_name = self.get_parameter("ego_vehicle_role_name").value

        self.carla_world = carla_world
        self.carla_settings = self.carla_world.get_settings()
        self.map = self.carla_world.get_map()
        # self.get_logger().info(f"[not]Change simulate mode from {self.carla_settings.synchronous_mode}\
        #                        to {self.synchronous_mode}")
        if self.synchronous_mode:
            self.carla_settings.synchronous_mode = True
            self.carla_settings.fixed_delta_seconds = self.fixed_delta_seconds
        self.carla_world.apply_settings(self.carla_settings)

        self.weather = carla.WeatherParameters(
            cloudiness=20.0, precipitation=0.0, sun_altitude_angle=40.0)
        self.carla_world.set_weather(self.weather)

        self.actor_list = []
        self.sensor_list = []
        self.blueprint_library = self.carla_world.get_blueprint_library()
        
        # spawn the ego vehicle actor
        self.ego_vehicle_bp = self.blueprint_library.filter(
            CARLA_EGO_MODEL_FILTER)[0]
        self.ego_vehicle_bp.set_attribute('color', '0, 0, 0')
        self.ego_spawn_point = carla.Transform(carla.Location(
            x=CARLA_EGO_INIT_X, y=CARLA_EGO_INIT_Y, z=CARLA_EGO_INIT_Z),
            carla.Rotation(yaw=CARLA_EGO_INIT_YAW*180/math.pi))
        self.ego_vehicle = self.carla_world.spawn_actor(
            self.ego_vehicle_bp, self.ego_spawn_point)
        self.ego_vehicle.set_simulate_physics(False)
        self.actor_list.append(self.ego_vehicle)

        # get the lane waypoint according to ego_vehicle
        lane_waypoints = self.map.generate_waypoints(WAYPOINTRESOLUTION)
        if EGO_VEHICLE_IN_LEFTLANE:
            self.all_waypoints = [wp.get_left_lane() for wp in lane_waypoints]
        else:
            self.all_waypoints= [wp.get_right_lane() for wp in lane_waypoints]

        # spawn the adjacent0 vehicle actor
        self.adjacent0_vehicle_bp = self.blueprint_library.filter(
            CARLA_ADJACENT0_MODEL_FILTER)[0]
        self.adjacent0_vehicle_bp.set_attribute('color', '255, 0, 0')
        self.adjacent0_spawn_point = carla.Transform(carla.Location(
            x=CARLA_ADJACENT0_INIT_X, y=CARLA_ADJACENT0_INIT_Y, z=CARLA_ADJACENT0_INIT_Z),
            carla.Rotation(yaw=CARLA_ADJACENT0_INIT_YAW*180/math.pi))
        self.adjacent0_vehicle = self.carla_world.spawn_actor(
            self.adjacent0_vehicle_bp, self.adjacent0_spawn_point)
        self.actor_list.append(self.adjacent0_vehicle)

        # spawn the adjacent1 vehicle actor
        self.adjacent1_vehicle_bp = self.blueprint_library.filter(
            CARLA_ADJACENT1_MODEL_FILTER)[0]
        self.adjacent1_vehicle_bp.set_attribute('color', '0, 255, 0')
        self.adjacent1_spawn_point = carla.Transform(carla.Location(
            x=CARLA_ADJACENT1_INIT_X, y=CARLA_ADJACENT1_INIT_Y, z=CARLA_ADJACENT1_INIT_Z),
            carla.Rotation(yaw=CARLA_ADJACENT1_INIT_YAW*180/math.pi))
        self.adjacent1_vehicle = self.carla_world.spawn_actor(
            self.adjacent1_vehicle_bp, self.adjacent1_spawn_point)
        self.actor_list.append(self.adjacent1_vehicle)

        self.carla_world.tick()  # vehicles spawn after tick, then you can use get_transform

        # set sensors for ego vehicle

        # add two camera for rear view
        # camera relative position related to the vehicle
        left_camera_transform = carla.Transform(carla.Location(x=LEFT_CAMERA_X, y=LEFT_CAMERA_Y, z=LEFT_CAMERA_Z),\
                                                      carla.Rotation(roll=LEFT_CAMERA_ROLL, pitch=LEFT_CAMERA_PITCH, yaw=LEFT_CAMERA_YAW))
        left_camera_bp = self.blueprint_library.find('sensor.camera.rgb')
        left_camera_bp.set_attribute('image_size_x', LEFT_CAMERA_IMAGE_SIZE_X)
        left_camera_bp.set_attribute('image_size_y', LEFT_CAMERA_IMAGE_SIZE_Y)
        left_camera_bp.set_attribute('fov', LEFT_CAMERA_FOV)
        left_camera = self.carla_world.spawn_actor(left_camera_bp, left_camera_transform, attach_to=self.ego_vehicle)
        left_camera.listen(lambda image: self.left_camera_callback(image))
        self.sensor_list.append(left_camera)

        right_camera_transform = carla.Transform(carla.Location(x=RIGHT_CAMERA_X, y=RIGHT_CAMERA_Y, z=RIGHT_CAMERA_Z),\
                                                 carla.Rotation(roll=RIGHT_CAMERA_ROLL, pitch=RIGHT_CAMERA_PITCH, yaw=RIGHT_CAMERA_YAW))
        right_camera_bp = self.blueprint_library.find('sensor.camera.rgb')
        right_camera_bp.set_attribute('image_size_x', RIGHT_CAMERA_IMAGE_SIZE_X)
        right_camera_bp.set_attribute('image_size_y', RIGHT_CAMERA_IMAGE_SIZE_Y)
        right_camera_bp.set_attribute('fov', RIGHT_CAMERA_FOV)
        right_camera = self.carla_world.spawn_actor(right_camera_bp, right_camera_transform, attach_to=self.ego_vehicle)
        right_camera.listen(lambda image: self.right_camera_callback(image))
        self.sensor_list.append(right_camera)

        # add one camera and one Lidar for perception module
        # camera relative position related to the vehicle
        perception_camera_bp = self.blueprint_library.find('sensor.camera.rgb')
        perception_camera_transform = carla.Transform(carla.Location(x=1.5, z=2.4))
        perception_camera = self.carla_world.spawn_actor(perception_camera_bp, perception_camera_transform, attach_to=self.ego_vehicle)
        perception_camera.listen(lambda image: self.perception_camera_callback(image))
        self.sensor_list.append(perception_camera)

        lidar_bp = self.blueprint_library.find('sensor.lidar.ray_cast')
        lidar_bp.set_attribute('channels', str(32))
        lidar_bp.set_attribute('points_per_second', str(90000))
        lidar_bp.set_attribute('rotation_frequency', str(40))
        lidar_bp.set_attribute('range', str(20))

        # set the relative location
        lidar_location = carla.Location(0, 0, 2)
        lidar_rotation = carla.Rotation(0, 0, 0)
        lidar_transform = carla.Transform(lidar_location, lidar_rotation)

        # spawn the lidar
        lidar = self.carla_world.spawn_actor(lidar_bp, lidar_transform, attach_to=self.ego_vehicle)
        lidar.listen(lambda point_cloud: self.lidar_callback(point_cloud))
        self.sensor_list.append(lidar)

        # create publishers
        self.left_camera_publisher = self.create_publisher(Image, "/carla/ego_vehicle/left_camera/image", 10)
        self.right_camera_publisher = self.create_publisher(Image, "/carla/ego_vehicle/right_camera/image", 10)
        self.perception_camera_publisher = self.create_publisher(Image, "/carla/ego_vehicle/perception_camera/image", 10)
        self.perception_lidar_publisher = self.create_publisher(PointCloud2, "/carla/ego_vehicle/perception_lidar/point_cloud", 10)
        # self.waypoint_publisher = self.create_publisher(
        #     Path,
        #     '/carla/{}/waypoints'.format(self.role_name),
        #     QoSProfile(depth=1, durability=DurabilityPolicy.TRANSIENT_LOCAL))
        self.ego_pose_service = self.create_service(GetWaypointsList, "/carla/vehicle/posestamped", self.find_ego_waypoint)

        # create subscription
        self.ego_transform_subscription = self.create_subscription(Pose, "carla/ego_vehicle/control/set_transform", \
                                                                   self.ego_transform_callback, 10)
        self.ego_transform_queue = queue.Queue(maxsize=1)

        # create a thread for server updating
        self.ego_vehicle_location = None
        self.on_tick = None
        # self.on_tick = self.carla_world.on_tick(self.find_ego_waypoint) 
        self.spectator = self.carla_world.get_spectator()
        self.tick_thread = threading.Thread(target=self.world_update)
        # self.tick_thread.daemon = True
        self.tick_thread.start()

    def ego_transform_callback(self, pose):
        x = pose.position.x
        y = -1*pose.position.y
        z = pose.position.z
        quaternion = (
            pose.orientation.w,
            pose.orientation.x,
            pose.orientation.y,
            pose.orientation.z,
        )
        euler = quat2euler(quaternion)  # rad: roll, pitch, yaw
        ego_transform = carla.Transform(carla.Location(x, y, z), \
                                        carla.Rotation(pitch=math.degrees(euler[1]), \
                                                    yaw=math.degrees(-1*euler[2]), roll=math.degrees(euler[0])))
        self.ego_transform_queue.put(ego_transform)
        
        # self.get_logger().info(f" get x={x}m, y={y}m, z={z}m.")

    
    # def find_ego_waypoint(self, _):   # 用on_tick注册进服务器时会默认增加一个参数，所以需要一个占位符
        # """
        # It uses the current pose of the ego vehicle as starting point. 
        # If the vehicle is respawned or move, the route is newly calculated.
        # The calculated route is published on '/carla/<ROLE NAME>/waypoints'
        # """

        # current_location = self.ego_vehicle.get_location()
        # if self.ego_vehicle_location:
        #     dx = self.ego_vehicle_location.x - current_location.x
        #     dy = self.ego_vehicle_location.y - current_location.y
        #     distance = math.sqrt(dx * dx + dy * dy)
        #     if distance > WAYPOINT_DISTANCE:
        #         self.get_logger().info("Ego vehicle was repositioned.")
        #         self.reroute()
        # self.ego_vehicle_location = current_location       
    def find_ego_waypoint(self, request, response): 
        if request.vehiclename.data == "ego_vehicle":
            current_transform = self.ego_vehicle.get_transform()
        elif request.vehiclename.data == "adjacent0_vehicle":
            current_transform = self.adjacent0_vehicle.get_transform()

        pose_stamped = PoseStamped()
        pose_stamped.pose = trans.carla_transform_to_ros_pose(current_transform)
        pose_stamped.header.frame_id = "ego_vehicle" 
        pose_stamped.header.stamp = self.get_clock().now().to_msg()

        response.vehiclepose = pose_stamped
        return response

    def reroute(self):
        """
        Triggers a rerouting
        """
        if self.ego_vehicle is None:
            self.current_route = None
        else:
            self.current_route = self.calculate_route_distance()
        self.publish_waypoints()
    def publish_waypoints(self):
        """
        Publish the ROS message containing the waypoints
        """
        msg = Path()
        msg.header.frame_id = "map"
        msg.header.stamp = self.get_clock().now().to_msg()
        if self.current_route is not None:
            for wp in self.current_route:
                pose = PoseStamped()
                pose.pose = trans.carla_transform_to_ros_pose(wp[0].transform)
                pose.header.frame_id = msg.header.frame_id 
                pose.header.stamp = msg.header.stamp
                msg.poses.append(pose)
                self.carla_world.debug.draw_point(wp[0].transform.location, size=0.1, color=carla.Color(255,0,0), life_time=0)
                # self.world.debug.draw_arrow(wp[0].transform.location, wp[0].transform.location + carla.Location(x=math.cos(math.radians(wp[0].transform.rotation.yaw)),\
                #                                                     y=math.sin(math.radians(wp[0].transform.rotation.yaw))), \
                #                                                         thickness=0.05, arrow_size=0.1, \
                #                                                             color=carla.Color(255,255,255), life_time=0)

        self.waypoint_publisher.publish(msg)
        self.get_logger().info("Published {} waypoints.".format(len(msg.poses)))

    def calculate_route_distance(self):
        """
        Calculate a route from the current location go WAYPOINTDISTANCE
        """
        self.get_logger().info(f"Calculating route to {WAYPOINTDISTANCE} m")

        grp = GlobalRoutePlanner(self.carla_world.get_map(), sampling_resolution=0.5)
        
        # self.ego_vehicle_location = self.ego_vehicle.get_location()
        print(self.ego_vehicle_location)
        # goal = self.ego_vehicle.get_transform()
        goal = None
        for waypoint_ in self.all_waypoints:
            # get Location
            location = waypoint_.transform.location
            # rotation = waypoint_.transform.rotation
            if self.ego_vehicle_location:
                dx = self.ego_vehicle_location.x - location.x
                dy = self.ego_vehicle_location.y - location.y
                distance = math.sqrt(dx * dx + dy * dy)
                if distance > WAYPOINTDISTANCE:
                    self.get_logger().info("calculate route.")
                    goal = waypoint_.transform
                    break
        if goal is not None:
            route = grp.trace_route(self.ego_vehicle.get_location(),
                                    carla.Location(goal.location.x,
                                                goal.location.y,
                                                goal.location.z))
        else:
            print("goal is None")
            route = None

        return route
    
    def world_update(self):
        try:
            while rclpy.ok():
                new_transform = self.ego_transform_queue.get()
                self.ego_vehicle.set_transform(new_transform)
                # set the location of the spectator in the ego vehicle
                spectator_transform = new_transform
                yaw_rad = math.radians(spectator_transform.rotation.yaw)
                spectator_transform.location += carla.Location(x=CARLA_SPECTATOR_DX*math.cos(yaw_rad)-CARLA_SPECTATOR_DY*math.sin(
                    yaw_rad), y=CARLA_SPECTATOR_DX*math.sin(yaw_rad)+CARLA_SPECTATOR_DY*math.cos(yaw_rad), z=CARLA_SPECTATOR_DZ)
                self.spectator.set_transform(spectator_transform)
                # (I test that this is no need: 2023/04/27)wait for the carla server and tick
                time.sleep(self.fixed_delta_seconds)
                self.carla_world.tick()

        except queue.Empty:
            print("queue is empty")

    def left_camera_callback(self, carla_image):
        """
        会在carla服务器刷新时自动调用,所以发送频率应该等于仿真频率;
        """
        carla_image_data_array = np.ndarray(
            shape=(carla_image.height, carla_image.width, 4),
            dtype=np.uint8, buffer=carla_image.raw_data)

        # ros msg
        ros_image = self.bridge.cv2_to_imgmsg(carla_image_data_array, "bgra8")
        ros_image.header.stamp = self.get_clock().now().to_msg()
        ros_image.header.frame_id = 'leftcamera'
        self.left_camera_publisher.publish(ros_image)


    def right_camera_callback(self, carla_image):
        """
        会在carla服务器刷新时自动调用,所以发送频率应该等于仿真频率;
        """
        carla_image_data_array = np.ndarray(
            shape=(carla_image.height, carla_image.width, 4),
            dtype=np.uint8, buffer=carla_image.raw_data)

        # # ros msg
        ros_image = self.bridge.cv2_to_imgmsg(carla_image_data_array, "bgra8")
        ros_image.header.stamp = self.get_clock().now().to_msg()
        ros_image.header.frame_id = 'rightcamera'
        self.right_camera_publisher.publish(ros_image)

    def perception_camera_callback(self, carla_image):
        """
        会在carla服务器刷新时自动调用,所以发送频率应该等于仿真频率;
        """
        carla_image_data_array = np.ndarray(
            shape=(carla_image.height, carla_image.width, 4),
            dtype=np.uint8, buffer=carla_image.raw_data)
        
        ros_image = self.bridge.cv2_to_imgmsg(carla_image_data_array, "bgra8")
        ros_image.header.stamp = self.get_clock().now().to_msg()
        ros_image.header.frame_id = 'perceptioncamera'
        self.perception_camera_publisher.publish(ros_image)

    def lidar_callback(self, carla_point_cloud):

        fields = [
            PointField(name='x', offset=0, datatype=PointField.FLOAT32, count=1),
            PointField(name='y', offset=4, datatype=PointField.FLOAT32, count=1),
            PointField(name='z', offset=8, datatype=PointField.FLOAT32, count=1),
            PointField(name='intensity', offset=12, datatype=PointField.FLOAT32, count=1)
        ]

        lidar_data_ori = np.frombuffer(
            bytes(carla_point_cloud.raw_data), dtype=np.float32)
        lidar_data = np.copy(lidar_data_ori)  # lidar_data_ori is read only
        lidar_data = np.reshape(
            lidar_data, (int(lidar_data.shape[0] / 4), 4))
        
        # we take the opposite of y axis
        # (as lidar point are express in left handed coordinate system, and ros need right handed)
        lidar_data[:, 1] *= -1

        header =Header()
        header.stamp = self.get_clock().now().to_msg()
        header.frame_id = 'perceptionlidar'
        point_cloud_msg = self.create_cloud(header, fields, lidar_data)
        self.perception_lidar_publisher.publish(point_cloud_msg)

    # http://docs.ros.org/indigo/api/sensor_msgs/html/point__cloud2_8py_source.html
    def _get_struct_fmt(self, is_bigendian, fields, field_names=None):
        fmt = '>' if is_bigendian else '<'

        offset = 0
        for field in (f for f in sorted(fields, key=lambda f: f.offset)
                    if field_names is None or f.name in field_names):
            if offset < field.offset:
                fmt += 'x' * (field.offset - offset)
                offset = field.offset
            if field.datatype not in _DATATYPES:
                print('Skipping unknown PointField datatype [{}]' % field.datatype, file=sys.stderr)
            else:
                datatype_fmt, datatype_length = _DATATYPES[field.datatype]
                fmt += field.count * datatype_fmt
                offset += field.count * datatype_length

        return fmt
    def create_cloud(self, header, fields, points):
        """
        Create a L{sensor_msgs.msg.PointCloud2} message.
        @param header: The point cloud header.
        @type  header: L{std_msgs.msg.Header}
        @param fields: The point cloud fields.
        @type  fields: iterable of L{sensor_msgs.msg.PointField}
        @param points: The point cloud points.
        @type  points: list of iterables, i.e. one iterable for each point, with the
                    elements of each iterable being the values of the fields for
                    that point (in the same order as the fields parameter)
        @return: The point cloud.
        @rtype:  L{sensor_msgs.msg.PointCloud2}
        """

        cloud_struct = struct.Struct(self._get_struct_fmt(False, fields))

        buff = ctypes.create_string_buffer(cloud_struct.size * len(points))

        point_step, pack_into = cloud_struct.size, cloud_struct.pack_into
        offset = 0
        for p in points:
            pack_into(buff, offset, *p)
            offset += point_step

        return PointCloud2(header=header,
                        height=1,
                        width=len(points),
                        is_dense=False,
                        is_bigendian=False,
                        fields=fields,
                        point_step=cloud_struct.size,
                        row_step=cloud_struct.size * len(points),
                        data=buff.raw)     
    
    def destroy(self):
        if self.on_tick:
            self.carla_world.remove_on_tick(self.on_tick)
            self.get_logger().info('remove on_tick functions')
    
    def __del__(self):
        self.tick_thread.join() # make sure the node will shutdown after this thread done
        self.get_logger().info("--in bridge---wait for Stop tick thread----")
        self.destroy_node()
        self.get_logger().info("destroy node")



def main(args=None):
    """
    main function for carla simulator ROS bridge
    maintaining the communication client and the CarlaBridge object
    """
    rclpy.init(args=args)
    carla_bridge = CarlaRosBridge("bridge")

    parameters = {}
    parameters['host']    = carla_bridge.get_parameter('host').value
    parameters['port']    = carla_bridge.get_parameter('port').value
    parameters['timeout'] = carla_bridge.get_parameter('timeout').value
    parameters['town']    = carla_bridge.get_parameter('town').value

    try:
        carla_client = carla.Client(
            host=parameters['host'],
            port=parameters['port']
        )
        print("Trying to connect to {host}:{port}".format(
            host=parameters['host'], port=parameters['port']))
        carla_client.set_timeout(parameters['timeout'])

        carla_world = carla_client.get_world()
        original_settings = carla_world.get_settings()

        if "town" in parameters:
            if parameters["town"].endswith(".xodr"):
                print(
                    "Loading opendrive world from file '{}'".format(parameters["town"]))
                with open(parameters["town"]) as od_file:
                    data = od_file.read()
                carla_world = carla_client.generate_opendrive_world(str(data))
            else:
                if carla_world.get_map().name != parameters["town"]:
                    print("Loading town '{}' (previous: '{}').".format(
                        parameters["town"], carla_world.get_map().name))
                    carla_world = carla_client.load_world(parameters["town"])
            carla_world.tick()    # make sure to update the new town
        
        carla_bridge.initialize_bridge(carla_world)

        rclpy.spin(carla_bridge)

    except (IOError, RuntimeError) as e:
        print("Error: {}".format(e))
    except KeyboardInterrupt:
        print("-----Bye---Stop by user.----")
    finally:
        carla_bridge.destroy()
        print('destroy actors')

        carla_client.apply_batch([carla.command.DestroyActor(x) for x in carla_bridge.actor_list])
        for sensor in carla_bridge.sensor_list:
            sensor.destroy()
        del carla_bridge
        carla_world.apply_settings(original_settings)
        del carla_world
        del carla_client

        print("--------Shutdown by user...")  # 需要连续按两下ctrl+C
        rclpy.shutdown()


if __name__ == '__main__':
     main()