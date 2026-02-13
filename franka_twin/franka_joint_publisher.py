import rclpy
from rclpy.node import Node
from franky import Affine, CartesianMotion, Robot, ReferenceType, Gripper, RelativeDynamicsFactor
from sensor_msgs.msg import JointState
import numpy as np

ROBOT_IP = "192.168.137.2"

franka_joint_names = ["fr3_joint1","fr3_joint2","fr3_joint3","fr3_joint4","fr3_joint5","fr3_joint6","fr3_joint7","fr3_finger_joint1","fr3_finger_joint2"]

class FrankaTwinNode(Node):
    def __init__(self) -> None:
        super().__init__("franka_twin_node")
        
        # Connect to real world franka arm
        self.real_franka = Robot(ROBOT_IP)
        self.real_franka.recover_from_errors()

        self.joint_pub = self.create_publisher(JointState, "/joint_command_fr3", 10)
        self.timer = self.create_timer(0.05, self.publish_joint_commands)  # 20 Hz

    def publish_joint_commands(self):
        # get current joint positions from real franka
        joint_pos = self.real_franka.current_joint_positions
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()

        msg.name = franka_joint_names
        msg.position = joint_pos.flatten().tolist() + [0.04, 0.04]  # Append gripper positions
        self.joint_pub.publish(msg)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = FrankaTwinNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

