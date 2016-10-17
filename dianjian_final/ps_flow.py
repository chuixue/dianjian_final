#coding:utf8
'''
Created on Oct 13, 2016

@author: Administrator
'''
import datetime
import json
import database
import random

def getFlow(dateStart, dateEnd):
    db = database.Database()
    tbName = "md_flow"
    tps = dateStart.split('-')
    tpe = dateEnd.split('-')
    dateStart = datetime.datetime(int(tps[0]), int(tps[1]), int(tps[2]))
    dateEnd = datetime.datetime(int(tpe[0]), int(tpe[1]), int(tpe[2]))
    #sql = "select personId, count(*) from {} group by ".format(tbName)
    #sql = "select sTime, count(*) from {} group by personId".format(tbName)
    #sqlw = "select weekday(sTime), count(*) from {} group by weekday(sTime)".format(tbName)
    #print db.getKeys(tbName); return
    sql = "select personId, sTime, tTime, source, target from {} where sTime >= '{}' and sTime<'{}'".format(tbName,
                          dateStart, dateEnd)
    count = 0
    units = {}
    persons = {}
    lsUnit = {}
    print sql
    for u in db.select("select name from md_unit"): units[u[0]] = 1
    for personId, unit in db.select("select personId, unit from md_person"): 
        if unit in units: persons[personId] = unit
    
    data = {}
    for (personId, sTime, tTime, source, target) in db.select(sql):
        if personId not in persons: continue
        wd = sTime.weekday()
        sh = sTime.hour
        #unit = lsUnit[random.randint(0, len(lsUnit)-1)]
        unit = persons[personId]
        if wd not in data: data[wd] = {}
        if sh not in data[wd]: data[wd][sh] = {}
        if unit not in data[wd][sh]: data[wd][sh][unit] = {source:0, target:0}
        data[wd][sh][unit][source] += 1
        
    return {'data':data}



if __name__ == '__main__':
    dt = datetime.datetime.now()

    getFlow()
    
    print datetime.datetime.now(), datetime.datetime.now()-dt
    