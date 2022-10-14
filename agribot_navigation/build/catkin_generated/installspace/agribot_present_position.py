#!/usr/bin/env python2
import rospy
from geometry_msgs.msg import PoseStamped
import tf
    
def print_position(list):
    for i in range(len(list)):
        print(list[i])

def get_position():
    rospy.init_node("get_position")
    listener = tf.TransformListener()
    save_position = []
    while True :
        for_save = input("wait for input: ")
        if for_save == 1:
            listener.waitForTransform('map' ,'base_footprint', rospy.Time(0) , rospy.Duration(1.0)) 
            trans, rot = listener.lookupTransform('map' ,'base_footprint', rospy.Time(0) )
            
            present_pose_x = trans[0]
            present_pose_y = trans[1]
            present_pose_z = trans[2]
            
            present_orientation_x = rot[0]
            present_orientation_y = rot[1]
            present_orientation_z = rot[2]
            present_orientation_w = rot[3]
            
            save_position = ([present_pose_x, present_pose_y, present_pose_z, present_orientation_x, present_orientation_y, present_orientation_z, present_orientation_w])
            print_position(save_position)
        elif for_save == 0:
            exit()
        else :
            print("input right number")         

if __name__ == '__main__':
    get_position()