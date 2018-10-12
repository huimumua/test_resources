#!/usr/bin/python
# _*_ coding:utf8 _*_

from selenium import webdriver as wd
import time

a=wd.Firefox()
a.get('https://10.8.6.221:443')
time.sleep(3)
a.find_element_by_id('username').send_keys('admin')
a.find_element_by_id('password').send_keys('1111')
a.find_element_by_id('login-btn').click()
time.sleep(8)
a.find_element_by_id('advanced').click()
time.sleep(3)
a.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[4]/div[1]/ul/li[5]/a').click()
time.sleep(3)
for i in range(1,129):
    a.find_element_by_id('addBtn').click()
    a.find_element_by_id('service_name').send_keys('%d' %i)
    a.find_element_by_id('port_range').send_keys('%d' %i)
    a.find_element_by_id('local_port').send_keys('%d' %i)
    a.find_element_by_id('local_ip').send_keys('192.168.1.22')
    a.find_element_by_id('confirm').click()
    time.sleep(1)
a.find_element_by_id('apply').click()
