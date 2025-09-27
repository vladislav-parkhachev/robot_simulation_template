ARG ROS_DISTRO=jazzy
FROM osrf/ros:${ROS_DISTRO}-desktop-full

ENV DEBIAN_FRONTEND=noninteractive
ENV ROS_DISTRO=${ROS_DISTRO}

RUN rosdep init || true && rosdep update

WORKDIR /robot_simulation_ws/src

COPY robot_simulation/package.xml robot_simulation/

WORKDIR /robot_simulation_ws

RUN . /opt/ros/${ROS_DISTRO}/setup.sh && \
    apt-get update && \
    rosdep install --from-paths src --ignore-src -r -y

WORKDIR /robot_simulation_ws/src

COPY robot_simulation robot_simulation

WORKDIR /robot_simulation_ws

RUN . /opt/ros/${ROS_DISTRO}/setup.sh && colcon build

SHELL ["/bin/bash", "-c"]

ENTRYPOINT ["/bin/bash", "-c", "source /opt/ros/${ROS_DISTRO}/setup.bash && source /robot_simulation_ws/install/setup.bash && exec \"$@\"", "--"]

CMD ["ros2", "launch", "robot_simulation", "simulation_world.launch.py"]