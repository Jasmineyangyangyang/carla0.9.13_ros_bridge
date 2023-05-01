"""
这个节点可以从Bottom读CAN数据，
当有写数据操作时，转成将ROS 写给CAN
但是失败在： 开始写操作后，当写操作结束它自己不会跳回读操作
"""
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
from geometry_msgs.msg import Pose  #从Bottom实时机读出来的车辆位姿
from kvaser_msg_interfaces.msg import ControlCmd   #要写给Bottom实时机的是time, stangle 和 vehicle

# Create a dictionary of predefined CAN bitrates, using the name after
# "BITRATE_" as key. E.g. "500K".
bitrates = {x.name.replace("BITRATE_", ""): x for x in canlib.Bitrate}


# 定义 ROS2 节点类
class CanNode(Node):
    def __init__(self, name, channel, bitrate, sendinterval, senddb, receivedb):
        super().__init__(name) # 节点名称
        self.can_channel = channel # 指定使用的 CAN 通道号
        self.can_bitrate = bitrate  # 指定使用的 CAN 的比特率
        self.dbc_file_send = senddb # 发送数据的 dbc 文件
        self.dbc_file_receive = receivedb # 接收数据的 dbc 文件
        # 初始化 Kvaser CAN
        self.ch = canlib.openChannel(self.can_channel, canlib.Open.ACCEPT_VIRTUAL,bitrate=self.can_bitrate)
        self.ch.setBusOutputControl(canlib.canDRIVER_NORMAL)
        self.ch.busOn()

        # 加载 dbc 文件
        self.send_dbc = kvadblib.Dbc(filename=self.dbc_file_send)
        self.receive_dbc = kvadblib.Dbc(filename=self.dbc_file_receive)

        self.sendinterval = sendinterval
        self.new_control_callback = partial(self.control_callback,  db=self.send_dbc, ch=self.ch, interval=self.sendinterval)

        self.publisher_ = self.create_publisher(Pose, "/Bottom_pose", QoSProfile(depth=10)) # 创建发布者
        self.subscription_ = self.create_subscription(ControlCmd, "/ControlBottom", self.new_control_callback, QoSProfile(depth=10)) # 创建订阅者
        self.timer = self.create_timer(0.001, lambda:self.read_can_data(self.receive_dbc))


    # 订阅到消息后的回调函数: 将msg按照senddb解析出来，然后写到kvaser CAN
    def control_callback(self, msg, db, ch, interval):
        # print the data from subscription
        self.get_logger().info("Prepared for listening control command...")
        self.get_logger().info(f"I heard: {msg.time} s, \
                               stangle={msg.stangle} deg, vehiclevx={msg.vehiclevx} km/h" )
        try:
            self.ping_loop(msg, db, ch, interval)
        except Exception as e:
            print(f"Caught an exception: {e}")
    
    def ping_loop(self, controlmsg, db, ch, interval):
        print('----------------------------')
        print("Send signals from the following messages in order:")
        print(list(db))
        print('----------------------------')
        # 构造 CAN 数据帧
        while True:
            # Create an empty framebox each time, ignoring previously set signal values.
            framebox = kvadblib.FrameBox(db)
            # Add all messages to the framebox, and send all signals in order.
            for msg in db:
                framebox.add_message(msg.name)

            # Make a list of all signals (which framebox has found in all messages we gave it)
            signals = [bsig.signal for bsig in framebox.signals()]

            # Set each signal's value
            for sig in signals:
                value = self.get_sig_value(sig, controlmsg)  #解析ROS消息
                framebox.signal(sig.name).phys = value
            # Send all messages/frames
            for frame in framebox.frames():
                print('Sending frame', frame)
                bmsg = db.interpret(frame)
                msg = bmsg._message
                print('┏', msg.name)
                if msg.comment:
                    print('┃', f'"{msg.comment}"')
                for bsig in bmsg:
                    print('┃', bsig.name + ':', bsig.value, bsig.unit)

                ch.writeWait(frame, timeout=5000)

            time.sleep(interval)

    def get_sig_value(self, sig, controlmsg):
        """
        解析ROS 消息
        """
        if sig.name == 'Sttime' or sig.name == 'Sptime':
            value = controlmsg.time
        elif sig.name == 'StAngle':
            value = controlmsg.stangle
        elif sig.name == 'VehicleVx':
            value = controlmsg.vehiclevx
            
        limits = sig.limits
        value = float(np.clip(value, limits.min, limits.max))

        # round value depending on type...
        if sig.type is kvadblib.SignalType.UNSIGNED or sig.type is kvadblib.SignalType.SIGNED:
            # ...remove decimals if the signal was of type unsigned
            value = int(round(value))
        else:
            # ...otherwise, round to get only one decimal
            value = round(value, 4)

        return value
    
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
            data = {"Xb": None, "Yb": None, "Yaw": None}
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
                    if all(data.values()):   #检查所有键是否都有值
                        print(data)
                        break
            
            x = data["Xb"]
            y = data["Yb"]
            yaw = data["Yaw"]
            self.get_logger().info(f"x = {x} m, y={y} m, yaw={yaw} rad")
            # 构造 ROS2 消息
            ego_vehicle_transform = Pose()
            ego_vehicle_transform.position.x = x
            ego_vehicle_transform.position.y = y
            ego_vehicle_transform.position.z = 0.0
            roll = 0.0  # deg
            pitch = 0.0 # deg
            yaw = yaw
            quat = euler2quat(math.radians(roll), math.radians(pitch), yaw)  #将角度转成弧度
            ego_vehicle_transform.orientation.w = quat[0]
            ego_vehicle_transform.orientation.x = quat[1]
            ego_vehicle_transform.orientation.y = quat[2]
            ego_vehicle_transform.orientation.z = quat[3]

            self.publisher_.publish(ego_vehicle_transform) # 发布 ROS2 消息

        except KeyboardInterrupt:
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
        '--sendDB', default="/home/cec20/Yangjiaxin/carla-ros-bridge/src/ros-bridge/kvaser_parser_ros/kvaser_parser_ros/dbc/send_data.dbc", \
              help=("The database file to base messages on.")
    )
    parser.add_argument(
        '--receiveDB', default="/home/cec20/Yangjiaxin/carla-ros-bridge/src/ros-bridge/kvaser_parser_ros/kvaser_parser_ros/dbc/vehicle_example.dbc", \
            help=("The database file to base messages on.")
    )
    parser.add_argument(
        '--sendinterval', type=float, default=0.1, help=("The time, in seconds, between ticks.")
    )
    args = parser.parse_args()
    return args

def main(argv=None):
    args = parse_args(argv)
    bitrate=bitrates[args.bitrate.upper()]

    rclpy.init()
    node = CanNode("can_node", args.channel, bitrate, args.sendinterval, args.sendDB, args.receiveDB)
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()