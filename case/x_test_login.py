#coding:utf-8
from selenium import webdriver
import time
import unittest

class LoginTest(unittest.TestCase):
    '''登录用例'''

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def setUp(self):
        self.driver.get('http://10.155.20.210/pms/index.php?m=user&f=login')

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()

    def get_login_info(self):
        try:
            te = self.driver.find_element_by_xpath('//*[@id="userMenu"]/a').text
            return te
        except:
            return ""

    def is_exist_alert(self):
        try:
            time.sleep(2)
            al = self.driver.switch_to.alert();
            text = al.text
            print (al)
            al.accept()
        except:
            pass

    def test01(self):
        '''登录成功用例'''
        time.sleep(2)
        self.driver.find_element_by_id('account').send_keys('zhouyanping')
        self.driver.find_element_by_name('password').send_keys('zhouyanping')
        self.driver.find_element_by_id('submit').click()
        time.sleep(2)
        t = self.get_login_info()
        print("正确的结果为%s" %t)
        self.assertTrue(t == '周艳萍')

    def test02(self):
        '''登录失败用例'''
        time.sleep(2)
        #输入错误的用户名密码
        self.driver.find_element_by_id('account').send_keys('zhouyanping')
        self.driver.find_element_by_name('password').send_keys('12345678')
        self.driver.find_element_by_id('submit').click()
        time.sleep(2)
        t = self.get_login_info()
        print("错误的结果为%s" %t)
        self.assertTrue(t == "")

    def tearDown(self):
        self.is_exist_alert()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
