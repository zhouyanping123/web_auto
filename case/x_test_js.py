#coding:utf-8
from selenium import webdriver
from pages.login_page import LoginPage
import time

driver = webdriver.Chrome()
ad = LoginPage(driver)
driver.get("http://10.155.20.210/pms/index.php?m=user&f=login")
driver.maximize_window()

# ad.login()
js = 'document.getElementsByName("account")[0].value="zhouyanping";' \
     'document.getElementsByName("password")[0].value="zhouyanping"'
driver.execute_script(js)

time.sleep(2)

jq = '$("#keepLoginon").click();' \
     '$("#submit").click()'
driver.execute_script(jq)

# test = ("xpath","//*[@id='mainmenu']/ul/li[4]/a")
# bugger = ("xpath",'//*[@id="modulemenu"]/ul/li[2]/a')
# newbugger = ("xpath","//*[@id='featurebar']/div[1]/div[2]/a[2]")
# ad.click(test)
# ad.click(bugger)
# ad.click(newbugger)
#
# j = "hello，world！"
# js = 'document.getElementsByClassName("ke-edit-iframe")[0].contentWindow.document.body.innerHTML="%s"' %j
# driver.execute_script(js)