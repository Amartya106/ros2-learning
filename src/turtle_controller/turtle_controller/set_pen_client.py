#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.srv import SetPen
from turtlesim.msg import Pose

class SetPenClient(Node):
    def __init__(self):
        super().__init__("set_pen_client")
        self.set_pen_client_ = self.create_client(SetPen, "/turtle1/set_pen")
        self.pose_sub = self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)
        self.zone = "green"

    def pose_callback(self, pose:Pose):
        prev_zone = self.zone

        if pose.x <5.5:
            self.zone = "green"
        elif pose.x>=5.5:
            self.zone = "red"
        
        if prev_zone != self.zone:
            self.call_set_pen()
    

    def call_set_pen(self):
        while not self.set_pen_client_.wait_for_service(1.0):
            self.get_logger().warn("Waiting for server....")

        request = SetPen.Request()

        if self.zone == "green":
            request.r = 0
            request.b = 0
            request.g = 255
        
        elif self.zone == "red":
            request.r = 255
            request.b = 0
            request.g = 0
        
        self.set_pen_client_.call_async(request)
        self.get_logger().info(f"Color changed to {self.zone}")

def main(args=None):
    rclpy.init(args=args)
    node = SetPenClient()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()