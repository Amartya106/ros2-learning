#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import math
import time
from geometry_msgs.msg import Twist


class SineTurtle(Node):
    def __init__(self):
        super().__init__("sine_turtle")

        self.sine_wave_gen_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.timer_ = self.create_timer(0.1, self.timer_callback)
        self.start_ = time.time()
        self.get_logger().info("Sine wave turtle has started")
    
    def timer_callback(self):
        t = time.time() - self.start_
        move = Twist()
        move.linear.x = 2.0
        move.angular.z = 2*math.sin(t)
        self.sine_wave_gen_.publish(move)

def main(args=None):
    rclpy.init(args=args)
    node = SineTurtle()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()