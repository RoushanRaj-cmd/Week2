import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ObstacleAvoidanceNode(Node):
    def __init__(self):
        super().__init__('obstacle_avoidance_node')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscription = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.move_cmd = Twist()
        self.move_cmd.linear.x = 0.2  # Set constant velocity in x direction
        self.stop_distance = 0.1  # Distance to stop before the obstacle
        self.obstacle_distance = float('inf')

    def scan_callback(self, msg):
        self.obstacle_distance = min(msg.ranges)

    def timer_callback(self):
        if self.obstacle_distance > self.stop_distance:
            self.publisher_.publish(self.move_cmd)
        else:
            self.move_cmd.linear.x = 0.0  # Stop the robot
            self.publisher_.publish(self.move_cmd)

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoidanceNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
