#coding:utf8
'''
Created on Oct 18, 2016

@author: Administrator
'''
import datetime
import json
import database
import random
import public as P

def getClock(_dateStart, _dateEnd):
    db = database.Database()
    tbName = "md_attendance"
    dtf = P.timeFliter("2015-11-01", "2015-12-01")
    
    #print db.getKeys(tbName); return
    #[u'personId', u'source', u'target', u'sTime', u'tTime', u'updateTime', u'mark']
    
    
    sql = "select personId, onTime, offTime, onPlace, offPlace from {} where onTime >= '{}' and onTime<'{}'".format(tbName,
                          dtf.start, dtf.end)
#    count = 0
    units = {}
    persons = {}
#    lsUnit = {}
    data = []
    for u in db.select("select name from md_unit"): units[u[0]] = 1
    
    
    for personId, unit in db.select("select personId, unit from {}".format("md_person")):         
        persons[personId] = unit if unit in units else "其他"
        if unit in units: persons[personId] = unit
    
    for (personId, onTime, offTime, onPlace, offPlace) in db.select(sql):
        if personId not in persons: continue
        line1 = [personId, P.DateF(onTime), onPlace]
        line2 = [personId, P.DateF(offTime), offPlace]
#        print line1
        data.append(line1)
        data.append(line2)
        
        #wd = sTime.weekday()
        #sh = sTime.hour
    print len(data)
    return data 
        
#    for (personId, sTime, tTime, source, target) in db.select(sql):
#        if personId not in persons: continue
#        wd = sTime.weekday()
#        sh = sTime.hour
#        #unit = lsUnit[random.randint(0, len(lsUnit)-1)]
#        unit = persons[personId]
#        if wd not in data: data[wd] = {}
#        if sh not in data[wd]: data[wd][sh] = {}
#        if unit not in data[wd][sh]: data[wd][sh][unit] = {source:0, target:0}
#        data[wd][sh][unit][source] += 1
        
#    return {'data':data}


if __name__ == '__main__':
    dt = datetime.datetime.now()

    getClock(None, None)
    
    print datetime.datetime.now(), datetime.datetime.now()-dt