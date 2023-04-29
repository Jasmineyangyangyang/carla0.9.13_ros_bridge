"""
basic: spawn ego_vehicle and add camera and lidar 2023/04-27

"""
import rclpy
from rclpy.node import Node

import carla
import numpy as np
import math
from cv_bridge import CvBridge
import sys

import queue
import threading

from transforms3d.euler import quat2euler
from geometry_msgs.msg import Pose 
from sensor_msgs.msg import Image
from sensor_msgs.msg import PointCloud2, PointField
from std_msgs.msg import Header

# for lidar point cloud
import struct
import ctypes

CARLA_FPS = 60.0
CARLA_SCENE_NAME = "Bend03"
CARLA_EGO_MODEL_FILTER = "model3"
CARLA_EGO_STATE_TOPIC_NAME = "ego_vehicle"
CARLA_EGO_INIT_X = 417.495391845703
CARLA_EGO_INIT_Y = 252.950531005859
CARLA_EGO_INIT_Z = 0.1
CARLA_EGO_INIT_YAW = -12.729858/180.*math.pi
CARLA_SPECTATOR_DX = 0.10
CARLA_SPECTATOR_DY = -0.40
CARLA_SPECTATOR_DZ = 1.22

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

RIGHT_CAMERA_X = 0.3
RIGHT_CAMERA_Y = 1.0
RIGHT_CAMERA_Z = 1.3
RIGHT_CAMERA_ROLL = 0.0
RIGHT_CAMERA_PITCH = 20.0
RIGHT_CAMERA_YAW = 150.0
RIGHT_CAMERA_IMAGE_SIZE_X = str(640)
RIGHT_CAMERA_IMAGE_SIZE_Y = str(400)

_DATATYPES = {}
_DATATYPES[PointField.INT8] = ('b', 1)
_DATATYPES[PointField.UINT8] = ('B', 1)
_DATATYPES[PointField.INT16] = ('h', 2)
_DATATYPES[PointField.UINT16] = ('H', 2)
_DATATYPES[PointField.INT32] = ('i', 4)
_DATATYPES[PointField.UINT32] = ('I', 4)
_DATATYPES[PointField.FLOAT32] = ('f', 4)
_DATATYPES[PointField.FLOAT64] = ('d', 8)


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
        self.ego_vehicle_name = self.get_parameter("ego_vehicle_role_name").value

        self.carla_world = carla_world
        self.carla_settings = self.carla_world.get_settings()
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
        left_camera = self.carla_world.spawn_actor(left_camera_bp, left_camera_transform, attach_to=self.ego_vehicle)
        left_camera.listen(lambda image: self.left_camera_callback(image))
        self.sensor_list.append(left_camera)

        right_camera_transform = carla.Transform(carla.Location(x=RIGHT_CAMERA_X, y=RIGHT_CAMERA_Y, z=RIGHT_CAMERA_Z),\
                                                 carla.Rotation(roll=RIGHT_CAMERA_ROLL, pitch=RIGHT_CAMERA_PITCH, yaw=RIGHT_CAMERA_YAW))
        right_camera_bp = self.blueprint_library.find('sensor.camera.rgb')
        right_camera_bp.set_attribute('image_size_x', RIGHT_CAMERA_IMAGE_SIZE_X)
        right_camera_bp.set_attribute('image_size_y', RIGHT_CAMERA_IMAGE_SIZE_Y)
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

        # update world to spawn lidar
        self.carla_world.tick() 

        # create publishers
        self.left_camera_publisher = self.create_publisher(Image, "/carla/ego_vehicle/left_camera/image", 10)
        self.right_camera_publisher = self.create_publisher(Image, "/carla/ego_vehicle/right_camera/image", 10)
        self.perception_camera_publisher = self.create_publisher(Image, "/carla/ego_vehicle/perception_camera/image", 10)
        self.perception_lidar_publisher = self.create_publisher(PointCloud2, "/carla/ego_vehicle/perception_lidar/point_cloud", 10)


        # create subscription
        self.ego_transform_subscription = self.create_subscription(Pose, "carla/ego_vehicle/control/set_transform", \
                                                                   self.ego_transform_callback, 10)
        self.ego_transform_queue = queue.Queue(maxsize=600)


        # create a thread for server updating
        self.spectator = self.carla_world.get_spectator()
        self.tick_thread = threading.Thread(target=self.world_update)
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
        euler = quat2euler(quaternion)  # roll, pitch, yaw
        yaw_rad = -1*euler[2]
        ego_transform = carla.Transform(carla.Location(x, y, z), \
                                        carla.Rotation(pitch=math.degrees(euler[1]), \
                                                       yaw=math.degrees(-1*euler[2]), roll=math.degrees(euler[0])))
        self.ego_transform_queue.put(ego_transform)
        # self.get_logger().info(f" get x={x}m, y={y}m, z={z}m.")
    
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
                # time.sleep(self.fixed_delta_seconds)
                self.carla_world.tick()

        except queue.Empty:
            print("queue is empty")
        
    
    def left_camera_callback(self, carla_image):
        """
        会在carla服务器刷新时自动调用,所以发送频率应该等于方振频率;
        """
        carla_image_data_array = np.ndarray(
            shape=(carla_image.height, carla_image.width, 4),
            dtype=np.uint8, buffer=carla_image.raw_data)
        
        ros_image = self.bridge.cv2_to_imgmsg(carla_image_data_array, "bgra8")
        ros_image.header.stamp = self.get_clock().now().to_msg()
        ros_image.header.frame_id = 'leftcamera'
        self.left_camera_publisher.publish(ros_image)


    def right_camera_callback(self, carla_image):
        """
        会在carla服务器刷新时自动调用,所以发送频率应该等于方振频率;
        """
        carla_image_data_array = np.ndarray(
            shape=(carla_image.height, carla_image.width, 4),
            dtype=np.uint8, buffer=carla_image.raw_data)
        
        ros_image = self.bridge.cv2_to_imgmsg(carla_image_data_array, "bgra8")
        ros_image.header.stamp = self.get_clock().now().to_msg()
        ros_image.header.frame_id = 'rightcamera'
        self.right_camera_publisher.publish(ros_image)

    def perception_camera_callback(self, carla_image):
        """
        会在carla服务器刷新时自动调用,所以发送频率应该等于方振频率;
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

        lidar_data = np.fromstring(
            bytes(carla_point_cloud.raw_data), dtype=np.float32)
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
    
    def __del__(self):
        self.tick_thread.join() # make sure the node will shutdown after this thread done

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
        carla_world.apply_settings(original_settings)
        print('destroy actors')
        carla_client.apply_batch([carla.command.DestroyActor(x) for x in carla_bridge.actor_list])
        for sensor in carla_bridge.sensor_list:
            sensor.destroy()
        print('done.')
        carla_bridge.destroy_node()
        rclpy.shutdown()
        del carla_world
        del carla_client



    rclpy.shutdown()

if __name__ == '__main__':
     main()