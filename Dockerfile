ARG ROS_DISTRO=jazzy
FROM osrf/ros:${ROS_DISTRO}-desktop-full

ENV DEBIAN_FRONTEND=noninteractive
ENV ROS_DISTRO=${ROS_DISTRO}

ARG BRANCH=turtlebot3_burger

RUN rosdep init || true && rosdep update

WORKDIR /robot_simulation_ws/src

COPY robot_simulation/package.xml robot_simulation/

RUN mkdir robot_description && \
    curl -fSL \
      https://raw.githubusercontent.com/vladislav-parkhachev/robot_description_template/${BRANCH}/robot_description/package.xml \
      -o robot_description/package.xml

WORKDIR /robot_simulation_ws

RUN . /opt/ros/${ROS_DISTRO}/setup.sh && \
    apt-get update && \
    rosdep install --from-paths src --ignore-src -r -y

WORKDIR /robot_simulation_ws/src

COPY robot_simulation robot_simulation

WORKDIR /robot_simulation_ws

RUN . /opt/ros/${ROS_DISTRO}/setup.sh && colcon build --packages-select robot_simulation

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

SHELL ["/bin/bash", "-c"]

ENTRYPOINT ["/entrypoint.sh"]

CMD ["ros2", "launch", "robot_simulation", "bringup_simulation.launch.py"]