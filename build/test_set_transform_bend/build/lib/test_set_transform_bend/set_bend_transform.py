
import csv
from math import * 
import time

import rclpy
from rclpy.node import Node
from transforms3d.euler import euler2quat
import math
# 1. 导入消息类型
from geometry_msgs.msg import Pose

      
class Transform_control(Node):
    def __init__(self, name):
        super().__init__(name)
        self.transform_pub = self.create_publisher(Pose, "carla/ego_vehicle/control/set_transform", 10)  # 创建发布者对象（消息类型、话题名、队列长度）
    
    def transform_set(self, x, y, z, yaw):
        # 构造 ROS2 消息
        self.ego_vehicle_pose = Pose()
        self.ego_vehicle_pose.position.x = x
        self.ego_vehicle_pose.position.y = -y
        self.ego_vehicle_pose.position.z = z
        roll = 0.0  # deg
        pitch = 0.0 # deg
        quat = euler2quat(math.radians(roll), math.radians(pitch), -yaw)  #将角度转成弧度
        self.ego_vehicle_pose.orientation.w = quat[0]
        self.ego_vehicle_pose.orientation.x = quat[1]
        self.ego_vehicle_pose.orientation.y = quat[2]
        self.ego_vehicle_pose.orientation.z = quat[3]

        ego_vehicle_transform = self.ego_vehicle_pose
        self.transform_pub.publish(ego_vehicle_transform)
        self.get_logger().info(f'x = {str(ego_vehicle_transform.position.x)} m')
        self.get_logger().info(f'y = {str(ego_vehicle_transform.position.y)} m')
        self.get_logger().info(f'yaw = {str(-yaw)} m')


def read_waypoints():
        # read data
        with open('/home/cec20/Yangjiaxin/carla-ros-bridge/src/ros-bridge/test_set_transform_bend/test_set_transform_bend/Bend03_left_1.csv') as f:
            reader = csv.reader(f)
            data = []
            for row in reader:
                data.append(row)
        return data

def main(args=None):
    """
    ros2运行该节点的入口函数
    1. 导入库文件
    2. 初始化客户端库
    3. 新建节点
    4. spin循环节点
    5. 销毁节点，关闭客户端库
    """
    data = read_waypoints()
    rclpy.init(args=args)
    node = Transform_control("vehicle_transform")
    # rclpy.spin(node)              #保持节点运行，直到检测收到退出指令（Ctrl+C)）
    x0, y0, z0 = data[0]
    x0 = float(x0)
    y0 = -1*float(y0)
    z0 = float(z0)

    try:
        while True:     
            for data_ in data[1:-1]:
                x, y, z = data_
                x = float(x)
                y = float(y)
                z = float(z)
                yaw = atan((y - y0)/(x - x0))
                if (x - x0)<0 and (y - y0)<0:
                    yaw = yaw-pi
                if (x - x0)<0 and (y - y0)>0:
                    yaw = yaw+pi
                node.transform_set(x, y, z, yaw)

                x0 = x
                y0 = y
                z0 = z
                time.sleep(0.01)  # 刷新率 30Hz
    except KeyboardInterrupt:
        node.get_logger().info("User requested shut down.")
    finally:
        node.destroy_node()
        rclpy.shutdown()              #关闭ROS2 python接口

if __name__ == '__main__':
    main()