#!/usr/bin/env python3
import time
import rospy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Vector3


def talker():
    pub = rospy.Publisher('chatter', Imu, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    timezero=time.time()
    accx=0
    while not rospy.is_shutdown():
        if accx<2.5:
            accx=time.time()-timezero

        lin_acc = Vector3(accx,0,9.81)
        ang_vel = Vector3(0,0,accx*4)
        mes=Imu(linear_acceleration=lin_acc,angular_velocity=ang_vel)
        rospy.loginfo(mes)
        pub.publish(mes)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass