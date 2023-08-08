# Use the official image as a parent image
FROM ubuntu:20.04

# Set the working directory in the container
WORKDIR /app

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary tools
RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    lsb-release

# Add ROS Noetic setup script to sources.list
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

# Add ROS public key
RUN curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add -

# Update system
RUN apt-get update

# Install ROS Noetic
RUN apt-get install -y ros-noetic-desktop-full

# Set ROS environment variables in .bashrc
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc

# Install python tools and dependencies
RUN apt-get install -y python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential

# Initialize rosdep
RUN rosdep init

# Update rosdep
RUN rosdep update

# Pytohn3 install
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install numpy pandas opencv-python rosbag-pandas

# Set the default command for the container
CMD ["bash"]