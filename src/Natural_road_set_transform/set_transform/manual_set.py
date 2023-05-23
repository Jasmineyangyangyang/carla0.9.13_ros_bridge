#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from transforms3d.euler import euler2quat
import math
# 1. 导入消息类型
from geometry_msgs.msg import Pose




class Transform_control(Node):
    """
    创建一个李四节点，并在初始化时输出一个话
    """
    def __init__(self,name):
        super().__init__(name)
        # 2.创建并初始化发布者成员属性pubnovel
        self.transform_pub= self.create_publisher(Pose,"carla/ego_vehicle/control/set_transform",10)


    def transfrom_set(self,x,y,z,yaw):
        ego_vehicle_transform=Pose()
        ego_vehicle_transform.position.x = x
        ego_vehicle_transform.position.y = y
        ego_vehicle_transform.position.z = z
        quat = euler2quat(math.radians(0), math.radians(0), math.radians(yaw))

        ego_vehicle_transform.orientation.w = quat[0]
        ego_vehicle_transform.orientation.x = quat[1]
        ego_vehicle_transform.orientation.y = quat[2]
        ego_vehicle_transform.orientation.z = quat[3]
        self.transform_pub.publish(ego_vehicle_transform)
        



    
        



def main(args=None):
    """
    ros2运行该节点的入口函数
    1. 导入库文件
    2. 初始化客户端库
    3. 新建节点
    4. spin循环节点
    5. 关闭客户端库
    """
    rclpy.init(args=args) # 初始化rclpy
    node1 = Transform_control("front")  # 新建一个节点
    while True:
        x1=float(input("请输入x的值"))
        y1=float(input("请输入y的值"))
        z1=float(input("请输入z的值"))
        yaw1=float(input("请输入yaw的值"))
        node1.transfrom_set(x1,y1,z1,yaw1)
        # a=str(input("是否继续设置车辆位置 y/n"))
        # if a=="n":
        #     break

    rclpy.spin(node1) # 保持节点运行，检测是否收到退出指令（Ctrl+C）

    rclpy.shutdown() # 关闭rclpy