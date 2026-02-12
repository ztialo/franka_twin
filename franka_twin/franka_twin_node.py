import rclpy
from rclpy.node import Node


class FrankaTwinNode(Node):
    def __init__(self) -> None:
        super().__init__("franka_twin_node")
        self.get_logger().info("franka_twin_node started")


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

