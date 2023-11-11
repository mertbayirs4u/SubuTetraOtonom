#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
from  geometry_msgs.msg import Twist
import time
import math

def ucgen_ciz():
    rospy.init_node("ucgen_ciz")
    pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)
    hiz_mesaji = Twist()

    for i in range(4):
        rospy.loginfo("kosedesiniz...")
        hiz_mesaji.linear.x = 0.3  
        mesafe = 1.0
        yer_degistirme = 0.0
        t0 = rospy.Time.now().to_sec()

        while (yer_degistirme < mesafe):
            pub.publish(hiz_mesaji)
            t1 = rospy.Time.now().to_sec()
            yer_degistirme = hiz_mesaji.linear.x * (t1 - t0)

        hiz_mesaji.linear.x = 0.0
        pub.publish(hiz_mesaji)

    
        radyansaniye = math.radians(120)  
        hiz_mesaji.angular.z = radyansaniye
        pub.publish(hiz_mesaji)
        
        donme_suresi =1.0
        time.sleep(donme_suresi)
        
        hiz_mesaji.angular.z = 0.0
        pub.publish(hiz_mesaji)
        
        rospy.loginfo("Donuldu...")
        
ucgen_ciz()
