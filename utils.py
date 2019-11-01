"""
公共方法
"""
import time
from selenium import webdriver


def switc_to_new_window():
    #     "切换新窗口方法"
    driver = DriverUtil.get_driver()
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])


def get_text_element(text):
    """获取文本信息对应元素方法"""
    xpath = '//*[contains(text(),"{}")]'.format(text)
    driver = DriverUtil.get_driver()
    try:
        element = driver.find_element_by_xpath(xpath)
        return element
    except Exception:
        return False


class DriverUtil(object):
    """浏览器工具类"""
    driver = None  # 为了表示浏览器对象的初始化状态(判断条件无法表示对象状态)

    @classmethod
    def get_driver(cls):
        """获取浏览器对象方法"""
        # 为了保证获取的浏览器对象始终是同一个, 需要条件判断浏览器对象的状态
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.get('http://127.0.0.1/')
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        """退出浏览器对象方法"""
        # 需要判断浏览器对象存在再执行退出操作
        if cls.driver:
            cls.driver.quit()
            cls.driver = None  # 保险措施, 确保浏览器对象的初始化状态


if __name__ == '__main__':
    DriverUtil.get_driver()
    time.sleep(2)
    DriverUtil.quit_driver()
