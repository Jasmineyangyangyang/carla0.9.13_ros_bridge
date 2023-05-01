#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
# 1. 导入消息类型
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge


cv_bridge = CvBridge()

class ImageNode(Node):
    """
    创建一个image节点，接受图像并用cv显示
    """
    def __init__(self,name):
        super().__init__(name)
        # 2.创建并初始化发布者成员属性pubnovel
        # self.frontimage= self.create_subscription(Image,"carla/ego_vehicle/rgb_front/image",self.imageshow1,60)
        self.leftimage = self.create_subscription(Image,"carla/ego_vehicle/left_camera/image",self.imageshow2,60)
        self.rightimage = self.create_subscription(Image,"carla/ego_vehicle/right_camera/image",self.imageshow3,60)

    def imageshow1(self,img_msg):
        img1 = cv_bridge.imgmsg_to_cv2(img_msg)         
        cv2.imshow('front_view', img1)
        # cv2.moveWindow("front_view",550,0)
        cv2.moveWindow("front_view",0,0)
        cv2.waitKey(1)

    def imageshow2(self,img_msg):
        img2 = cv_bridge.imgmsg_to_cv2(img_msg)         
        cv2.imshow('rear_view_L', img2)
        cv2.moveWindow("rear_view_L",250,700)
        cv2.waitKey(1)

    def imageshow3(self,img_msg):
        img3 = cv_bridge.imgmsg_to_cv2(img_msg)         
        cv2.imshow('rear_view_R', img3)
        cv2.moveWindow("rear_view_R",2500,700)
        cv2.waitKey(1)
    

        

def main(args=None):
    '''
    1. 编程接口初始化 rclpy.init(args=args)
    2. 创建节点并初始化
    3. 实现节点功能
    4. 销毁节点并关闭接口
    '''
    rclpy.init(args=args) # 初始化rclpy
    node1 = ImageNode("rearview")  # 新建一个节点
    rclpy.spin(node1) # 保持节点运行，检测是否收到退出指令（Ctrl+C）

    rclpy.shutdown() # 关闭rclpy