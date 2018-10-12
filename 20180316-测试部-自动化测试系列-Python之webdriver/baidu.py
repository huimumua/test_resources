# coding = utf-8 
from selenium import webdriver 
import time

browser = webdriver.Firefox() 
browser.get("http://www.baidu.com")
time.sleep(1) 
browser.find_element_by_id("kw").send_keys('harry') 
time.sleep(1)
browser.find_element_by_id("su").click() 
time.sleep(10)
browser.quit()
