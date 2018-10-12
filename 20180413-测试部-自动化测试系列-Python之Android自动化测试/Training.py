from appium import webdriver
from logpy import Logger
from win32com.client import Dispatch
import os, sys, time, logging

Project_root_path = sys.path[0]

log = Logger('call.log',Clevel = logging.DEBUG, Flevel = logging.DEBUG)

autoWindow = None
#initial QXDM instance
def Initialize():
    log.info('Initialize QXDM instance and return its automation window')
    qxdm_instance = Dispatch("QXDM.QXDMAutoApplication") 
 
    if not bool(qxdm_instance):
        log.debug("Unable to obtain ISF interface")
    else:
        autoWindow = qxdm_instance.GetAutomationWindow()
    log.info("Initialize QXDM instance succeeded...")
    return autoWindow
 
def Excute(iteration = 1):
    autoWindow = Initialize()
    appVer = autoWindow.AppVersion
    log.info(appVer)
    handle = autoWindow.LoadConfig(r'C:\Users\lcfyujianwen\Desktop\default_dmc.dmc')#load DMC
    if handle == 0:
        log.debug('Unable to load the dmc file')
        return False
    else:
        log.info('load the dmc file succeed...')
    portNumber = input("Please input COMPort Number:")
    reVar = autoWindow.SetComPort(portNumber)
    if reVar is False:
        log.debug('Fail to connect port COM %s'%portNumber)
        return False
    else:
        log.info('Connected to port COM %s'%portNumber)

    for i in range(1, iteration+1):
        MO_Call(i)
        time.sleep(10)
        res = autoWindow.SaveItemStore(Project_root_path + '\\isf_log\\Iteration_%d.isf'%(i))
        log.info("Save item store result: %s"%res)
        time.sleep(3)
    autoWindow.QuitApplication()
    log.info("Quit QXDM Application...")
       
def MO_Call(i):
    time.sleep(1)
    driver.find_element_by_id("com.zui.contacts:id/one").click()#id定位
    driver.find_element_by_android_uiautomator('new UiSelector().description("八")').click()#content-desc定位
    driver.find_elements_by_class_name('android.widget.ImageButton')[5].click()#class定位
    #     driver.find_element_by_id("com.zui.contacts:id/six").click()
    driver.find_element_by_id("com.zui.contacts:id/eight").click()
    driver.find_element_by_id("com.zui.contacts:id/three").click()
    driver.find_element_by_id("com.zui.contacts:id/seven").click()
    driver.find_element_by_id("com.zui.contacts:id/nine").click()
    driver.find_element_by_id("com.zui.contacts:id/three").click()
    driver.find_element_by_id("com.zui.contacts:id/nine").click()
    driver.find_element_by_id("com.zui.contacts:id/eight").click()
    driver.find_element_by_id("com.zui.contacts:id/seven").click()
    driver.find_element_by_id("com.zui.contacts:id/call_sim_single").click()
    time.sleep(20)
    try:
        if driver.find_element_by_android_uiautomator('new UiSelector().description("挂断")') != None :
            driver.find_element_by_android_uiautomator('new UiSelector().description("挂断")').click()#content-desc定位
            log.info('Call Success: %d'%i)
    except:
        log.cri("Call Fail: %d"%i)

if __name__ == '__main__':
    desired_caps = {
            'platformName': 'Android',
            'deviceName': 'MOTO',
            'platformVersion': '7.1.1',
            'udid':'N52C150503',
#                 'app': Project_root_path + '\\apk\\mukewang.apk', 
            'appPackage': 'com.zui.contacts',
            'appActivity': 'com.android.newcontact.vl.activity.DialpadShutcut',
            'noReset': True, # 不需要每次都安装apk 
            'unicodeKeyboard': True, #使用unicode编码方式发送字符串
            'resetKeyboard': True #将键盘隐藏起来 
            } 
#更多Desired Capabilities参考网址：https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    Excute(2)
    driver.quit()