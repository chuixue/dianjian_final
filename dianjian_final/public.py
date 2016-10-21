#coding:utf8

'''
Created on Oct 19, 2016

@author: Administrator
'''
import datetime

class TMFT():
    pass

def timeFliter(dateStart, dateEnd):
    data = TMFT()
    
    if None==dateStart and None==dateEnd:
        data.start = datetime.datetime(2015, 1, 1)
        data.end = datetime.datetime.now()
        return data
#        return {'start':datetime.datetime(2015, 1, 1), 'end':datetime.datetime.now()}
    tps = dateStart.split('-')
    tpe = dateEnd.split('-')
    data.start = datetime.datetime(int(tps[0]), int(tps[1]), int(tps[2]))
    data.end = datetime.datetime(int(tpe[0]), int(tpe[1]), int(tpe[2]))
    return data

def DateF(_dt):
    if _dt==None: _dt = datetime.datetime.now()
    return "{}-{}-{} {}:{}:{}".format(_dt.year, _dt.month, _dt.day,
                                      _dt.hour, _dt.minute, _dt.second)
    
def TimeF(_dt):
    if _dt==None: _dt = datetime.datetime.now()
    return "{}:{}:{}".format(_dt.hour, _dt.minute, _dt.second)

def _TimeF(_dt):
    if _dt==None: _dt = datetime.datetime.now()
    return "{}:{}".format(_dt.hour, _dt.minute)
    
if __name__ == '__main__':
#    timeFliter(None, None)
    print DateF(None)
    pass

