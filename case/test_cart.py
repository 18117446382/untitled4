"""
购物车-测试用例
"""
import unittest

from page.goods_detail_page import GoodDetailProxy
from page.index_page import IndexProxy
from page.search_list_page import SearchListProxy
from utils import DriverUtil


class TestTPShopCart(unittest.TestCase):
    """购物车测试类"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtil.get_driver()  # 获取浏览器对象
        cls.index_proxy = IndexProxy()  # 首页页面业务执行对象
        cls.search_list_proxy = SearchListProxy()  # 搜索列表页面业务执行对象
        cls.goods_detail_proxy = GoodDetailProxy()  # 商品详情页面业务执行对象

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()  # 退出浏览器对象

    def setUp(self) -> None:
        self.driver.get('http://127.0.0.1/')  # 跳转首页

    def test_cart(self):
        """购物车测试方法"""
        goods_name = '小米手机5'
        self.index_proxy.search_goods(goods_name)  # 搜索商品
        self.search_list_proxy.go_to_goods_detail(goods_name)  # 跳转商品详情页面
        self.goods_detail_proxy.join_cart_func()  # 添加购物车
        result = self.goods_detail_proxy.get_result()  # 获取添加结果
        print('添加结果为:', result)
        self.assertIn('添加成功', result)  # 断言判



if __name__ == '__main__':
    unittest.main()
