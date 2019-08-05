import pytest
import logging
from Pages.PagesObjects.login_page import LoginPage
from Pages.PagesObjects.common_business import CommonBus as Cb
from TestDatas import login_datas as LD

@pytest.mark.usefixtures("start_app")
class TestLogin:

    @pytest.mark.failone
    @pytest.mark.parametrize("data", LD.wrong_user)
    def test_wrong_1(self, start_app, data):
        logging.info("*********登陆用例：异常场景：手机号码或密码为空*********")
        # 步骤
        # 点击我的柠檬
        Cb(start_app).switch_navigate("我的柠檬")
        lp = LoginPage(start_app)
        lp.input_phone(data["phone"])
        lp.input_password(data["password"])
        # 断言 - 错误提示信息匹配
        try:
            assert lp.get_phoneAndpasswordError_toastMsg() == data["check"]
        except:
            logging.exception("断言失败")
            lp.save_webImgs("登陆异常_手机号码或密码为空_断言")
            raise

    @pytest.mark.failtwo
    @pytest.mark.parametrize("data", LD.login_wrong)
    def test_wrong_2(self, start_app, data):
        logging.info("*********登陆用例：异常场景：手机号码或密码错误，提示错误的账号信息*********")
        # 步骤
        # 点击我的柠檬
        Cb(start_app).switch_navigate("我的柠檬")
        lp = LoginPage(start_app)
        lp.input_phone(data["phone"])
        lp.input_password(data["password"])
        # 断言 - 错误提示信息匹配
        try:
            assert lp.get_accountError_toastMsg() == data["check"]
        except:
            logging.exception("断言失败")
            lp.save_webImgs("登陆异常_错误的账号信息_断言")
            raise

    @pytest.mark.parametrize("data", LD.login_success)
    def test_normal_login(self, start_app,data):
        # 步骤
        # 点击我的柠檬
        Cb(start_app).switch_navigate("我的柠檬")
        # 输入用户名，点击下一步,,#输入密码，点击下一步
        lp = LoginPage(start_app)
        lp.input_phone(data["phone"])
        lp.input_password(data["password"])
        try:
            assert lp.get_login_toastMag() == data["check"]
        except:
            logging.exception("断言失败")
            lp.save_webImgs("登陆成功_获取断言失败")
            raise

        # LoginPage(start_app).input_phone(LD.login_success["phone"]).input_password(LD.login_success["password"])
        # 断言
        # 判断个人页面元素
        # Cb(start_app).switch_navigate("心若向陽 ，無謂悲傷")
