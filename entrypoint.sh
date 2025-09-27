#!/bin/bash
set -e

source /opt/ros/${ROS_DISTRO}/setup.bash

if [ -d "/robot_simulation_ws/src/robot_description" ]; then
  cd /robot_simulation_ws
  colcon build --symlink-install --packages-select robot_description
  source install/setup.bash
fi

exec "$@"