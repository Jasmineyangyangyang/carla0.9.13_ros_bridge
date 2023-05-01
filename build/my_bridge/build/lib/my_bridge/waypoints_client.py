
import rclpy
from rclpy import Node
from waypoints_types.srv import GetWaypointsList

class TrajectoryControlNode(Node):
    def __init__(self, name):
        super().__init__(name)
        role_name =  "ego_vehicle"
        self._buffer_size = 5
        self._waypoints_queue = collections.deque(maxlen=20000)
        self._waypoint_buffer = collections.deque(maxlen=self._buffer_size)
        self.lane_subscriber = self.create_subscription(
            Path,
            "/carla/{}/waypoints".format(role_name),
            self.path_cb,
            10)
        
        self.pub = self.create_publisher(ControlCmd, "/ControlBottom", 10)
        # self.sub = self.create_subscription()
        # self.timer = self.create_timer(0.01, self.timer_callback)   # 0.01秒
    
    def timer_callback(self):
        msg = ControlCmd()
        msg.time = float(1.23)
        msg.stangle = float(-3.0)
        msg.vehiclevx = float(40.0)
        self.pub.publish(msg)
        self.get_logger().info(f'Publishing : {msg.time} s, {msg.stangle} deg, {msg.vehiclevx} km/h')

    def path_cb(self, path_msg):
        self._waypoint_buffer.clear()
        self._waypoints_queue.clear()
        self._waypoints_queue.extend([pose.pose for pose in path_msg.poses])  #Posestamp
        for pose in path_msg.poses:
            self.get_logger().info(f'get waypoint {pose.pose.position.x}, {pose.pose.position.y}')


def main(args=None):
    rclpy.init(args=args)
    node = TrajectoryControlNode("trajectory_control")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
