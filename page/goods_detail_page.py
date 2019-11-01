"""
商品详情页面
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from utils import DriverUtil


class GoodDetailPage(BasePage):
    """商品详情-对象库层"""

    def __init__(self):
        super().__init__()  # 获取浏览器对象
        self.join_cart_btn = (By.ID, 'join_cart')  # 加入购物车按钮
        self.join_result = (By.CSS_SELECTOR, '.conect-title')  # 添加购物车结果

    def find_join_cart_btn(self):
        """加入购物车按钮方法"""
        return self.find_element_func(self.join_cart_btn)

    def find_join_result(self):
        """添加购物车结果定位"""
        return self.find_element_func(self.join_result)


class GoodDetailHandle(object):
    """商品详情-操作层"""

    def __init__(self):
        self.good_detail_page = GoodDetailPage()

    def click_join_cart_btn(self):
        """加入 购物车按钮 方法"""
        self.good_detail_page.find_join_cart_btn().click()

    def get_join_result(self):
        """添加购物车结果方法"""
        # frame切换
        driver = DriverUtil.get_driver()
        driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
        return self.good_detail_page.find_join_result().text


class GoodDetailProxy(object):
    """业务层"""

    def __init__(self):
        self.good_detail_handle = GoodDetailHandle()

    def join_cart_func(self):
        """点击加入购物车方法"""
        self.good_detail_handle.click_join_cart_btn()

    def get_result(self):
        """添加购物车结果方法"""
        return self.good_detail_handle.get_join_result()
