from Pages.PagesObjects.basepage import BasePage
from Pages.PagesLocators.login_page_locator import LoginPageLocator as loc

class LoginPage(BasePage):

    #登陆功能
    def input_phone(self,phone):
        #输入用户名、密码、点击登陆
        name="输入手机号码页面"
        #点击我的柠檬
        self.wait_eleVisible(loc.lemon_element, model=name)
        self.click_element(loc.lemon_element, model=name)
        #点击我的头像
        self.wait_eleVisible(loc.head_element,model=name)
        self.click_element(loc.head_element,model=name)

        self.wait_eleVisible(loc.phone_input,model=name)
        self.input_text(loc.phone_input,phone,model=name)
        return self

    def input_password(self,password):
        name = "输入密码页面"
        #等待
        self.wait_eleVisible(loc.password_input,model=name)
        self.input_text(loc.password_input,password, model=name)
        self.click_element(loc.login_element, model=name)
        return self

    def get_login_toastMag(self):
        name = "登录成功_toast信息获取"
        msg = "心若向陽 ，無謂悲傷"
        return self.get_toast_msg(msg,model=name)

    #密码不正确的提示信息：手机号码或密码不能为空
    def get_phoneAndpasswordError_toastMsg(self):
        name = "手机号码或密码不正确_toast信息获取"
        msg = "手机号码或密码不能为空"
        return self.get_toast_msg(msg,model=name)

    #账户或密码不正确的提示信息:错误的账号信息
    def get_accountError_toastMsg(self):
        name = "账户或密码不正确_toast信息获取"
        msg = "错误的账号信息"
        return self.get_toast_msg(msg,model=name)