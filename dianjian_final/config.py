#coding:utf8
'''
Created on Oct 13, 2016

@author: Administrator
'''


class Config(object):
    def __init__(self):
        self.dbhost = "192.168.3.177"
        self.dbuser = "root"
        self.dbpasswd = "root"
        self.dbname = "dianjian"
        self.dbport = "3306"
        
    def __del__(self):  
        pass