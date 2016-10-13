#coding:utf8
'''
Created on Oct 13, 2016

@author: Administrator
'''
import datetime
import json
import database
import random

def getFlow():
    db = database.Database()
    tbName = "md_flow"
    #sql = "select personId, count(*) from {} group by ".format(tbName)
    #sql = "select sTime, count(*) from {} group by personId".format(tbName)
    sql = "select personId, sTime, tTime, source, target from {} ".format(tbName)
    
#    print db.getKeys(tbName); return
    
    count = 0
    data = {}
#    src = {}
#    tgt = {}
    lsUnit = ["部门A", "部门B", "部门C", "部门D"]
    for (personId, sTime, tTime, source, target) in db.select(sql):
        wd = sTime.weekday()
        sh = sTime.hour
        unit = lsUnit[random.randint(0, len(lsUnit)-1)]
        
        if wd not in data: data[wd] = {}
        if sh not in data[wd]: data[wd][sh] = {}
        if unit not in data[wd][sh]: data[wd][sh][unit] = {source:0, target:0}
        data[wd][sh][unit][source] += 1
        
    
#        print sh 
#        ls[source] = 
        
#        print personId 
        pass
#        print item
#        count+=item[1]
#    print count
    return data

if __name__ == '__main__':
    dt = datetime.datetime.now()

    getFlow()
    
    print datetime.datetime.now(), datetime.datetime.now()-dt
    