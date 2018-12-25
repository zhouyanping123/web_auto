from common.base import Base
from selenium import webdriver

login_url = "http://10.155.20.210/pms/index.php?m=user&f=login"

class LoginPage(Base):
    #登录
    loc_user = ("xpath", "//*[@id='account']")
    loc_pwd = ("xpath", "//*[@id='login-form']/form/table/tbody/tr[2]/td/input")
    loc_button = ("xpath", "//*[@id='submit']")
    loc_keep_login = ("id", "keepLoginon")
    loc_forget_pwd = ("link text", "忘记密码")

    loc_get_user = ("xpath",'//*[@id="userMenu"]/a')

    loc_refresh = ("xpath","/html/body/div/p/a")

    def input_user(self, username):
        self.sendKeys(self.loc_user, username)

    def input_pwd(self, pwd):
        self.sendKeys(self.loc_pwd, pwd)

    def click_login_button(self):
        self.click(self.loc_button)

    def click_keep_login(self):
        self.click(self.loc_keep_login)

    def click_forget_pwd(self):
        self.click(self.loc_forget_pwd)

    def is_exist_alert(self):
        al = self.is_alert_present()
        if al:
            al.accept()

    def get_login_info(self):
        try:
            ele = self.findElement(self.loc_get_user).text
            return ele
        except:
            return ""

    def get_login_result(self,text):
        res = self.is_text_present_in_element(self.loc_get_user,text)
        return res

    def get_element(self):
        try:
            ele = self.findElement(self.loc_refresh).text
            return ele
        except:
            return ""

    #登录函数
    def login(self,username='zhouyanping', pwd="zhouyanping",keeplogin = False):
        # self.driver.get(login_url)
        # self.driver.maximize_window()
        self.input_user(username)
        self.input_pwd(pwd)
        if keeplogin:self.click_keep_login()
        self.click_login_button()
        # self.sendKeys(self.loc1,username)
        # self.sendKeys(self.loc2,pwd)
        # self.click(self.loc3)

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get(login_url)
    # driver.maximize_window()
    ad = LoginPage(driver)
    ad.login(keeplogin=True)
    # ad.input_user("zhouyanping")
    # ad.input_pwd("zhouyanping")
    # ad.click_login_button()
    # ele = ad.get_login_info()
    # print(ele)