"""
购物车页面
"""
from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandle


class GoodsCartPage(BasePage):
    """购物车-对象库层"""

    def __init__(self):
        super().__init__()
        self.check_all = (By.CLASS_NAME, 'checkCartAll')  # 全选框
        self.go_pay_btn = (By.LINK_TEXT, '去结算')  # 去结算

    def find_check_all(self):
        """全选框定位方法"""
        return self.find_element_func(self.check_all)

    def find_go_pay_btn(self):
        """去结算按钮定位方法"""
        return self.find_element_func(self.go_pay_btn)


class GoodsCarHandle(BaseHandle):
    """购物车-操作层"""

    def __init__(self):
        self.goods_cart_page = GoodsCartPage()  # 获取对象层对象

    def click_check_all(self):
        """点击全选框"""
        # 判断全选框选中状态
        check_element = self.goods_cart_page.find_check_all()
        if not check_element.is_selected():  # 如果全选框不被选中
            check_element.click()  # 点击全选
        # self.goods_cart_page.find_check_all().click()

    def click_go_pay_btn(self):
        """点击去结算"""
        self.goods_cart_page.find_go_pay_btn().click()


class GoodsCarProxy(object):
    """购物车-业务层"""

    def __init__(self):
        self.goods_cart_handle = GoodsCarHandle()  # 获取操作对象

    def go_to_order_check(self):
        self.goods_cart_handle.click_check_all()  # 确认全选
        self.goods_cart_handle.click_go_pay_btn()  # 点击去结算
