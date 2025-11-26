ARG ROS_DISTRO=jazzy
FROM osrf/ros:${ROS_DISTRO}-desktop-full

RUN apt-get update

WORKDIR /robot_simulation_ws/src

COPY robot_simulation/robot_simulation/package.xml robot_simulation/
COPY robot_description/robot_description/package.xml robot_description/

WORKDIR /robot_simulation_ws

RUN rosdep install --from-paths src --ignore-src -r -y

WORKDIR /robot_simulation_ws/src

COPY robot_simulation/robot_simulation robot_simulation
COPY robot_description/robot_description robot_description

WORKDIR /robot_simulation_ws

RUN . /opt/ros/${ROS_DISTRO}/setup.sh && \
    colcon build --symlink-install

ENV PROMPT_COMMAND="source /opt/ros/${ROS_DISTRO}/setup.bash"
CMD ["bash"]

