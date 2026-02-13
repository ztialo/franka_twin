from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    return LaunchDescription(
        [
            Node(
                package="franka_twin",
                executable="franka_joint_publisher",
                name="franka_joint_publisher",
                output="screen",
            ),
        ]
    )

