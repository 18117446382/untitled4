"""购物车测试用例"""
import unittest
from asyncio import sleep

from page.goods_detail_page import GoodDetailProxy
from page.index_page import IndexProxy
from page.search_list_page import SearchListProxy
from utils import DriverUtil


class TestTPShopCart(unittest.TestCase):
    """购物车测试类"""

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil.get_driver()  # 获取浏览器对象
        cls.index_proxy = IndexProxy()  # 首页页面业务执行对象
        cls.search_list_proxy = SearchListProxy()  # 搜索列表页面业务执行对象
        cls.good_detail_proxy = GoodDetailProxy()  # 商品详情页面

    # @classmethod
    # def tearDownClass(cls):
    #     DriverUtil.quit_driver() #退出浏览器对象
    def setUp(self):
        self.driver.get("http://127.0.0.1/")  # 跳转浏览器对象

    def test_cart(self):
        """购物车测试方法"""
        goods_name = '小米手机5'
        self.index_proxy.search_goods(goods_name)  # 搜索商品
        # sleep(3)
        self.search_list_proxy.go_to_good_detail(goods_name)  # 跳转商品详情页面
        # sleep(3)
        self.good_detail_proxy.join_cart_func()  # 点击添加购物车
        # sleep(3)
        result = self.good_detail_proxy.get_result()  # 获取添加结果
        print('添加结果为：', result)
        self.assertIn('添加成功', result)  # 断言


if __name__ == '__main__':
    unittest.main()
