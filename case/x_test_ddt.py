#coding:utf-8
import os
import unittest

import ddt
from selenium import webdriver

from pages.excel_read import ExcelUtil
from pages.login_page import LoginPage, login_url

'''
1,输入用户名，输入密码，点击登录
2，输入用户名，不输入密码，点击登录
3，输入错误的用户名，密码，点击登录
'''

# testdata = [
#     {"username":"zhouyanping","pwd":"zhouyanping","res":True},
#     {"username":"zhouyanping","pwd":"","res":False},
#     {"username":"zhouyanping","pwd":"123456","res":False}
# ]

propath = os.path.dirname(os.getcwd())
firepath = os.path.join(propath, "data", "datas.xlsx")
print(firepath)
# firepath = "F:\\study\\web_auto\\data\\datas.xlsx"
data = ExcelUtil(firepath)
testdata = data.dict_data()
print(testdata)

@ddt.ddt
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

    def login_case(self,username,pwd,res):
        self.loginp.login(username,pwd)
        # gu = self.loginp.get_login_info()
        gu = self.loginp.get_login_result("周艳萍")
        '''在excel里边用true，false是str类，需要转换成bool'''
        if res == "True": resul = True
        else:resul = False
        assert gu == resul

    @ddt.data(*testdata)
    def test_01(self,data):
        '''输入用户名，输入密码，点击登录'''
        print("-------------------开始执行-----------------")
        print("测试数据 %s" % data)
        self.login_case(data["username"],data["pwd"],data["res"])
        print("-------------------执行结束-----------------")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()







