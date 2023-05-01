
import rclpy
from rclpy.node import Node

import carla
import collections


from waypoints_types.srv import GetWaypointsList
from kvaser_msg_interfaces.msg import ControlCmd
import carla_common.transforms as trans


class WaypointsListNode(Node):
    def __init__(self, name, carla_world):
        super().__init__(name)
        self.carla_world = carla_world
        
        self.role_name =  "ego_vehicle"
        self._buffer_size = 5
        self._waypoints_queue = collections.deque(maxlen=20000)
        self._waypoint_buffer = collections.deque(maxlen=self._buffer_size)
        self.lane_client = self.create_client(
            GetWaypointsList,
            "/carla/vehicle/posestamped"
            )
        while not self.lane_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.request = GetWaypointsList.Request()

        self.control_publisher = self.create_publisher(ControlCmd, "/ControlBottom", 10)
        
        # self.ego_vehicle_location_subscription = self.create_subscription(
        #     Pose, 
        #     "/carla/ego_vehicle/control/set_transform", 
        #     self.listener_callback, 10)

    
    def timer_callback(self):
        msg = ControlCmd()
        msg.time = float(1.23)
        msg.stangle = float(-3.0)
        msg.vehiclevx = float(40.0)
        self.control_publisher.publish(msg)
        self.get_logger().info(f'Publishing : {msg.time} s, {msg.stangle} deg, {msg.vehiclevx} km/h')

    def send_request(self):
        self.request.vehiclename.data = self.role_name
        self.future = self.lane_client.call_async(self.request)  # 异步方式发送请求（通过其他线程发送请求）
        rclpy.spin_until_future_complete(self, self.future)
        if self.future.result() is not None:
            self.ego_pose = self.future.result().vehiclepose
            self.ego_transform = trans.ros_pose_to_carla_transform(self.ego_pose.pose)
            self.get_logger().info(f"receive from service: {self.ego_transform}")
            # return self.ego_transform
        else:
            self.get_logger().info("Service call failed")

        # self._waypoint_buffer.clear()
        # self._waypoints_queue.clear()
        # self._waypoints_queue.extend([pose.pose for pose in path_msg.poses])  #Posestamp
        # for pose in path_msg.poses:
        #     self.get_logger().info(f'get waypoint {pose.pose.position.x}, {pose.pose.position.y}')

def connect_to_carla():

    print("Waiting for CARLA world (topic: /carla/world_info)...")
    host =  "127.0.0.1"
    port = 2000
    timeout = 10
    print("CARLA world available. Trying to connect to {host}:{port}".format(
        host=host, port=port))

    carla_client = carla.Client(host=host, port=port)
    carla_client.set_timeout(timeout)

    try:
        carla_world = carla_client.get_world()
    except RuntimeError as e:
        print("Error while connecting to Carla: {}".format(e))
        raise e
    print("Connected to Carla.")
    return carla_world

def main(args=None):
    carla_world = connect_to_carla()

    # key = True
    # try:
    #     while key:
    #         pass
    # except KeyboardInterrupt:
    #     key = False

    rclpy.init(args=args)
    node = WaypointsListNode("trajectory_control", carla_world)
    node.send_request()
    # rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
