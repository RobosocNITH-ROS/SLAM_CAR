#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys, termios, tty

class KeyboardTeleop(Node):
    def __init__(self):
        super().__init__('keyboard_teleop')
        self.publisher = self.create_publisher(Twist, '/slamurai_controller/cmd_vel_unstamped', 10)
        self.get_logger().info("Keyboard Teleop Node Started")
        self.run()

    def get_key(self):
        tty.setraw(sys.stdin.fileno())
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, termios.tcgetattr(sys.stdin))
        return key

    def run(self):
        twist = Twist()
        while rclpy.ok():
            key = self.get_key()
            if key == 'w':
                twist.linear.x = 2.0
                twist.angular.z = 0.0
            elif key == 's':
                twist.linear.x = -2.0
                twist.angular.z = 0.0
            elif key == 'a':
                twist.linear.x = 0.0
                twist.angular.z = 1.0
            elif key == 'd':
                twist.linear.x = 0.0
                twist.angular.z = -1.0
            elif key == 'x':
                twist.linear.x = 0.0
                twist.angular.z = 0.0
            else:
                continue

            self.publisher.publish(twist)
            self.get_logger().info(f"Publishing: linear={twist.linear.x}, angular={twist.angular.z}")

            if key == 'q':  # Quit on 'q'
                break

        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.publisher.publish(twist)
        self.get_logger().info("Stopped")


def main():
    rclpy.init()
    node = KeyboardTeleop()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

