import numpy as np
from transforms3d.euler import euler2quat
import math
import time
import argparse
from functools import partial

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile   #QoSProfile是ROS2中的一个类，用于设置节点之间的通信质量, 它包含了一些参数（历史消息数量，保留时间，延迟等）
from canlib import canlib, Frame, kvadblib

# 导入消息类型
from geometry_msgs.msg import Pose, PoseStamped  #从Bottom实时机读出来的车辆位姿
from kvaser_msg_interfaces.msg import ControlCmd   #要写给Bottom实时机的是time, stangle 和 vehicle
from nav_msgs.msg import Path

# Create a dictionary of predefined CAN bitrates, using the name after
# "BITRATE_" as key. E.g. "500K".
bitrates = {x.name.replace("BITRATE_", ""): x for x in canlib.Bitrate}

# xfile1=open("/home/cec20/zhang/Natural_road_code/Centerroad_x.txt")
# data1=xfile1.read()
# centerroad_x=data1.split(",")
# del centerroad_x[len(centerroad_x)-1]
# xfile1.close()

# xfile2=open("/home/cec20/zhang/Natural_road_code/Centerroad_y.txt")
# data1=xfile2.read()
# centerroad_y=data1.split(",")
# del centerroad_y[len(centerroad_y)-1]
# xfile2.close()

# Init_dis=float(80/5)
# Ref_len=0
# for i in range(0,len(centerroad_x)-1):
#     x1=float(centerroad_x[i])
#     x2=float(centerroad_x[i+1])
#     y1=float(centerroad_y[i])
#     y2=float(centerroad_y[i+1])    
#     dis=math.sqrt((x2-x1)**2+(y2-y1)**2)
#     Ref_len=Ref_len+dis

           
# FreX=[]
# Tra_X=[]
# Tra_Y=[]
# FreX.append(Init_dis)

# def Frenet2Cartesian(frex):
#     if frex>Ref_len:
#         frex=frex-Ref_len
#     dis1=0
#     for idx1 in range(0,len(centerroad_x)-1):
#         idx2=idx1+1
#         x1=float(centerroad_x[idx1])
#         x2=float(centerroad_x[idx2])
#         y1=float(centerroad_y[idx1])
#         y2=float(centerroad_y[idx2])    
#         dis=math.sqrt((x2-x1)**2+(y2-y1)**2)
#         if frex<dis1+dis:
#             Lane_yaw=math.atan2((y2-y1),(x2-x1))
#             cartesian_x=x1+(frex-dis1)*math.cos(Lane_yaw)-2*math.sin(Lane_yaw)
#             cartesian_y=y1+(frex-dis1)*math.sin(Lane_yaw)+2*math.cos(Lane_yaw)
#             Tra_X.append(round(cartesian_x,4))
#             Tra_Y.append(round(cartesian_y,4))
#             break
#         dis1+=dis

# def Cal_yaw():
#     if len(Tra_X)>2:
#         yaw=math.atan2((float(Tra_Y[-1])-float(Tra_Y[-2])),(float(Tra_X[-1])-float(Tra_X[-2])))
#     else:
#         yaw=1.5708
#     return yaw


