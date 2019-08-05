#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/11/28 17:04

import os

#框架项目顶层目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #项目根路径


testdatas_dir =  os.path.join(base_dir,"TestDatas")

testcases_dir =  os.path.join(base_dir,"TestCases")

htmlreport_dir =  os.path.join(base_dir,"Outputs/Reports")

logs_dir =  os.path.join(base_dir,"Outputs/Logs")


screenshot_dir = os.path.join(base_dir,"Outputs/Screenshots")

#caps
caps_dir = os.path.join(base_dir,"Desired_Caps")
