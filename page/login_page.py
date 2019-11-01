"""
登录页面
"""
from selenium.webdriver.common.by import By
from base.bas import BasePage, BaseHandle



class LoginPage(BasePage):
    """登录-对象库层"""
    def __init__(self):
        super().__init__()
        self.username = (By.ID,'username')
        self.password = (By.ID,'password')
        self.verify_code = (By.ID,'verify_code')
        self.login_btn = (By.NAME,'sbtbutton')
    def find_username(self):
        return self.find_element_func(self.username)
    def find_password(self):
        return self.find_element_func(self.password)
    def find_varify_code(self):
        return self.find_element_func(self.verify_code)
    def find_login_btn(self):
        return self.find_element_func(self.login_btn)


class LoginHandle(BaseHandle):
    """登录-操作层"""
    def __init__(self):
        self.login_page = LoginPage()#获取对象库层对象
    def input_username(self,name):
        """用户名输入方法"""
        self.input_text(self.login_page.find_username(),name)
    def input_password(self,pwd):
        """密码输入方法"""
        self.input_text(self.login_page.find_password(),pwd)
    def input_verify_code(self,code):
        """验证码输入方法"""
        self.input_text(self.login_page.find_varify_code(),code)
    def click_login_btn(self):
        """登录按钮点击方法"""
        self.login_page.find_login_btn().click()



class LoginProxy(object):
    """登录操作层"""
    def __init__(self):#获取操作层对象
        self.login_handle = LoginHandle()
    def login(self,name,pwd,code):
        """登录方法"""
        self.login_handle.input_username(name)#输入用户名
        self.login_handle.input_password(pwd)#输入密码
        self.login_handle.input_verify_code(code)#输入验证码
        self.login_handle.click_login_btn()#点击登录