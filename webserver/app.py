import os
import threading
from std_msgs.msg import String

#import rospy
from flask import Flask, render_template
from flask_socketio import SocketIO

#import ros
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

app = Flask(__name__,  template_folder='templates', static_folder='static')
socketio = SocketIO(app,cors_allowed_origins="*")

@app.route("/", methods=['GET', 'POST'])
def index():
     return render_template('index.html')

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

@socketio.on("update")
def update(data):
    print('Current Value 1', data['HSV1'])
    print('Current Value 2', data['HSV2'])
    print('Current Value 3', data['HSV3'])
    print('Current Value 4', data['HSV4'])
    print('Current Value 5', data['HSV5'])
    print('Current Value 6', data['HSV6'])

def main(args=None):
    print('Starting Flask Server')
    socketio.run(app, debug=True, host='0.0.0.0')

if __name__ == "__main__":
    main()
    