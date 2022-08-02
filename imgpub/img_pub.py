import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImgPub(Node):
    def __init__(self):
        super().__init__('img_pub')
        self.publisher = self.create_publisher(Image, 'video_frames', 10)
        timer_period = 0.1

        self.timer = self.create_timer(timer_period, self.tiemr_callback)
        self.cap = cv2.VideoCapture(0)
        self.br = CvBridge()


    def timer_callback(self):
        ret, frame = self.cap.read()

        if ret == True:
            self.publisher_.publish(self.br.cv2_to_imgmsg(frame))

        self.get_logger().info('Publish Video')

    def main(args=None):
        rclpy.init(args=args)
        img_pub = ImgPub()
        rclpy.spin(img_pub)
        img_pub.destroy_node()
        rclpy.shutdown()

    if __name__ == '__main__':
        main()