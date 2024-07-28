import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys, select, termios, tty

class KeyboardControlNode(Node):
    def __init__(self):
        super().__init__('keyboard_control_node')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.move_cmd = Twist()
        self.settings = termios.tcgetattr(sys.stdin)

    def get_key(self):
        tty.setraw(sys.stdin.fileno())
        select.select([sys.stdin], [], [], 0)
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        return key

    def timer_callback(self):
        key = self.get_key()
        if key == 'w':
            self.move_cmd.linear.x = 0.2
            self.move_cmd.angular.z = 0.0
        elif key == 's':
            self.move_cmd.linear.x = -0.2
            self.move_cmd.angular.z = 0.0
        elif key == 'a':
            self.move_cmd.linear.x = 0.0
            self.move_cmd.angular.z = 0.2
        elif key == 'd':
            self.move_cmd.linear.x = 0.0
            self.move_cmd.angular.z = -0.2
        elif key == 'q':
            self.move_cmd.linear.x = 0.0
            self.move_cmd.angular.z = 0.0
        else:
            self.move_cmd.linear.x = 0.0
            self.move_cmd.angular.z = 0.0
        
        self.publisher_.publish(self.move_cmd)

def main(args=None):
    rclpy.init(args=args)
    node = KeyboardControlNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
