from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

def generate_launch_description():

    sim_world = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('robot_simulation'), 'launch', 'simulation_world.launch.py'
            ])
        ])
    )

    robot_description_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('robot_description'), 'launch', 'robot_description.launch.py'
            ])
        ])
    )

    spawn_robot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('robot_simulation'), 'launch', 'spawn_robot.launch.py'
            ])
        ])
    )

    controllers_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('robot_simulation'), 'launch', 'controllers.launch.py'
            ])
        ])
    )

    bridge_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('robot_simulation'), 'launch', 'bridge.launch.py'
            ])
        ])
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )

    return LaunchDescription([
        sim_world,
        robot_description_launch,
        spawn_robot,
        controllers_launch,   
        bridge_launch,
        rviz_node        
    ])
