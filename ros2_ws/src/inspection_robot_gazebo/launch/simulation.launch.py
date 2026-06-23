from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    desc_pkg = get_package_share_directory('my_assembly_description')
    gazebo_pkg = get_package_share_directory('inspection_robot_gazebo')

    xacro_file = os.path.join(desc_pkg, 'urdf', 'my_assembly.xacro')
    world_file = os.path.join(gazebo_pkg, 'worlds', 'empty.sdf')

    robot_description = {
        'robot_description': Command(['xacro ', xacro_file])
    }

    return LaunchDescription([

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[robot_description],
            output='screen'
        ),

        ExecuteProcess(
            cmd=['gz', 'sim', '-r', world_file],
            output='screen'
        ),

        Node(
       	    package='ros_gz_sim',
            executable='create',
            arguments=[
       	        '-file',
                os.path.join(desc_pkg, 'urdf', 'my_assembly.urdf'),
                '-name',
                'inspection_robot',
                '-z',
                '0.25'
        ],
        output='screen'
    ) 
    ])
