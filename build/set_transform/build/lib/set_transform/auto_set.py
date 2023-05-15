#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from transforms3d.euler import euler2quat
import math
# 1. 导入消息类型
from geometry_msgs.msg import Pose,PoseStamped
import time
from nav_msgs.msg import Path


class ego_transform_control(Node):
    """
    创建一个节点
    """
    def __init__(self,name):
        super().__init__(name)
        # 2.创建并初始化发布者成员属性pubnovel
        # self.transform_pub= self.create_publisher(Pose,"carla/ego_vehicle/control/set_transform",10)
        self.transform_pub= self.create_publisher(Path,"carla/ego_vehicle/control/set_transform",10)

    def transfrom_set(self,x1,y1,z1,yaw1,x2,y2,z2,yaw2):
        msg = Path()
        msg.header.frame_id = "ego_vehicle"
        msg.header.stamp = self.get_clock().now().to_msg()
        ego_vehicle_transform=PoseStamped()
        ego_vehicle_transform.header.frame_id = msg.header.frame_id 
        ego_vehicle_transform.header.stamp = msg.header.stamp
        ego_vehicle_transform.pose.position.x = x1
        ego_vehicle_transform.pose.position.y = y1
        ego_vehicle_transform.pose.position.z = z1
        quat1 = euler2quat(math.radians(0), math.radians(0), math.radians(yaw1))
        ego_vehicle_transform.pose.orientation.w = quat1[0]
        ego_vehicle_transform.pose.orientation.x = quat1[1]
        ego_vehicle_transform.pose.orientation.y = quat1[2]
        ego_vehicle_transform.pose.orientation.z = quat1[3]
        adjacent_vehicle_transform=PoseStamped()
        adjacent_vehicle_transform.header.frame_id = msg.header.frame_id 
        adjacent_vehicle_transform.header.stamp = msg.header.stamp        
        adjacent_vehicle_transform.pose.position.x = x2
        adjacent_vehicle_transform.pose.position.y = y2
        adjacent_vehicle_transform.pose.position.z = z2
        quat2 = euler2quat(math.radians(0), math.radians(0), math.radians(yaw2))
        adjacent_vehicle_transform.pose.orientation.w = quat2[0]
        adjacent_vehicle_transform.pose.orientation.x = quat2[1]
        adjacent_vehicle_transform.pose.orientation.y = quat2[2]
        adjacent_vehicle_transform.pose.orientation.z = quat2[3]
        msg.poses.append(ego_vehicle_transform)
        msg.poses.append(adjacent_vehicle_transform)
        self.transform_pub.publish(msg)







class tra_transform_control(Node):
    """
    创建一个节点
    """
    def __init__(self,name):
        super().__init__(name)
        # 2.创建并初始化发布者成员属性pubnovel
        self.transform_pub= self.create_publisher(Pose,"/carla/adjacent_vehicle/control/set_transform",10)


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
        
xfile1=open("/home/cec20/Yangjiaxin/my-carla-ros-bridge/src/Natural_road_set_transform/set_transform/ego_x.txt")
data1=xfile1.read()
ego_x=data1.split(",")
del ego_x[len(ego_x)-1]
xfile1.close()

xfile2=open("/home/cec20/Yangjiaxin/my-carla-ros-bridge/src/Natural_road_set_transform/set_transform/ego_y.txt")
data1=xfile2.read()
ego_y=data1.split(",")
del ego_y[len(ego_y)-1]
xfile2.close()

xfile3=open("/home/cec20/Yangjiaxin/my-carla-ros-bridge/src/Natural_road_set_transform/set_transform/ego_yaw.txt")
data1=xfile3.read()
ego_yaw=data1.split(",")
del ego_yaw[len(ego_yaw)-1]
xfile3.close()

xfile4=open("/home/cec20/Yangjiaxin/my-carla-ros-bridge/src/Natural_road_set_transform/set_transform/tra_x.txt")
data1=xfile4.read()
tra_x=data1.split(",")
del tra_x[len(tra_x)-1]
xfile4.close()

xfile5=open("/home/cec20/Yangjiaxin/my-carla-ros-bridge/src/Natural_road_set_transform/set_transform/tra_y.txt")
data1=xfile5.read()
tra_y=data1.split(",")
del tra_y[len(tra_y)-1]
xfile5.close()

xfile6=open("/home/cec20/Yangjiaxin/my-carla-ros-bridge/src/Natural_road_set_transform/set_transform/tra_yaw.txt")
data1=xfile6.read()
tra_yaw=data1.split(",")
del tra_yaw[len(tra_yaw)-1]
xfile6.close()

# for i,n in enumerate(ego_y):
#     if n == "0":
#         del ego_x[int(i)+1:]
#         del ego_y[int(i)+1:]
#         del ego_yaw[int(i)+1:]
#         del tra_x[int(i)+1:]
#         del tra_y[int(i)+1:]
#         del tra_yaw[int(i)+1:]
#         break


    
        



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
    # node2 = tra_transform_control("tra")
    i=int(0)
    while True:
        x1=float(ego_x[i])
        y1=float(ego_y[i])
        yaw1=math.degrees(float(ego_yaw[i]))
        x2=float(tra_x[i])
        y2=float(tra_y[i])
        yaw2=math.degrees(float(tra_yaw[i]))
        node1.transfrom_set(x1,y1,0.0,yaw1,x2,y2,0.0,yaw2)
        # node1.transfrom_set(x1,y1,0.0,yaw1)
        # node2.transfrom_set(x2,y2,0.0,yaw2)
        # if i>=1:
        #     x3=float(ego_x[i-1])
        #     y3=float(ego_y[i-1])
        #     v1=3.6*math.sqrt((x1-x3)**2+(y1-y3)**2)/0.02
        #     v2="%.1fkm/h"%v1
        #     speedshow(v2)
        if i == len(ego_x)-1:
            i=int(0)
        else:
            i=i+1
        time.sleep(1/60)




    rclpy.spin(node1) # 保持节点运行，检测是否收到退出指令（Ctrl+C）

    rclpy.shutdown() # 关闭rclpy