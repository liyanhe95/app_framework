from Pages.PagesObjects.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy

class CommonBus(BasePage):

    def switch_navigate(self,name):
        loc = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("{}")'.format(name))
        self.wait_eleVisible(loc)
        self.click_element(loc)