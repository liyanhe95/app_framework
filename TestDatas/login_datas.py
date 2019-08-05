#正常场景 -- 登陆成功的测试数据;
login_success = [{"phone":"18877314371",
               "password":"314371",
               "check":"心若向陽 ，無謂悲傷"}]

#异常场景  -- 手机号码或密码为空 -- toast提示
wrong_user = [
    {"phone": "18877314371", "password": "", "check": "手机号码或密码不能为空"},
    {"phone": "", "password": "123456", "check": "手机号码或密码不能为空"}
]

#异常场景 --手机号码或密码错误，提示错误的账号信息-- toast提示
login_wrong = [
    {"phone":"18877314371","password":"123456","check":"错误的账号信息"},
    {"phone":"18877314360","password":"314371","check":"错误的账号信息"}
]

