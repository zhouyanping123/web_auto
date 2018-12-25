#coding:utf-8
from selenium import webdriver
import unittest
from pages.login_page import LoginPage,login_url
import time

'''
1,输入用户名，输入密码，点击登录
2，输入用户名，不输入密码，点击登录
3，输入错误的用户名，密码，点击登录
4，点击忘记密码
'''

class LoginPageCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.loginp = LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(login_url)
        self.loginp.is_exist_alert()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def test_01(self):
        '''输入用户名，输入密码，点击登录'''
        self.loginp.input_user("zhouyanping")
        self.loginp.input_pwd("zhouyanping")
        self.loginp.click_login_button()
        gu = self.loginp.get_login_info()
        assert gu == "周艳萍"

    def test_02(self):
        '''输入用户名，不输入密码，点击登录'''
        self.loginp.input_user("zhouyanping")
        self.loginp.click_login_button()
        gu = self.loginp.get_login_info()
        assert gu == ""

    def test_03(self):
        '''输入错误的用户名，密码，点击登录'''
        self.loginp.input_user("zhouyanping")
        self.loginp.input_pwd("123456")
        self.loginp.click_login_button()
        gu = self.loginp.get_login_info()
        assert gu == ""

    def test_04(self):
        '''点击忘记密码'''
        self.loginp.click_forget_pwd()
        gu = self.loginp.get_element()
        assert gu == "刷新"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()







