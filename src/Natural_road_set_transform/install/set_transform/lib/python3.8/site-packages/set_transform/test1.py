#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from transforms3d.euler import euler2quat
import math
# 1. 导入消息类型
from geometry_msgs.msg import Pose,Twist,Vector3
from std_msgs.msg import Bool
import time
from tkinter import *
import tkinter as tk


actor_list = []
window1 = tk.Tk()  # 实例化TK
window1.title("Speed")
window1.geometry('300x100+900+900')

xfile1=open("/home/zhang/CARLA_0.9.13/PythonAPI/Natural_road_code/ego_x.txt")
data1=xfile1.read()
ego_x=data1.split(",")
del ego_x[len(ego_x)-1]
xfile1.close()

xfile2=open("/home/zhang/CARLA_0.9.13/PythonAPI/Natural_road_code/ego_y.txt")
data1=xfile2.read()
ego_y=data1.split(",")
del ego_y[len(ego_y)-1]
xfile2.close()

xfile3=open("/home/zhang/CARLA_0.9.13/PythonAPI/Natural_road_code/ego_yaw.txt")
data1=xfile3.read()
ego_yaw=data1.split(",")
del ego_yaw[len(ego_yaw)-1]
xfile3.close()

xfile4=open("/home/zhang/CARLA_0.9.13/PythonAPI/Natural_road_code/tra_x.txt")
data1=xfile4.read()
tra_x=data1.split(",")
del tra_x[len(tra_x)-1]
xfile4.close()

xfile5=open("/home/zhang/CARLA_0.9.13/PythonAPI/Natural_road_code/tra_y.txt")
data1=xfile5.read()
tra_y=data1.split(",")
del tra_y[len(tra_y)-1]
xfile5.close()

xfile6=open("/home/zhang/CARLA_0.9.13/PythonAPI/Natural_road_code/tra_yaw.txt")
data1=xfile6.read()
tra_yaw=data1.split(",")
del tra_yaw[len(tra_yaw)-1]
xfile6.close()

class ego_transform_control(Node):
    """
    创建一个节点
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

class tra_transform_control(Node):
    """
    创建一个节点
    """
    def __init__(self,name):
        super().__init__(name)
        # 2.创建并初始化发布者成员属性pubnovel
        self.transform_pub= self.create_publisher(Pose,"carla/hero/control/set_transform",10)
        self.autopilot_set= self.create_publisher(Bool,"carla/hero/enable_autopilot",10)
        self.velocity_set= self.create_publisher(Twist,"carla/hero/control/set_target_velocity",10)


    def transfrom_set(self,x,y,z,yaw):
        tra_vehicle_transform=Pose()
        tra_vehicle_transform.position.x = x
        tra_vehicle_transform.position.y = y
        tra_vehicle_transform.position.z = z
        quat = euler2quat(math.radians(0), math.radians(0), math.radians(yaw))

        tra_vehicle_transform.orientation.w = quat[0]
        tra_vehicle_transform.orientation.x = quat[1]
        tra_vehicle_transform.orientation.y = quat[2]
        tra_vehicle_transform.orientation.z = quat[3]
        self.transform_pub.publish(tra_vehicle_transform)
        



def speedshow(str1):
    Label(window1,text=str1,font=("宋体",20),fg = "black" , width = 12,height = 2).place(x = 50,y = 20)
    window1.update()
    window1.after(2)

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
    node1 = ego_transform_control("ego")  # 新建一个节点
    node2 = tra_transform_control("tra")
    node1.transfrom_set(float(ego_x[0]),float(ego_y[0]),0.0,float(ego_yaw[0]))    
    node2.transfrom_set(float(tra_x[0]),float(tra_y[0]),0.0,float(tra_yaw[0]))    
    i=int(0)
    signal1=Bool()
    signal1.data=True
    signal2=Bool()
    signal2.data=False
    node2.autopilot_set.publish(signal1)
    hero_velocity=Twist()
    v3=Vector3()
    while True:
        x1=float(ego_x[i])
        y1=float(ego_y[i])
        yaw1=math.degrees(float(ego_yaw[i]))
        x2=float(tra_x[i])
        y2=float(tra_y[i])
        yaw2=math.degrees(float(tra_yaw[i]))
        node1.transfrom_set(x1,y1,0.0,yaw1)
        x3=float(ego_x[i-1])
        y3=float(ego_y[i-1])
        v1=3.6*math.sqrt((x1-x3)**2+(y1-y3)**2)/0.02
        v2="%.1fkm/h"%v1
        # speedshow(v2)      
        v3.x=float(v1)
        hero_velocity.linear=v3
        node2.velocity_set.publish(hero_velocity)
        i=i+1
        if i == len(ego_x)-1:
            i=int(0)
        time.sleep(0.02)

    rclpy.spin(node1) # 保持节点运行，检测是否收到退出指令（Ctrl+C）
    rclpy.spin(node2) # 保持节点运行，检测是否收到退出指令（Ctrl+C）
    
    
    rclpy.shutdown() # 关闭rclpy