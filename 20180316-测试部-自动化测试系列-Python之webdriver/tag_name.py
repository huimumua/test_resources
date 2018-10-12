# coding=utf-8  
  
from selenium import webdriver  
  
driver = webdriver.Firefox()  
driver.maximize_window()  
driver.implicitly_wait(6)  
  
driver.get("https://www.baidu.com")  
try:  
    driver.find_element_by_tag_name("form")  
    print ('test pass: tag name found')  
except Exception as e:  
    print ("Exception found", format(e))  
  
driver.quit()  