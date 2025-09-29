import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

PKG_NAME = "robot_description"
PKG_SHARE = get_package_share_directory(PKG_NAME)

DEFAULT_MODEL_PATH = os.path.join(PKG_SHARE, "urdf", "robot.urdf.xacro")
DEFAULT_CONFIG_PATH = os.path.join(PKG_SHARE, "config", "robot_components.yaml")
DEFAULT_JSP_GUI = "false"
DEFAULT_USE_SIM_TIME = "true"

def generate_launch_description():

    declare_jsp_gui = DeclareLaunchArgument(
        'jsp_gui', default_value=DEFAULT_JSP_GUI, choices=['true', 'false'],
        description='Run joint_state_publisher GUI'
    )
    declare_use_sim_time = DeclareLaunchArgument(
        'use_sim_time', default_value=DEFAULT_USE_SIM_TIME, choices=['true', 'false'],
        description='Use simulated time'
    )

    declare_entity_name = DeclareLaunchArgument(
        'entity_name', default_value='boxes',
        description='Entity name in Gazebo'
    )
    declare_x = DeclareLaunchArgument('x', default_value='0.0', description='Spawn X position')
    declare_y = DeclareLaunchArgument('y', default_value='0.0', description='Spawn Y position')
    declare_z = DeclareLaunchArgument('z', default_value='0.0', description='Spawn Z position')

    jsp_gui = LaunchConfiguration('jsp_gui')
    use_sim_time = LaunchConfiguration('use_sim_time')
    entity_name = LaunchConfiguration('entity_name')
    x = LaunchConfiguration('x')
    y = LaunchConfiguration('y')
    z = LaunchConfiguration('z')

    robot_description_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('robot_description'), 'launch', 'robot_description.launch.py'
            ])
        ]),
        launch_arguments={
            'jsp_gui': jsp_gui,
            'use_sim_time': use_sim_time,
            'simulation' : 'true'
        }.items()
    )

    gz_spawn_entity = Node(
        package='ros_gz_sim',
        executable='create',
        output='screen',
        arguments=[
            '-topic', 'robot_description',
            '-name', entity_name,
            '-allow_renaming', 'true',
            '-x', x, '-y', y, '-z', z
        ]
    )

    return LaunchDescription([
        declare_jsp_gui,
        declare_use_sim_time,
        declare_entity_name,
        declare_x,
        declare_y,
        declare_z,
        robot_description_launch,
        gz_spawn_entity
    ])
