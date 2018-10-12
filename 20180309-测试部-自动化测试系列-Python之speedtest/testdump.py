from selenium import webdriver
from time import sleep
from selenium.common.exceptions import TimeoutException
import serial.tools.list_ports
import unittest
import os
import time


class Testdump(unittest.TestCase):
    def setUp(self):
        print('测试前，请确保QPST已打开')
    def tearDown(self):
        print('dum测试结束')
    def test_dump(self):
        driver = webdriver.Firefox()
        driver.get("http://beta.speedtest.net/#")
        run_times= 0
        dump_times = 1
        for i in range(100):
            try:
                sleep(1)
                element = driver.find_element_by_class_name("js-start-test")
            except:
                pass
            else:
                try:
                    if element.is_displayed():
                        element.click()
                        run_times = run_times + 1
                        print(run_times)
                        sleep(45)
                        if run_times%5==0:
                            os.system('adb reboot')
                            sleep(55)
                            continue
                    else:
                        driver.get("http://beta.speedtest.net/#")
                        continue
                except TimeoutException:
                    print("超时")
                    driver.get("http://beta.speedtest.net/#")
                    continue
                except Exception:
                    print("异常")
                    driver.get("http://beta.speedtest.net/#")
                    continue
            finally:
                    port_list = list(serial.tools.list_ports.comports())
                    if len(port_list) ==0:
                        print('找不到串口测试结束')
                        break
                    else:
                        com1 = list(list(port_list)[0])[0]
                        com2 = list(list(port_list)[1])[0]
                        file1= os.path.exists("C:\ProgramData\Qualcomm\QPST\Sahara\Port_%s"%com1)
                        file2 = os.path.exists("C:\ProgramData\Qualcomm\QPST\Sahara\Port_%s"%com2)
                        if file1 or file2:
                            os.chdir(r'C:\ProgramData\Qualcomm\QPST\Sahara')
                            sleep(20)
                            try:
                                os.rename('Port_%s'%com1, time.strftime('%Y-%m-%d %H_%M_%S')+'设备第%ddump'%dump_times)
                                dump_times = dump_times + 1
                            except:
                                os.rename('Port_%s'%com2, time.strftime('%Y-%m-%d %H_%M_%S')+'设备第%ddump'%dump_times)
                                dump_times = dump_times + 1
                            print("设备dump")
                            # raise Exception('设备异常')
                        else:
                            print("设备正常")

if __name__ =='__main__':
    unittest.main()





