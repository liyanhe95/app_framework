#根据测试用例需求，动态配置参数
import yaml
import os
from Common.contants import caps_dir
from appium import webdriver
import pytest

#登陆功能：重置
@pytest.fixture
def start_app_withReset():
    driver = basedriver(False)
    yield driver
    driver.close_app()
    driver.quit()

#题库功能：不重置，记住用户状态，不需要每次都重新登陆
# 首先要确认用户是否登陆。如果没有，则先登陆

@pytest.fixture
def start_app():
    #启动会话
    driver = basedriver()
    #确认用户是否登陆
    is_login()
    yield driver
    driver.close_app()
    driver.quit()

#确认用户是否已登陆。进入题库，判断是否有【去登陆】提示
#如果没有，pass。如果有
def is_login():
    flag = 0
    try:
        pass
        #进入题库，找【去登陆】提示，如果没有找到会抛异常，如果找到了，表示没有登陆
        #如果找到flag = 1
        flag = 1  #flag=1,说明要登陆
    except:
        #已登陆
        pass
    if flag == 1:
        pass
        # 登陆

def basedriver(noReset=None,port=4723,**kwargs):
    #从yaml里面读取启动参数
    fs = open(os.path.join(caps_dir,"desired_caps.yaml"),encoding='UTF-8')
    desired_caps = yaml.load(fs)
    if noReset is not None:
        desired_caps["noReset"] = noReset

    if kwargs:
        #修改从配置文件这读取出来的desired_caps,如果有不一样的地方
        pass
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub'.format(port),desired_caps)
    return driver
    #启动appium会话  - 连接appium server 端口号
