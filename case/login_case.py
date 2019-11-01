"""
登录测试用例
"""

import unittest
import time

from page.index_page import IndexProxy
from page.login_page import LoginProxy
from utils import DriverUtil


class TestShop(unittest.TestCase):
    """TPShop测试类"""

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()  # 获取浏览器对象
        cls.login_proxy = LoginProxy()  # 获取登录业务层执行对象
        cls.index_proxy = IndexProxy()

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        DriverUtil.quit_driver()  # 退出浏览器对象

    def setUp(self):
        self.driver.get("http://127.0.0.1/")  # 跳转首页
        self.index_proxy.go_to_login_page()  # 跳转登录页

    def test_tpshop_login(self):
        """测试登录方法"""
        # self.login_proxy.login('18888888888','8888','8888')
        self.login_proxy.login('13800001111', '123456', '8888')
        time.sleep(5)
        title = self.driver.title  # 获取页面标题
        print('标题为:', title)
        self.assertIn('我的账户', title)  # 断言判断结果


if __name__ == '__main__':
    unittest.main()
