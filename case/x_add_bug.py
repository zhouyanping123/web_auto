from common.base import Base
from selenium import webdriver
import time

class AddBug(Base):
    #登录
    loc1 = ("xpath","//*[@id='account']")
    loc2 = ("xpath","//*[@id='login-form']/form/table/tbody/tr[2]/td/input")
    loc3 = ("xpath","//*[@id='submit']")

    #添加bug
    test = ("xpath","//*[@id='mainmenu']/ul/li[4]/a")
    bugger = ("xpath",'//*[@id="modulemenu"]/ul/li[2]/a')
    newbugger = ("xpath","//*[@id='featurebar']/div[1]/div[2]/a[2]")
    influenceversion = ("xpath","//*[@id='openedBuild_chosen']/ul")
    ivchosen = ("xpath",'//*[@id="openedBuild_chosen"]/div')
    chosensingle = ("xpath","//*[@id='assignedTo_chosen']/a")
    cschosen = ("xpath",'//*[@id="assignedTo_chosen"]/div/ul/li[1]')
    title = ("id","title") #Bug标题
    ifr = ("class name","ke-edit-iframe") #富文本框
    body = ("tag name", "body")  #重现步骤
    button = ("id","submit")

    #检查是否添加
    newtitle = ("xpath","//*[@id='bugList']/tbody/tr[1]/td[4]/a")

    #登录函数
    def login(self,username='zhouyanping', pwd="zhouyanping"):
        self.sendKeys(self.loc1,username)
        self.sendKeys(self.loc2,pwd)
        self.click(self.loc3)

    #添加bug
    def addbug(self, title, content):
        self.click(self.test)
        time.sleep(3)
        self.click(self.bugger)
        self.click(self.newbugger)
        self.click(self.influenceversion)
        # time.sleep(2)
        self.click(self.ivchosen)
        self.click(self.chosensingle)
        # time.sleep(2)
        self.click(self.cschosen)
        self.sendKeys(self.title,title)
        #切换到iframe
        frame = self.findElement(self.ifr)
        self.driver.switch_to.frame(frame)
        # time.sleep(2)
        self.clear(self.body)
        self.sendKeys(self.body, content)
        #切回正常
        self.driver.switch_to.default_content()
        self.click(self.button)

    def is_add_success(self,title):
        res = self.is_text_present_in_element(self.newtitle,title)
        return res

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://10.155.20.210/pms/index.php?m=user&f=login")
    ad = AddBug(driver)
    ad.login()
    t = time.strftime("%Y-%m-%d %H:%M:%S")
    title = "我是标题"+t
    content = '''
       [步骤]111
       [结果]111
       [期望]111
       '''
    ad.addbug(title,content)
    res = ad.is_add_success(title)
    assert res == True







