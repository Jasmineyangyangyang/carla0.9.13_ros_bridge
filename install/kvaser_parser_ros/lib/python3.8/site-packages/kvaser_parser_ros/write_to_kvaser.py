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

import queue
import threading

# 导入消息类型
from geometry_msgs.msg import Pose  #从Bottom实时机读出来的车辆位姿
from kvaser_msg_interfaces.msg import ControlCmd   #要写给Bottom实时机的是time, stangle 和 vehicle

# Create a dictionary of predefined CAN bitrates, using the name after
# "BITRATE_" as key. E.g. "500K".
bitrates = {x.name.replace("BITRATE_", ""): x for x in canlib.Bitrate}


# 定义 ROS2 节点类
class CanNode(Node):
    def __init__(self, name, channel, bitrate, sendinterval, senddb):
        super().__init__(name) # 节点名称
        self.can_channel = channel # 指定使用的 CAN 通道号
        self.can_bitrate = bitrate  # 指定使用的 CAN 的比特率
        self.dbc_file_send = senddb # 发送数据的 dbc 文件

        # 初始化 Kvaser CAN
        self.ch = canlib.openChannel(self.can_channel, canlib.Open.ACCEPT_VIRTUAL,bitrate=self.can_bitrate)
        self.ch.setBusOutputControl(canlib.canDRIVER_NORMAL)
        self.ch.busOn()

        # 加载 dbc 文件
        self.send_dbc = kvadblib.Dbc(filename=self.dbc_file_send)

        self.sendinterval = sendinterval
        # self.new_control_callback = partial(self.control_callback,  db=self.send_dbc, ch=self.ch, interval=self.sendinterval)

        self.subscription_ = self.create_subscription(ControlCmd, "/ControlBottom", self.control_callback, QoSProfile(depth=10)) # 创建订阅者,假设规控发送指令按120Hz

        # 创建序列用来接收控制信号
        self.control_queue = queue.Queue(maxsize=20000)
        # self.control_queue_lock = threading.Lock()
        # 为写入CAN创建单独的线程
        self.can_thread = threading.Thread(target=self.ping_loop, args=(self.send_dbc, self.ch, self.sendinterval))
        self.can_thread.start()

    # 订阅到消息后的回调函数: 将msg按照senddb解析出来，然后写到kvaser CAN
    def control_callback(self, msg):
        # print the data from subscription
        self.get_logger().info("Prepared for listening control command...")
        self.get_logger().info(f"I heard: {msg.time} s, \
                               stangle={msg.stangle} deg, vehiclevx={msg.vehiclevx} km/h" )
        self.control_queue.put(msg)   #查阅资料：queue中已设置了锁来处理资源调度问题，不需要手动添加
        # self.control_queue_lock.acquire()
        
        # try:
        #     self.control_queue.put(msg)
        #     # self.ping_loop(msg, db, ch, interval)
        # except Exception as e:
        #     print(f"Caught an exception: {e}")
        # finally:
        #     self.control_queue_lock.release()
    
    def ping_loop(self, db, ch, interval):
        print('----------------------------')
        print("Send signals from the following messages in order:")
        print(list(db))
        print('----------------------------')
        # 构造 CAN 数据帧
        while rclpy.ok():
            # Create an empty framebox each time, ignoring previously set signal values.
            framebox = kvadblib.FrameBox(db)
            # Add all messages to the framebox, and send all signals in order.
            for msg in db:
                framebox.add_message(msg.name)

            # Make a list of all signals (which framebox has found in all messages we gave it)
            signals = [bsig.signal for bsig in framebox.signals()]

            # Set each signal's value
            # with self.control_queue_lock:   # 使用with语句可以实现自动获取和释放锁
            controlmsg = self.control_queue.get()
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
    
    def __del__(self):
        self.ch.busOff()
        self.ch.close()
        self.can_thread.join()  #确保线程结束后再关闭节点



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
        '--sendinterval', type=float, default=1.0/120.0, help=("The time, in seconds, between ticks.")
    )
    args = parser.parse_args()
    return args

def main(argv=None):
    args = parse_args(argv)
    bitrate=bitrates[args.bitrate.upper()]

    rclpy.init()
    node = CanNode("write_to_can_node", args.channel, bitrate, args.sendinterval, args.sendDB)
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()