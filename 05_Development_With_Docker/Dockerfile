FROM ros_with_python_files AS base
WORKDIR catkin_ws/
SHELL ["/bin/bash", "-c"]
USER root
RUN catkin clean --yes && catkin config --install --extend /opt/ros/noetic && catkin build
FROM ubuntu:latest
COPY --from=base catkin_ws/build ./

