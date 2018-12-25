from selenium import webdriver
import unittest
from pages.login_page import LoginPage,login_url
from pages.add_bug_page import AddBugPage
import time

my = 'http://10.155.20.210/pms/index.php?m=my&f=index'

class AddBugCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(login_url)
        cls.driver.maximize_window()
        lp = LoginPage(cls.driver)
        lp.login()
        cls.ad = AddBugPage(cls.driver)

    def setUp(self):
        self.driver.get(my)

    def test_add_bug(self):
        t = time.strftime("%Y-%m-%d %H:%M:%S")
        title = "我是标题"+t
        content = '''
           [步骤]111
           [结果]111
           [期望]111
           '''
        self.ad.addbug(title,content)
        res = self.ad.is_add_success(title)
        assert res == True

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()