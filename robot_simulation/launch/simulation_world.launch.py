import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.substitutions import FindPackageShare

PKG_SHARE = get_package_share_directory('robot_simulation')

DEFAULT_WORLD_PATH = os.path.join(PKG_SHARE, "worlds", "empty.world")
DEFAULT_MODELS_PATH = os.path.join(PKG_SHARE, "models")

def generate_launch_description():

    declare_world = DeclareLaunchArgument(
        'world',
        default_value=DEFAULT_WORLD_PATH,
        description='Absolute path to world file'
    )

    world = LaunchConfiguration('world')

    set_gz_path = SetEnvironmentVariable(
        name='GZ_SIM_RESOURCE_PATH',
        value=DEFAULT_MODELS_PATH
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py'
            )
        ]),
        launch_arguments={'gz_args': ['-r -v4 ', world]}.items()
    )

    return LaunchDescription([
        declare_world,
        set_gz_path,
        gazebo
    ])