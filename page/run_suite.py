from base.base_page import BaseHandle, BasePage
from selenium.webdriver.common.by import By


class OrderPayPage(BasePage):
    # 订单支付 -- 对象库层
    def __init__(self):
        super().__init__()
        self.wait_for_pay = (By.LINK_TEXT, "代付款")
        self.now_pay = (By.LINK_TEXT, "立即支付")

    def find_wait_for_pay(self):
        return self.find_element_func(self.wait_for_pay)

    def find_now_for_pay(self):
        return self.find_element_func(self.find_now_for_pay)


class OrderPayHandle(BaseHandle):
    # 订单支付 -- 操作层
    def __init__(self):
        self.order_pay = OrderPayPage()

    def click_wait_for_pay(self):
        self.order_pay.find_wait_for_pay().click()

    def click_now_for_pay(self):
        self.order_pay.find_now_for_pay().click()


class OrderPayProxy(object):
    # 订单支付 --业务层
    def __init__(self):
        self.orderpayproxy = OrderPayHandle()

    def order_by_1(self):
        self.orderpayproxy.click_now_for_pay()
        self.orderpayproxy.click_wait_for_pay()

