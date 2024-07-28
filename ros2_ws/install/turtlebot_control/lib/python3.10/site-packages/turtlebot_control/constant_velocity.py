import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class ConstantVelocityNode(Node):
    def __init__(self):
        super().__init__('constant_velocity_node')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.move_cmd = Twist()
        self.move_cmd.linear.x = 0.2  # Setting constant velocity in x direction

    def timer_callback(self):
        self.publisher_.publish(self.move_cmd)

def main(args=None):
    rclpy.init(args=args)
    node = ConstantVelocityNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
