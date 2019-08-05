from appium.webdriver.common.mobileby import MobileBy

class LoginPageLocator:
    #我的柠檬
    lemon_element = (MobileBy.ID,"com.lemon.lemonban:id/navigation_my")
    #点击头像登陆
    head_element = (MobileBy.ID,"com.lemon.lemonban:id/fragment_my_lemon_avatar_title")
    phone_input = (MobileBy.ID, "com.lemon.lemonban:id/et_mobile")
    # 手机号码或密码不能为空
    wrong_toast_msg = (MobileBy.XPATH,'//*[contains(@text,"手机号码或密码")]')
    # 密码输入框
    password_input = (MobileBy.ID, "com.lemon.lemonban:id/et_password")
    # 错误的账号信息
    wrong_account_msg = (MobileBy.XPATH, '//*[contains(@text,"错误的账号信息")]')
    #点击登陆
    login_element = (MobileBy.ID, "com.lemon.lemonban:id/btn_login")

