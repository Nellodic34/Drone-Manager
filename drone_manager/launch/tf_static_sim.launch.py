import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node, SetParameter
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():


    return LaunchDescription([
        # Node(
        #     package='tf2_ros', executable='static_transform_publisher', output='screen',
        #     arguments=['0', '0', '0', '0.7071068', '0.7071068', '0.0', '0.0', 'odom', 'odomNED']),

        # Node(
        #     package='tf2_ros', executable='static_transform_publisher', output='screen',
        #     arguments=['0', '0', ' 0', '0', '0', '3.14159265359', 'base_link_FRD', 'base_link']),  # ZYX
        # # OAk-D Lite
        # Node(
        #     package='tf2_ros', executable='static_transform_publisher', output='screen',
        #     arguments=['0.15', '0.03', '0.0', '-1.5707','0', '-1.5707', 'base_link', 'x500_depth_0/OakD-Lite/base_link/StereoOV7251']),
        # Node(
        #     package='tf2_ros', executable='static_transform_publisher', output='screen',
        #     arguments=['0.15', '0.03', '0.0',  '-1.5707', '0', '-1.5707', 'base_link', 'x500_depth_0/OakD-Lite/base_link/IMX214']),
        # Node(
        #     package='tf2_ros', executable='static_transform_publisher', output='screen',
        #     arguments=['0.15', '0.03', '0.0', '-1.5707','0', '-1.5707', 'odom', 'odom/x500_depth_0/OakD-Lite/base_link/StereoOV7251']),
        # Node(
        #     package='tf2_ros', executable='static_transform_publisher', output='screen',
        #     arguments=['0.15', '0.03', '0.0',  '-1.5707', '0', '-1.5707', 'odom', 'odom/x500_depth_0/OakD-Lite/base_link/IMX214']),

        Node(
            package='tf2_ros', executable='static_transform_publisher', output='screen',
            arguments=['1.5', '1.0', '1.85', '0', '0', '0', 'map', 'goal1']),
        Node(
            package='tf2_ros', executable='static_transform_publisher', output='screen',
            arguments=['9.5', '1.0', '1.85', '0', '0', '0', 'map', 'goal2']),

        Node(
            package='tf2_ros', executable='static_transform_publisher', output='screen',
            arguments=['15.5', '2.0', '1.85', '0', '0', '0', 'map', 'goal3']),

        Node(
            package='tf2_ros', executable='static_transform_publisher', output='screen',
            arguments=['17.5', '4.0', '1.85', '0', '0', '0', 'map', 'goal4']),
        
        Node(
            package='tf2_ros', executable='static_transform_publisher', output='screen',
            arguments=['9.5', '4.0', '1.85', '0', '0', '0', 'map', 'goal5']),

        Node(
            package='tf2_ros', executable='static_transform_publisher', output='screen',
            arguments=['1.5', '4.0', '1.85', '0', '0', '0', 'map', 'goal6']),   

        Node(
            package='tf2_ros', executable='static_transform_publisher', output='screen',
            arguments=['1.5', '7.0', '1.85', '0', '0', '0', 'map', 'goal7']),

        Node(
            package='tf2_ros', executable='static_transform_publisher', output='screen',
            arguments=['9.5', '6.95', '1.85', '0', '0', '0', 'map', 'goal8']),

        Node(
            package='tf2_ros', executable='static_transform_publisher', output='screen',
            arguments=['15.5', '6.7', '1.85', '0', '0', '0', 'map', 'goal9']),
            
    ])

