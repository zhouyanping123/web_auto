from selenium import webdriver
import time
import unittest
from case.x_add_bug import AddBug


class AddBugTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.ad = AddBug(cls.driver)
        cls.driver.get("http://10.155.20.210/pms/index.php?m=user&f=login")
        cls.driver.maximize_window()

    def test_add_bug(self):
        self.ad.login()
        t= time.strftime("%Y-%m-%d %H:%M:%S")
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
        time.sleep(2)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
