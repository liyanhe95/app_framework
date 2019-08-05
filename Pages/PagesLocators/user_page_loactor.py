from appium.webdriver.common.mobileby import MobileBy as Mb

class UserPageLocator:
    # 用户余额
    user_leftMoney = (Mb.ID,"com.xxzb.fenwoo:id/tv_leave")
    # 功能区
    user_functions_locator = (Mb.ID,"com.xxzb.fenwoo:id/tv_opt_name")
    # 用户昵称
    user_nickname_locator = (Mb.ID,"com.xxzb.fenwoo:id/tv_name")

    #弹框
    # 手势密码设置弹框 - 立马设置按钮
    popup_setGesture_confirm_button = (Mb.ID,"com.xxzb.fenwoo:id/btn_confirm")
    # 手势密码设置弹框 - 以后再说按钮
    popup_setGesture_cancel_button = (Mb.ID,"com.xxzb.fenwoo:id/btn_cancel")


