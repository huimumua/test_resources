# -*- coding: UTF-8 -*-
#!/usr/bin/env python
import os, sys
import logging
import ctypes

Project_root_path = sys.path[0]
FOREGROUND_WHITE = 0x0007
FOREGROUND_BLUE = 0x01 # text color contains blue.
FOREGROUND_GREEN= 0x02 # text color contains green.
FOREGROUND_RED  = 0x04 # text color contains red.
FOREGROUND_YELLOW = FOREGROUND_RED | FOREGROUND_GREEN

STD_OUTPUT_HANDLE= -11
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool

class Logger:
    def __init__(self, script_name,Clevel = logging.DEBUG,Flevel = logging.DEBUG):
         self.logger = logging.getLogger(script_name)
         self.logger.setLevel(logging.DEBUG)
         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
         #设置CMD日志
         cmd_display = logging.StreamHandler()
         cmd_display.setFormatter(formatter)
         cmd_display.setLevel(Clevel)
         #设置文件日志
         log_file = logging.FileHandler(Project_root_path + os.sep + script_name, 'w', encoding="utf-8")
         log_file.setFormatter(formatter)
         log_file.setLevel(Flevel)
         self.logger.addHandler(cmd_display)
         self.logger.addHandler(log_file)
        
         
    def debug(self,message,color=FOREGROUND_BLUE):
        set_color(color)
        self.logger.debug(message)
        set_color(FOREGROUND_WHITE)
    
    def info(self,message,color=FOREGROUND_GREEN):
        set_color(color)
        self.logger.info(message)
        set_color(FOREGROUND_WHITE)
    
    def war(self,message,color=FOREGROUND_YELLOW):
        set_color(color)
        self.logger.warn(message)
        set_color(FOREGROUND_WHITE)
    
    def error(self,message,color=FOREGROUND_RED):
        set_color(color)
        self.logger.error(message)
        set_color(FOREGROUND_WHITE)
    
    def cri(self,message,color=FOREGROUND_RED):
        set_color(color)
        self.logger.critical(message)
        set_color(FOREGROUND_WHITE)
 
if __name__ == '__main__':
    log = Logger('log1111.log',logging.DEBUG,logging.WARNING)
    log.debug('debug message')
    log.cri('cri message')
    log.info('info message')
    log.war('war message')
    log.error('error message')