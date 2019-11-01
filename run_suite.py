"""
执行测试套件(程序入口)
"""
# 导包
import unittest
from case.test_cart import TestTPShopCart
from case.test_login import TestTPShopLogin
from case.test_order import TestTPShopOrder
from utils import DriverUtil

# 初始化套件对象
suite = unittest.TestSuite()

# 调用方法组装测试用例
suite.addTest(unittest.makeSuite(TestTPShopLogin))  # 登录测试脚本
suite.addTest(unittest.makeSuite(TestTPShopCart))  # 添加购物车脚本
suite.addTest(unittest.makeSuite(TestTPShopOrder))  # 提交订单和订单支付脚本

# 关闭浏览器退出方法
DriverUtil.change_quit_status(False)

# 初始化测试执行对象并调用方法
unittest.TextTestRunner().run(suite)

# 打开浏览器退出方法
DriverUtil.change_quit_status(True)

# 再次调用浏览器退出方法
DriverUtil.quit_driver()