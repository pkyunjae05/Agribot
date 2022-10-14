#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import PoseStamped
import tf
from move_base_msgs.msg import MoveBaseActionResult

class Agribot:
    def __init__(self):
        rospy.init_node("agribot_navigation")
        self.move_base_pub = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=1)
        self.get_waypoint = []
        
    def add_direct(self,list):
        self.get_waypoint.append(list)
        
    def nav_to_destination(self):
        for i in range(len(self.get_waypoint)):
            destination_pose_x = self.get_waypoint[i][0]
            destination_pose_y = self.get_waypoint[i][1]
            destination_pose_z = self.get_waypoint[i][2]
            
            destionation_orientation_x = self.get_waypoint[i][3]
            destionation_orientation_y = self.get_waypoint[i][4]
            destionation_orientation_z = self.get_waypoint[i][5]
            destionation_orientation_w = self.get_waypoint[i][6]
            
            self.goal_move_base(destination_pose_x, destination_pose_y, destination_pose_z, destionation_orientation_x, destionation_orientation_y, destionation_orientation_z, destionation_orientation_w)
            rospy.wait_for_message("/move_base/result", MoveBaseActionResult, timeout=None)    
 
    def goal_move_base(self, pose_x, pose_y, pose_z, ori_x, ori_y, ori_z, ori_w):
        
        msg_move_to_goal = PoseStamped()
        msg_move_to_goal.pose.position.x = pose_x 
        msg_move_to_goal.pose.position.y = pose_y
        msg_move_to_goal.pose.position.z = pose_z
        msg_move_to_goal.pose.orientation.x = ori_x
        msg_move_to_goal.pose.orientation.y = ori_y
        msg_move_to_goal.pose.orientation.z = ori_z
        msg_move_to_goal.pose.orientation.w = ori_w
        msg_move_to_goal.header.frame_id = 'map'
        
        rospy.sleep(1)
    
        self.move_base_pub.publish(msg_move_to_goal) 
        
if __name__ == '__main__':
       
    agribot = Agribot()

    agribot.add_direct([-0.0260153507156, -0.579098354641,0.00147086223095, -3.48971414009e-06,-4.11038833918e-06,0.0511170043605,0.998692671364]) # go straight
    agribot.add_direct([0.559010277604, -0.022294466122, 3.31309131093e-05,7.86070542854e-05,8.48814102932e-05,0.754915964665,0.655821525196]) # go straight
    agribot.nav_to_destination()
    # rospy.spin()
    
    
    
    