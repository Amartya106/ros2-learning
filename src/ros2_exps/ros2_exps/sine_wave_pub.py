#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Float64
import math
import time


class SinePublisher(Node):
    def __init__(self):
        super().__init__("sine_publisher")

        self.sine_wave_pub_ = self.create_publisher(Float64, "sine_wave", 10)
        self.timer_ = self.create_timer(0.1, self.timer_callback)
        self.start_ = time.time()
        self.get_logger().info("Sine wave publisher has been started")
    
    def timer_callback(self):
        t = time.time() - self.start_

        msg = Float64()
        msg.data = math.sin(t)
        self.sine_wave_pub_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = SinePublisher()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()