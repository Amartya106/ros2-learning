#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import HardwareStatus


class CustomPub(Node):
    def __init__(self):
        super().__init__("custom_pub")
        self.custom_pub_ = self.create_publisher(HardwareStatus, "test", 10)
        self.my_timer_ = self.create_timer(1, self.test)
        self.get_logger().info("Publisher has been started")


    def test(self):
        msg = HardwareStatus()
        msg.temperature = 34.5
        self.custom_pub_.publish(msg)



def main(args=None):
    rclpy.init(args=args)
    node = CustomPub()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()