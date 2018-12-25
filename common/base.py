from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class Base():

    def __init__(self,driver):
        self.driver = driver
        self.timeout=10
        self.t=0.5

    def findElement(self, locator):
        if not isinstance(locator,tuple):
            print('locator格式不对，应传入元祖：("xxx","xxx")')
        else:
            ele = WebDriverWait(self.driver, self.timeout,self.t).until(lambda x: x.find_element(*locator))
            return ele

    def findElement2(self, locator):
        '''定位到元素，则返回元素对象，没定位到，则返回timeout异常'''
        ele = WebDriverWait(self.driver, self.timeout,self.t).until(EC.presence_of_element_located(locator))
        return ele

    def findElements(self, locator):
        ele = WebDriverWait(self.driver, self.timeout,self.t).until(lambda x: x.find_elements(*locator))
        return ele

    def sendKeys(self,locator,value,is_clear_first = False):
        ele = self.findElement(locator)
        if is_clear_first:
            ele.clear()
        ele.send_keys(value)

    def move_to_element(self,locator):
        '''鼠标悬停操作'''
        ele = self.findElement(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    def click(self,locator):
        ele = self.findElement(locator)
        ele.click()

    def clear(self,locator):
        ele = self.findElement(locator)
        ele.clear()

    def isSelected(self,locator):
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r

    def select_by_index(self,locator,index=0):
        '''通过索引查找，从0开始，默认选择第一个'''
        ele = self.findElement(locator)
        Select(ele).select_by_index(index)

    def select_by_value(self,locator,value):
        '''通过value值查找'''
        ele = self.findElement(locator)
        Select(ele).select_by_value(value)

    def select_by_text(self,locator,text):
        '''通过文本属性查找'''
        ele = self.findElement(locator)
        Select(ele).select_by_visible_text(text)

    def js_focus_element(self, locator):
        '''聚焦元素'''
        ele = self.findElement(locator)
        driver.execute_script('arguments[0].scrollIntoView();', ele)

    def js_scroll_top(self):
        '''滑到页面顶部'''
        js = "window.scrollTo(0,0)"
        driver.execute_script(js)

    def js_scroll_end(self, d):
        '''滑到页面底部'''
        js = "window.scrollTo(%d,document.body.scrollHeight)" % d
        driver.execute_script(js)

    def isElementExist(self,locator):
        try:
            self.findElement(locator)
            return True
        except:
            return False

    def isElementExist2(self,locator):
        ele = self.findElements(locator)
        n = len(ele)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            print("定位到的元素个数为：%d" %n)
            return True

    def is_title(self, _text):
        try:
            ele = WebDriverWait(self.driver, self.timeout,self.t).until(EC.title_is(_text))
            return ele
        except:
            return False

    def is_title_contains(self, _text):
        try:
            ele = WebDriverWait(self.driver, self.timeout,self.t).until(EC.title_contains(_text))
            return ele
        except:
            return False

    def is_text_present_in_element(self,locator, _text):
        try:
            ele = WebDriverWait(self.driver, self.timeout,self.t).until(EC.text_to_be_present_in_element(locator, _text))
            return ele
        except:
            return False

    def is_value_present_in_element(self,locator, value):
        '''返回布尔值，value为空也返回false'''
        try:
            ele = WebDriverWait(self.driver, self.timeout,self.t).until(EC.text_to_be_present_in_element_value(locator, value))
            return ele
        except:
            return False

    def is_alert_present(self):
        '''判断是否有alert'''
        try:
            ele = WebDriverWait(self.driver, self.timeout,self.t).until(EC.alert_is_present())
            return ele
        except:
            return False

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get('http://10.155.20.210/pms/index.php?m=user&f=login')
    dr = Base(driver)
    # loc1 =(By.ID,"account")
    # loc2 =(By.NAME,"password")
    # loc3 =(By.ID,"submit")
    loc1 = ("id","account")
    loc2 = ("name","password")
    loc3 = ("id","submit")

    dr.sendKeys(loc1,"zhouyanping")
    dr.sendKeys(loc2,"zhouyanping")
    dr.clear(loc2)

    # dr.click(loc3)