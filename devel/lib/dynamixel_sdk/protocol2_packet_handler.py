#!/usr/bin/python3
# -*- coding: utf-8 -*-
# generated from catkin/cmake/template/script.py.in
# creates a relay to a python script source file, acting as that file.
# The purpose is that of a symlink
python_script = '/media/enrique/ae414e9e-3895-46c8-92d6-d4cb9803e8e8/enrique/Road-Lane-Detection-ROS-turtlebot3/src/DynamixelSDK/ros/dynamixel_sdk/src/dynamixel_sdk/protocol2_packet_handler.py'
with open(python_script, 'r') as fh:
    context = {
        '__builtins__': __builtins__,
        '__doc__': None,
        '__file__': python_script,
        '__name__': __name__,
        '__package__': None,
    }
    exec(compile(fh.read(), python_script, 'exec'), context)
