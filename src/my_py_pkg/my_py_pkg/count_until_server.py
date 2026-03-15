#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, GoalResponse
from rclpy.action.server import ServerGoalHandle
from my_robot_interfaces.action import CountUntil 
import time

class CountUntilServerNode(Node):
    def __init__(self):
        super().__init__("count_until_server")
        self.count_until_server_ = ActionServer(
            self,
            CountUntil,
            "count_until",
            goal_callback=self.goal_callback,
            execute_callback=self.execute_callback
        )

        self.get_logger().info("Action server has been started")
    
    def goal_callback(self, goal_request: CountUntil.Goal):
        self.get_logger().info("Recieved a goal")

        if goal_request.target_number <=0:
            self.get_logger().warn("Rejecting the goal, target number must be greater than 0")
            return GoalResponse.REJECT
        
        self.get_logger().info("Accepting the goal")
        return GoalResponse.ACCEPT
    
    def execute_callback(self, goal_handle: ServerGoalHandle):
        target_number = goal_handle.request.target_number
        delay = goal_handle.request.delay
        result = CountUntil.Result()
        feedback = CountUntil.Feedback()
        counter = 0

        for i in range(target_number):
            counter +=1
            self.get_logger().info(str(counter))
            feedback.current_number = counter
            goal_handle.publish_feedback(feedback)
            time.sleep(delay)


        goal_handle.succeed()
        result.reached_number = counter
        return result



def main(args=None):
    rclpy.init(args=args)
    node = CountUntilServerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()