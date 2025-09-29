from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    robot_controllers = os.path.join(
        get_package_share_directory('robot_description'),
        'config', 'diff_drive_controller.yaml'
    )

    joint_state_broadcaster_spawner = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['joint_state_broadcaster'],
    )

    diff_drive_base_controller_spawner = Node(
        package='controller_manager',
        executable='spawner',
        arguments=[
            'diff_drive_base_controller',
            '--param-file',
            robot_controllers,
            '--controller-ros-args',
            '-r /diff_drive_controller/cmd_vel:=/cmd_vel',
        ],
    )

    return LaunchDescription([
        joint_state_broadcaster_spawner,
        diff_drive_base_controller_spawner
    ])