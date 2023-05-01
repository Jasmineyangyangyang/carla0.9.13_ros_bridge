import launch
import launch_ros.actions

def generate_launch_description():
    ld = launch.LaunchDescription([
        launch_ros.actions.Node(
            package='imagenode',
            executable='cameranode1',
            name='carla_ros_bridge',
            output='screen',
            emulate_tty='True',
            on_exit=launch.actions.Shutdown(),
        )
    ])
    return ld

if __name__ == '__main__':
    generate_launch_description()