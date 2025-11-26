import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
    AppendEnvironmentVariable,
)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, TextSubstitution


ARGUMENTS = [
    DeclareLaunchArgument(
        "world",
        default_value=os.path.join(
            get_package_share_directory("robot_simulation"),
            "worlds",
            "empty.world",
        ),
        description="World file to load in Gazebo.",
    ),
    DeclareLaunchArgument(
        "verbosity",
        default_value="4",
        description="Gazebo verbosity level passed via -v flag.",
    ),
]


def generate_launch_description():
    pkg_share = get_package_share_directory("robot_simulation")
    models_path = os.path.join(pkg_share, "models")

    gz_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("ros_gz_sim"),
                "launch",
                "gz_sim.launch.py",
            )
        ),
        launch_arguments={
            "gz_args": [
                TextSubstitution(text="-r -v"),
                LaunchConfiguration("verbosity"),
                TextSubstitution(text=" "),
                LaunchConfiguration("world"),
            ]
        }.items(),
    )

    ld = LaunchDescription(ARGUMENTS)
    ld.add_action(AppendEnvironmentVariable("GZ_SIM_RESOURCE_PATH", models_path))
    ld.add_action(gz_launch)

    return ld
