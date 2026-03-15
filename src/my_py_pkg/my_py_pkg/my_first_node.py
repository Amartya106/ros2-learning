#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class myNode(Node):
    def __init__(self):
        super().__init__('my_first_node')
        self.counter_ = 0
        self.timer_ = self.create_timer(1, self.print_string)
    
    def print_string(self):
        self.get_logger().info(f"I am {self.counter_}")
        self.counter_ +=1

def main(args = None):
    rclpy.init(args=args)
    node = myNode()
    rclpy.spin(node)
    rclpy.shutdown() 

if __name__ == '__main__':
    main()
