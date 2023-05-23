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
from nav_msgs.msg import Path



CARLA_FPS = 60.0
CARLA_SCENE_NAME = "Natural_road"
CARLA_EGO_MODEL_FILTER = "model3"
CARLA_EGO_STATE_TOPIC_NAME = "ego_vehicle"
CARLA_EGO_INIT_X = -158.
CARLA_EGO_INIT_Y = 23.9
CARLA_EGO_INIT_Z = 0.1
CARLA_EGO_INIT_YAW = -90/180.*math.pi
CARLA_SPECTATOR_DX = -0.10
CARLA_SPECTATOR_DY = -0.35
CARLA_SPECTATOR_DZ = 1.2

CARLA_ADJACENT_MODEL_FILTER = "model3"
CARLA_ADJACENT_STATE_TOPIC_NAME = "adjacent"
CARLA_ADJACENT_INIT_X = -162.
CARLA_ADJACENT_INIT_Y = 7.9
CARLA_ADJACENT_INIT_Z = 0.1
CARLA_ADJACENT_INIT_YAW = -90/180.*math.pi


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

        # spawn the adjacent vehicle actor
        self.adjacent_vehicle_bp = self.blueprint_library.filter(
            CARLA_ADJACENT_MODEL_FILTER)[0]
        self.adjacent_vehicle_bp.set_attribute('color', '255, 0, 0')
        self.adjacent_spawn_point = carla.Transform(carla.Location(
            x=CARLA_ADJACENT_INIT_X, y=CARLA_ADJACENT_INIT_Y, z=CARLA_ADJACENT_INIT_Z),
            carla.Rotation(yaw=CARLA_ADJACENT_INIT_YAW*180/math.pi))
        self.adjacent_vehicle = self.carla_world.spawn_actor(
            self.adjacent_vehicle_bp, self.adjacent_spawn_point)
        self.actor_list.append(self.adjacent_vehicle)


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

        # create publishers
        self.left_camera_publisher = self.create_publisher(Image, "/carla/ego_vehicle/left_camera/image", 10)
        self.right_camera_publisher = self.create_publisher(Image, "/carla/ego_vehicle/right_camera/image", 10)

        # create subscription
        self.ego_transform_subscription = self.create_subscription(Path,'carla/ego_vehicle/control/set_transform', self.ego_transform_callback,10)

        self.ego_transform_queue = queue.Queue(maxsize=1)
        self.adjacent_transform_queue = queue.Queue(maxsize=1)
        self.lock = threading.Lock()

        # create a thread for server updating
        self.on_tick = None
        # self.on_tick = self.carla_world.on_tick(self.find_ego_waypoint) 
        self.spectator = self.carla_world.get_spectator()
        self.tick_thread = threading.Thread(target=self.world_update)
        self.tick_thread.start()
    

    def ego_transform_callback(self, path):
        ego_transform = None
        adjacent_transform = None
        pose1=path.poses[0].pose
        pose2=path.poses[1].pose
        x1 = pose1.position.x
        y1 = -1*pose1.position.y
        z1 = pose1.position.z
        quaternion1 = (
            pose1.orientation.w,
            pose1.orientation.x,
            pose1.orientation.y,
            pose1.orientation.z,
        )
        euler1 = quat2euler(quaternion1)  # rad: roll, pitch, yaw
        ego_transform = carla.Transform(carla.Location(x1, y1, z1), \
                                        carla.Rotation(pitch=math.degrees(euler1[1]), \
                                                    yaw=math.degrees(-1*euler1[2]), roll=math.degrees(euler1[0])))
        # self.lock.acquire()
        # try:
        #     self.ego_transform_queue.put(ego_transform)
        # finally:
        #     self.lock.release()
        self.ego_transform_queue.put(ego_transform)
        # print(ego_transform)
        x2 = pose2.position.x
        y2 = -1*pose2.position.y
        z2 = pose2.position.z
        quaternion2 = (
            pose2.orientation.w,
            pose2.orientation.x,
            pose2.orientation.y,
            pose2.orientation.z,
        )
        euler2 = quat2euler(quaternion2)  # rad: roll, pitch, yaw
        adjacent_transform = carla.Transform(carla.Location(x2, y2, z2), \
                                        carla.Rotation(pitch=math.degrees(euler2[1]), \
                                                    yaw=math.degrees(-1*euler2[2]), roll=math.degrees(euler2[0])))
        self.adjacent_transform_queue.put(adjacent_transform)
        # print(adjacent_transform)
        # self.adjacent_vehicle.set_transform(adjacent_transform)
        # spectator_transform = ego_transform
        # yaw_rad = math.radians(spectator_transform.rotation.yaw)
        # spectator_transform.location += carla.Location(x=CARLA_SPECTATOR_DX*math.cos(yaw_rad)-CARLA_SPECTATOR_DY*math.sin(
        #             yaw_rad), y=CARLA_SPECTATOR_DX*math.sin(yaw_rad)+CARLA_SPECTATOR_DY*math.cos(yaw_rad), z=CARLA_SPECTATOR_DZ)#CARLA_SPECTATOR_DZ
        # self.spectator.set_transform(spectator_transform)
        # self.carla_world.tick()
        # self.ego_transform_queue.put(ego_transform)
        # self.adjacent_vehicle.set_transform(adjacent_transform)
        # self.get_logger().info(f" get x={x}m, y={y}m, z={z}m.")
    
    def world_update(self):
        try:
            while rclpy.ok():
                new_transform1 = self.ego_transform_queue.get()
                self.ego_vehicle.set_transform(new_transform1)
                new_transform2 = self.adjacent_transform_queue.get()
                self.adjacent_vehicle.set_transform(new_transform2)  
                # set the location of the spectator in the ego vehicle
                spectator_transform = new_transform1
                yaw_rad = math.radians(spectator_transform.rotation.yaw)
                spectator_transform.location += carla.Location(x=CARLA_SPECTATOR_DX*math.cos(yaw_rad)-CARLA_SPECTATOR_DY*math.sin(
                    yaw_rad), y=CARLA_SPECTATOR_DX*math.sin(yaw_rad)+CARLA_SPECTATOR_DY*math.cos(yaw_rad), z=CARLA_SPECTATOR_DZ)#CARLA_SPECTATOR_DZ
                # spectator_transform.location = carla.Location(x=-162.0, y=23.9, z=1.3)#CARLA_SPECTATOR_DZ
                # spectator_transform.rotation = carla.Rotation(pitch=float(0),yaw=float(-90))
                self.spectator.set_transform(spectator_transform)
                # (I test that this is no need: 2023/04/27)wait for the carla server and tick
                # time.sleep(self.fixed_delta_seconds)
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

    
    def destroy(self):
        if self.on_tick:
            self.carla_world.remove_on_tick(self.on_tick)
            self.get_logger().info('remove on_tick functions')
    
    def __del__(self):
        # self.tick_thread.join() # make sure the node will shutdown after this thread done
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