import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from math import sqrt

class MoveToGoalNode(Node):
    def __init__(self):
        super().__init__('move_to_goal_node')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscription = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.move_cmd = Twist()
        self.move_cmd.linear.x = 0.2  # Setting constant velocity in x direction
        self.goal_distance = 1.0  # Distance to the goal point in meters
        self.current_distance = 0.0

    def odom_callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        self.current_distance = sqrt(x**2 + y**2)

    def timer_callback(self):
        if self.current_distance < self.goal_distance:
            self.publisher_.publish(self.move_cmd)
        else:
            self.move_cmd.linear.x = 0.0  # Stopping the robot
            self.publisher_.publish(self.move_cmd)

def main(args=None):
    rclpy.init(args=args)
    node = MoveToGoalNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
