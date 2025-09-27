from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

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

    return LaunchDescription([
        sim_world,
        robot_description_launch,
        spawn_robot
    ])