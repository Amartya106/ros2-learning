#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen
from my_robot_interfaces.srv import TurtleActivation


class ChallengeNode(Node):
    def __init__(self):

        super().__init__("Challenge_Node")
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.pose_sub_ = self.create_subscription(Pose, "/turtle1/pose", self.callback_sub, 10)
        self.turtle_activation_service_ = self.create_service(TurtleActivation, "turtle_activation", self.callback_turtle_activation)
        self.turtle_active_ = True
        

    def callback_sub(self, pose:Pose):

        if self.turtle_active_:

            cmd = Twist()

            if pose.x < 5.5:
                cmd.linear.x = 1.0
                cmd.angular.z = 1.0

            elif pose.x >=5.5:
                cmd.linear.x = 2.0
                cmd.angular.z = 2.0
            
            self.cmd_vel_pub_.publish(cmd)


    def callback_turtle_activation(self, request: TurtleActivation.Request, response: TurtleActivation.Response):
        self.turtle_active_ = request.active_state
        response.message = f"Active status: {self.turtle_active_}"
        return response



def main(args=None):
    rclpy.init(args=args)
    node = ChallengeNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()