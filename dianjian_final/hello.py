#coding:utf8
'''
Created on Mar 16, 2016

@author: Administrator
'''
import datetime
import json
import database



def server(key):
    data = {'username':'lucy', 'message':'Hello World', 'key':key}
    return json.dumps(data)




def test():
    db = database.Database()
    tbName = "md_flow"
    sql = "select * from {}".format(tbName)
    
#    for item in db.select(sql):pass
    
    print db.getKeys(tbName)

    
dt = datetime.datetime.now()
test()
print datetime.datetime.now(), datetime.datetime.now()-dt