# 定义 ROS2 节点类
class CanNode(Node):
    def __init__(self, name, channel, bitrate, receivedb):
        super().__init__(name) # 节点名称
        self.can_channel = channel # 指定使用的 CAN 通道号
        self.can_bitrate = bitrate  # 指定使用的 CAN 的比特率
        self.dbc_file_receive = receivedb # 接收数据的 dbc 文件
        # 初始化 Kvaser CAN
        self.ch = canlib.openChannel(self.can_channel, canlib.Open.ACCEPT_VIRTUAL,bitrate=self.can_bitrate)
        self.ch.setBusOutputControl(canlib.canDRIVER_NORMAL)
        self.ch.busOn()

        # 加载 dbc 文件
        self.receive_dbc = kvadblib.Dbc(filename=self.dbc_file_receive)

        # self.publisher_ = self.create_publisher(Pose, "/Bottom_pose", QoSProfile(depth=10)) # 创建发布者
        
        self.publisher_ = self.create_publisher(Path, "/carla/ego_vehicle/control/set_transform", QoSProfile(depth=10))
        # self.publisher_adjacent = self.create_publisher(Pose, "/carla/adjacent_vehicle/control/set_transform", QoSProfile(depth=10))
        self.timer = self.create_timer(1.0/60.0, lambda:self.read_can_data(self.receive_dbc))
    
    def printframe(self, db, frame, data):
        try:
            bmsg = db.interpret(frame)
        except kvadblib.KvdNoMessage:
            print(f"<<< No message found for frame with id {frame.id} >>>")
            return

        if not bmsg._message.dlc == bmsg._frame.dlc:
            print(
                "<<< Could not interpret message because DLC does not match for"
                f" frame with id {frame.id} >>>"
            )
            print(f"\t- DLC (database): {bmsg._message.dlc}")
            print(f"\t- DLC (received frame): {bmsg._frame.dlc}")
            return

        msg = bmsg._message
        
        if msg.name == "VehicleXb":
            for bsig in bmsg:
                if bsig.name == "Xb":
                    data['Xb'] = float(bsig.value)
        elif msg.name == "VehicleYb":
            for bsig in bmsg:
                if bsig.name == "Yb":
                    data["Yb"] = float(bsig.value)
        elif msg.name == "VehicleYaw":
            for bsig in bmsg:
                if bsig.name == "Yaw":
                    data["Yaw"] = float(bsig.value)
        elif msg.name == "AdjacentVehicleXb":
            for bsig in bmsg:
                if bsig.name == "AdjacentXb":
                    data["AdjacentXb"] = float(bsig.value)
        elif msg.name == "AdjacentVehicleYb":
            for bsig in bmsg:
                if bsig.name == "AdjacentYb":
                    data["AdjacentYb"] = float(bsig.value)
        elif msg.name == "AdjacentVehicleYaw":
            for bsig in bmsg:
                if bsig.name == "AdjacentYaw":
                    data["AdjacentYaw"] = float(bsig.value)
        # print('┏', msg.name)

        # if msg.comment:
        #     print('┃', f'"{msg.comment}"')

        # for bsig in bmsg:
        #     print('┃', bsig.name + ':', bsig.value, bsig.unit)

        # print('┗')
        return data
    
    # 循环读取 CAN 数据并发布 ROS2 消息
    def read_can_data(self, db):
        try:
            data = {"Xb": None, "Yb": None, "Yaw": None, "AdjacentXb": None,"AdjacentYb": None,"AdjacentYaw": None} 
            print("Listening...")
            # 解析 CAN 帧数据
            while True:
                frame = self.ch.read(timeout=100) # 从 CAN 通道读取数据，设置超时时间为 100 毫秒
                send_id_list = [100, 101]  # 这是发数据占用的id， 要过滤掉，以免读到发过去的数据
                if frame.id in send_id_list:
                    print(f"<<< You are sending frame with id {frame.id}, please waite... >>>")
                    continue
                else: 
                    data = self.printframe(db, frame, data)
                    # print(data)
                    no_None_flag = True        #检查所有键是否都有值(0也可以),而不是None
                    for value_ in data.values():
                        if value_ is None:
                            no_None_flag = False
                    if no_None_flag:
                        break

                    # if all(data.values()):   #检查所有键是否都有值
                    #     print(data)
                    #     break
            
            x = data["Xb"]
            y = data["Yb"]
            yaw = data["Yaw"]
            self.get_logger().info(f"x = {x} m, y={y} m, yaw={yaw} rad")

            adjacent_x = data["AdjacentXb"]
            adjacent_y = data["AdjacentYb"]
            adjacent_yaw = data["AdjacentYaw"]
            self.get_logger().info(f"adjacent_x = {adjacent_x} m, adjacent_y={adjacent_y} m, adjacent_yaw={adjacent_yaw} rad")
            # 构造 ROS2 消息
            msg = Path()
            msg.header.frame_id = "vehicle"
            msg.header.stamp = self.get_clock().now().to_msg()
            ego_vehicle_transform = PoseStamped()
            ego_vehicle_transform.header.frame_id = "ego_vehicle"
            ego_vehicle_transform.header.stamp = msg.header.stamp
            ego_vehicle_transform.pose.position.x = x
            ego_vehicle_transform.pose.position.y = y
            ego_vehicle_transform.pose.position.z = 0.0
            roll = 0.0  # deg
            pitch = 0.0 # deg
            yaw = yaw
            quat = euler2quat(math.radians(roll), math.radians(pitch), yaw)  #将角度转成弧度
            ego_vehicle_transform.pose.orientation.w = quat[0]
            ego_vehicle_transform.pose.orientation.x = quat[1]
            ego_vehicle_transform.pose.orientation.y = quat[2]
            ego_vehicle_transform.pose.orientation.z = quat[3]
            adjacent_vehicle_transform = PoseStamped()
            adjacent_vehicle_transform.header.frame_id = "adjacent_vehicle"
            adjacent_vehicle_transform.header.stamp = msg.header.stamp            
            adjacent_vehicle_transform.pose.position.x = adjacent_x
            adjacent_vehicle_transform.pose.position.y = adjacent_y
            adjacent_vehicle_transform.pose.position.z = 0.0
            quat = euler2quat(0.0, 0.0, adjacent_yaw)  #将角度转成弧度
            adjacent_vehicle_transform.pose.orientation.w = quat[0]
            adjacent_vehicle_transform.pose.orientation.x = quat[1]
            adjacent_vehicle_transform.pose.orientation.y = quat[2]
            adjacent_vehicle_transform.pose.orientation.z = quat[3]
            msg.poses.append(ego_vehicle_transform)
            msg.poses.append(adjacent_vehicle_transform)
            self.publisher_.publish(msg) # 发布 ROS2 消息
            # self.publisher_adjacent.publish(adjacent_vehicle_transform) 

        except KeyboardInterrupt:
            self.ch.busOff()
            self.ch.close()
            print("Stop.")    




def parse_args(argv):
    parser = argparse.ArgumentParser(
        description="Send and receive CAN message based on different database.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        'channel', type=int, default=0, nargs='?', help=("The channel to send messages on.")
    )
    parser.add_argument(
        '--bitrate', '-b', default='500k', help=("Bitrate, one of " + ', '.join(bitrates.keys()))
    )
    parser.add_argument(
        '--receiveDB', default="/home/cec20/Yangjiaxin/my-carla-ros-bridge/src/kvaser_parser_ros/kvaser_parser_ros/dbc/vehicle_example_adjacent.dbc", \
            help=("The database file to base messages on.")
    )

    args = parser.parse_args()
    return args

def main(argv=None):
    args = parse_args(argv)
    bitrate=bitrates[args.bitrate.upper()]

    rclpy.init()
    node = CanNode("read_from_can_node", args.channel, bitrate, args.receiveDB)
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()