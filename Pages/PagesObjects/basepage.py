from Pages.PagesLocators.login_page_locator import LoginPageLocator as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from Common import logger
import logging
import time
import datetime
from Common import contants
from appium.webdriver.common.mobileby import MobileBy


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self, loc, timeout=30, poll_frequency=0.5, model=None):
        """
        :param loc: 元素定位表达。元组类型，表达方式(元素定位类型，元素定位方法)
        :param timeout: 等待上限。
        :param poll_frequency: 轮询频率
        :param model: 等待失败时，截图操作，图片文件中需要表达的功能模块标注。
        :return: None
        """
        logging.info("{1}: 等待元素可见 {0}".format(loc, model))
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(loc))
            end = time.time()
            logging.info("等待时长：以秒为单位")
        except:
            logging.exception("等待元素可见失败。")
            # 截图
            self.save_webImgs(model)
            raise

    def get_visible_element(self, locator, eqc=20) -> WebElement:
        try:
            return WebDriverWait(self.driver, eqc).until(
                EC.visibility_of_element_located(locator)
            )
        # save_screenshot  保存截屏
        except Exception as e:
            logging.exception('no this element:{}'.format(e))
            self.driver.save_screenshot("{}.jpg".format(time.time()))
            raise e

        # 查找一个元素
    def get_element(self, loc, model=None):
        logging.info("{0}：查找元素 {1}".format(model, loc))
        try:
            return self.driver.find_element(*loc)
        except:
            logging.exception("查找元素失败。")
            # 截图
            self.save_webImgs(model)
            raise

    # 输入操作
    def input_text(self, loc, text, model=None):
        # 查找元素
        ele = self.get_element(loc)
        # 输入操作
        logging.info("{0}: 在元素 {1} 中输入文本：{2}".format(model, loc, text))
        try:
            ele.send_keys(text)
        except:
            logging.exception("输入操作失败")
            # 截图
            self.save_webImgs(model)
            raise

    # 清除操作
    def clear_input_text(self, loc, model=None):
        # 找元素再清除
        ele = self.get_element(loc, model)
        # 点击操作
        logging.info("{0}: 元素：{1} 清除文本内容。".format(model, loc))
        try:
            ele.clear()
        except:
            # 捕获异常到日志中；
            logging.exception("元素：{0} 清除文本内容失败。：".format(loc))
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self.save_webImgs(model)
            # 抛出异常
            raise

    # 点击操作
    def click_element(self, loc: object, model: object = None) -> object:
        # 找到元素
        ele = self.get_element(loc, model)
        # 点击操作
        logging.info("{0}: 元素：{1} 点击事件。".format(model, loc))
        try:
            ele.click()
        except:
            # 捕获异常到日志中；
            logging.exception("元素：{0} 点击事件失败：".format(loc))
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self.save_webImgs(model)
            # 抛出异常
            raise

    # 获取文本内容
    def get_text(self, loc, model=None):
        # 找到元素
        ele = self.get_element(loc, model)
        # 获取元素的文本内容
        logging.info("{0}：获取元素：{1} 的文本内容".format(model, loc))
        try:
            text = ele.text
            logging.info("{0}：元素：{1} 的文本内容为：{2}".format(model, loc, text))
            return text
        except:
            # 捕获异常到日志中；
            logging.exception("获取元素：{0} 的文本内容失败。报错信息如下：".format(loc))
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self.save_webImgs(model)
            # 抛出异常
            raise

    # 获取元素的属性
    def get_element_attribute(self, loc, attr_name, model=None):
        # 找到元素
        ele = self.get_element(loc, model)
        # 获取元素的属性
        logging.info("{0}: 获取元素：{1} 的属性：{2}".format(model, loc, attr_name))
        try:
            value = ele.get_attribute(attr_name)
            logging.info("{0}: 元素：{1} 的属性：{2} 值为：{3}".format(model, loc, attr_name, value))
            return value
        except:
            # 捕获异常到日志中；
            logging.exception("获取元素：{0} 的属性：{1} 失败，异常信息如下：".format(loc, attr_name))
            # 截图 - 保存到的指定的目录。名字要想好怎么取？
            self.save_webImgs(model)
            # 抛出异常
            raise

    # 截图
    def save_webImgs(self, model=None):
        # filepath=指的图片保存目录/model(页面功能名称)_当前时间到秒.png
        filePath = contants.screenshot_dir + \
                   "/{0}_{1}.png".format(model, time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
        # 截图文件存放在 Screenshot目录下
        # driver方法：self.driver.save_screenshot()
        filepath = ""
        try:
            self.driver.save_screenshot(filepath)
            logging.info("截屏成功。图片路径为{0}".format(filePath))
        except:
            logging.exception("截图失败")

    # webview切换
    def switch_webview(self, webview_name, timeout=30, poll_frequency=0.5, model=None):
        # 等待webview元素出现
        loc = (MobileBy.CLASS_NAME, "android..webview")
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((loc)))
        # 获取所有的上下文  列表
        contexts = self.driver.contexts
        # 判断你webview 名称  是否  在当前的上下文当中，如果 在就切换，如果不在就报错。
        if webview_name in contexts:
            # 切换
            pass
        else:
            # 抛出异常。
            pass

    # 获取设备的大小
    def get_device_size(self):
        try:
            return self.driver.get_window_size()
        except:
            print("输出当前设备的大小")
    #滑屏操作-左右、上下,默认向左滑动
    #左右滑动  y不变，x变
    def swipe_left_right(self,start_per=0.9,end_per=0.1):
        size = self.get_device_size()
        self.driver.swipe(size["widht"]*start_per,size["height"]*0.5,size["widht"]*end_per,size["height"]*0.5,200)
        time.sleep(0.5)
        # 滑屏操作 - 向上滑屏

    def swipe_up_down(self, start_y_percent=0.9, end_y_percent=0.1):
        size = self.driver.get_window_size()
        starty = size["height"] * start_y_percent
        endy = size["height"] * end_y_percent
        x = size["width"] * 0.5
        self.driver.swipe(x, starty, x, endy, 200)

    #列表滑动===找元素，需要翻页才能看到其它的内容
    def scroll_list(self,str_obj=None):
        if str is not None:
            old = self.driver.page_source
            new_src = ""
            size =self.driver.get_window_size()
            while old != new_src:
                # 把new的值给old赋值，因为new马上就要更新了（滑动新的页面之前需要把旧的值给到old）
                old = new_src
                # 从下向上滑动一次
                self.driver.swipe(size["width"] * 0.5, size["height"] * 0.9, size["width"] * 0.5, size["height"] * 0.2, 200)
                # 获取滑动之后的页面内容
                new_src = self.driver.page_source
                # 其它的需求：滑一次找一次的内容
                if new_src.find("逻辑思维题") != -1:
                    print("找到了")
                    break

    #toast获取
    #h5切换
    # 获取元素的大小、坐标

    # toast获取
    def get_toast_msg(self, part_text, model=None):
        # xpath表达式 ---文本匹配去获取
        # uiautomator2
        # 等待元素存在，而不是元素可见
        xpath_loc = '//*[contains(@text,"{}")]'.format(part_text)
        logging.info("{0}: 获取toast信息，表达式为：{1}".format(model, xpath_loc))
        try:
            # 等待元素存在
            WebDriverWait(self.driver, 10, 0.01).until(EC.presence_of_element_located((MobileBy.XPATH, xpath_loc)))
            return self.driver.find_element_by_xpath(xpath_loc).text
        except:
            # 抛异常
            logging.exception("获取toast失败")
            self.save_webImgs(model)
            raise
            pass
    #藏起键盘
    def hide_keyboard(self):
        pass




