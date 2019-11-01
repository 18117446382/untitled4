"""
订单页面
"""
from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandle


class OrderCheckPage(BasePage):
    """订单确认-对象库层"""

    def __init__(self):
        super().__init__()  # 获取浏览器对象
        self.submit_order_btn = (By.LINK_TEXT, '提交订单')  # 提交订单按钮

    def find_submin_order_btn(self):
        """提交订单按钮定位方法"""
        return self.find_element_func(self.submit_order_btn)


class OrderCheckHandle(BaseHandle):
    """操作层"""

    def __init__(self):
        self.order_check_page = OrderCheckPage()  # 元素定位获取对象

    def click_submin_order_btn(self):
        """提交订单按钮点击方法"""
        self.order_check_page.find_submin_order_btn().click()


class OrderCheckProxy(object):
    """业务层"""

    def __init__(self):
        self.order_check_handle = OrderCheckHandle()  # 操作对象

    def submin_osder_func(self):
        """提交订单方法"""
        self.order_check_handle.click_submin_order_btn()
