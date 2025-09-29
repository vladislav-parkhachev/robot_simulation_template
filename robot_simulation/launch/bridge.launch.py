from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    bridge_params = os.path.join(
        get_package_share_directory('robot_simulation'),
        'config', 'bridge_parameters.yaml'
    )

    bridge_node = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['--ros-args', '-p', f'config_file:={bridge_params}']
    )

    return LaunchDescription([bridge_node])
