import rclpy 
from rclpy.node import Node 
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
 
class Img_Sub(Node):
 
  def __init__(self):

    super().__init__('img_sub')
    self.subscription = self.create_subscription(Image, 'video_frames', self.listener_callback, 10)
    self.subscription 
      
    self.br = CvBridge()
   
  def listener_callback(self, data):

    self.get_logger().info('Receiving video')
    current_frame = self.br.imgmsg_to_cv2(data)
    cv2.imshow("camera", current_frame)
    cv2.waitKey(1)
  
def main(args=None):
  
  rclpy.init(args=args)
  img_sub = Img_Sub()
  rclpy.spin(img_sub)
  img_sub.destroy_node()
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()
