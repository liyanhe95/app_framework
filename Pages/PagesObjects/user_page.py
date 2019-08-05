from Pages.PagesObjects.basepage import BasePage
from Pages.PagesLocators.user_page_loactor import UserPageLocator as loc
class UserPage(BasePage):

    #获取用户余额
    def get_userLeftMoney(self):
        name="个人页面_获取用户余额"
        #等待元素
        self.wait_eleVisible(loc.user_leftMoney,model=name)
        #获取个人可用余额的文本内容
        text = self.get_text(loc.user_leftMoney,model=name)
        # 截取数字部分 - 分隔符为 元
        return text.strip("元").replace(",","")

    def get_user_nickname(self):
        pass

    def settting(self):
        pass

    # 手势密码取消和设置进入
    # 设置手势
    def popup_setGesture_confirm(self):
        self.wait_eleVisible(loc.popup_setGesture_confirm_button)
        self.get_element(loc.popup_setGesture_confirm_button).click()

    # 暂不设置
    def popup_setGesture_cancel(self):
        self.wait_eleVisible(loc.popup_setGesture_cancel_button,timeout=7)
        self.get_element(loc.popup_setGesture_cancel_button).click()

    #获取第一条投资记录的时间、投资金额、收益金额 -- 扩展
    # def get_first_investRecord_info(self):
    #     pass