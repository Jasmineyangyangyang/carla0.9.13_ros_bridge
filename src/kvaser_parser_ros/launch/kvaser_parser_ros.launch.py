"""
这个launch文件没有正确运行，因为缺少对节点中参数的赋值
运行时会报错 “--ros-args *** was required: shutting down launched system”
"""
from launch_ros.actions import Node
import launch

def generate_launch_description():
    ld = launch.LaunchDescription([
        Node(
            package='kvaser_parser_ros',
            executable='write_to_kvaser',
            output='screen',
            emulate_tty='True',
            on_exit=launch.actions.Shutdown(),
        ),
        Node(
            package='kvaser_parser_ros',
            executable='read_from_kvaser',
            output='screen',
            emulate_tty='True',
            on_exit=launch.actions.Shutdown(),
        )

    ])
    return ld

if __name__ == '__main__':
    generate_launch_description()