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

xfile7=open("/home/zhang/CARLA_0.9.13/PythonAPI/Natural_road_code/Centerroad_x.txt")
data1=xfile7.read()
centerroad_x=data1.split(",")
del centerroad_x[len(centerroad_x)-1]
xfile7.close()

xfile8=open("/home/zhang/CARLA_0.9.13/PythonAPI/Natural_road_code/Centerroad_y.txt")
data1=xfile8.read()
centerroad_y=data1.split(",")
del centerroad_y[len(centerroad_y)-1]
xfile8.close()

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


Init_dis=float(80/5)
Ref_len=0
for i in range(0,len(centerroad_x)-1):
    x1=float(centerroad_x[i])
    x2=float(centerroad_x[i+1])
    y1=float(centerroad_y[i])
    y2=float(centerroad_y[i+1])    
    dis=math.sqrt((x2-x1)**2+(y2-y1)**2)
    Ref_len=Ref_len+dis

           
FreX=[]
Tra_X=[]
Tra_Y=[]
FreX.append(Init_dis)

def Frenet2Cartesian(x3):
    if x3>Ref_len:
        x3=x3-Ref_len
    dis1=0
    for idx1 in range(0,len(centerroad_x)-1):
        idx2=idx1+1
        x1=float(centerroad_x[idx1])
        x2=float(centerroad_x[idx2])
        y1=float(centerroad_y[idx1])
        y2=float(centerroad_y[idx2])    
        dis=math.sqrt((x2-x1)**2+(y2-y1)**2)
        if x3<dis1+dis:
            Lane_yaw=math.atan2((y2-y1),(x2-x1))
            cartesian_x=x1+(x3-dis1)*math.cos(Lane_yaw)-2*math.sin(Lane_yaw)
            cartesian_y=y1+(x3-dis1)*math.sin(Lane_yaw)+2*math.cos(Lane_yaw)
            Tra_X.append(round(cartesian_x,4))
            Tra_Y.append(round(cartesian_y,4))
            break
        dis1+=dis

def Cal_yaw():
    if len(Tra_X)>2:
        yaw=math.atan2((float(Tra_Y[-1])-float(Tra_Y[-2])),(float(Tra_X[-1])-float(Tra_X[-2])))
    else:
        yaw=1.5708
    return yaw





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
    i=int(0)
    while True:
        x1=float(ego_x[i])
        y1=float(ego_y[i])
        yaw1=math.degrees(float(ego_yaw[i]))
        node1.transfrom_set(x1,y1,0.0,yaw1)
        x2=float(ego_x[i-1])
        y2=float(ego_y[i-1])
        v1=3.6*math.sqrt((x1-x2)**2+(y1-y2)**2)/0.02
        v2="%.1fkm/h"%v1
        x3=float(FreX[-1])
        Frenet2Cartesian(x3)
        x3=x3+0.02*45/3.6
        FreX.append(x3)
        x4=float(Tra_X[-1])
        y4=float(Tra_Y[-1])
        yaw4=Cal_yaw()
        yaw4=math.degrees(float(yaw4))
        node2.transfrom_set(x4,y4,0.0,yaw4)
        # speedshow(v2)      
        i=i+1
        if i == len(ego_x)-1:
            i=int(0)
        time.sleep(0.02)

    rclpy.spin(node1) # 保持节点运行，检测是否收到退出指令（Ctrl+C）
    rclpy.spin(node2) # 保持节点运行，检测是否收到退出指令（Ctrl+C）
    
    
    rclpy.shutdown() # 关闭rclpy