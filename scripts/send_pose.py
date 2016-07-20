#!/usr/bin/env python

"""
Send out the pose to the ur5 to achieve a line.

node : node_send_pose
publish topic : topic_pose

@author: zhw
@time: 2016/7/20

"""

import rospy
from geometry_msgs.msg import Pose

def send_pose():
    pub = rospy.Publisher('topic_pose', Pose, queue_size=10)
    rospy.init_node('node_send_pose', anonymous=True)

    ms_pose = Pose()
    ms_pose.position.x = 0.3
    ms_pose.position.y = 0.2
    ms_pose.position.z = 0.2

    rate = rospy.Rate(0.5) # 10hz

    flag_1 = 1
    while not rospy.is_shutdown():

        if (flag_1 == 1) and (ms_pose.position.x >= 0.6):
            flag_1 = -1
        elif (flag_1 == -1) and (ms_pose.position.x <= 0.4):
            flag_1 = 1
        elif (flag_1 == -1) and (ms_pose.position.x < 0.6) and (ms_pose.position.x > 0.4):
            flag_1 = -1
        else:
            flag_1 = 1
        ms_pose.position.x += 0.05*flag_1
        
        # if ms_pose.position.x > 0.7:
        #     rospy.signal_shutdown("x reaches to 0.8m")
        #     pass
        
        pub.publish(ms_pose)

        pose_str = "send out pose is %s" % ms_pose.position.x
        rospy.loginfo(pose_str)

        rate.sleep()

if __name__ == '__main__':
    try:
        send_pose()
    except rospy.ROSInterruptException:
        pass
