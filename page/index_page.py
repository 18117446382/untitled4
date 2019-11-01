"""
首页页面业务执行对象
"""
from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandle


class IndexPage(BasePage):
    """搜索列表—对象层"""

    def __init__(self):
        super().__init__()  # 获取父类的浏览器对象
        self.login_link = (By.LINK_TEXT, '登录')  # 登录链接
        self.search_bar = (By.ID, 'q')  # 搜索框
        self.search_btn = (By.CLASS_NAME, 'ecsc-search-button')  # 搜索按钮
        self.my_cart_btn = (By.CLASS_NAME, 'share-shopcar-index')  # 我的购物车

    def find_login_link(self):
        """登录链接定位方法"""
        return self.find_element_func(self.login_link)

    def find_search_bar(self):
        """搜索框定位方法"""
        return self.find_element_func(self.search_bar)

    def find_search_btn(self):
        """搜索按钮定位方法"""
        return self.find_element_func(self.search_btn)

    def find_my_cart_btn(self):
        """我的购物车定位方法"""
        return self.find_element_func(self.my_cart_btn)


class IndexHandle(BaseHandle):
    """搜索列表—操作层"""

    def __init__(self):
        self.index_page = IndexPage()  # 元素定位对象

    def click_login_link(self):
        # 登录链接点击方法
        self.index_page.find_login_link().click()

    def input_search_bar(self, kw):
        """搜索框输入方法"""
        self.input_text(self.index_page.find_search_bar(), kw)

    def click_search_btn(self):
        """搜索框按钮点击方法"""
        self.index_page.find_search_btn().click()

    def click_my_cart_btn(self):
        """我的购物车按钮点击方法"""
        self.index_page.find_my_cart_btn().click()


class IndexProxy(object):
    """搜索列表—业务层"""

    def __init__(self):
        self.index_handle = IndexHandle()  # 操作对象

    def go_to_login_page(self):
        # 跳转登录页面
        self.index_handle.click_login_link()

    def search_goods(self, kw):
        """搜索商品方法"""
        self.index_handle.input_search_bar(kw)  # 输入关键字
        self.index_handle.click_search_btn()  # 点击搜索

    def go_to_goods_cart(self):
        """跳转购物车页面方法"""
        self.index_handle.click_my_cart_btn()
