#coding:utf8
'''
Created on Oct 13, 2016

@author: Administrator
'''
import config as CFG
import mysql.connector

def cout(ls):
    for l in ls: print l, ':', ls[l],
    print
def out(ls):
    for l in ls: print l,
    print

class Database(object):
    ''' for query data in only one code '''

    def __init__(self):
        self.cfg = CFG.Config()
        self.lsConn = []
        self.lsCurs = []
        
        
    def selectEx(self, sql):
        return self.select(sql).fetchall()
    
    def select(self, sql):
        cnx = mysql.connector.connect(user=self.cfg.dbuser, password=self.cfg.dbpasswd, database=self.cfg.dbname)
        cursor = cnx.cursor()
        self.lsConn.append(cnx)
        self.lsCurs.append(cursor)
        cursor.execute(sql)
        return cursor
    def getKeys(self, tbName):
        return [info[0] for info in self.select("SHOW FULL COLUMNS FROM {}".format(tbName))]

    def __del__(self):  
        try:
            for i in range(0, len(self.lsConn)):
                self.lsCurs[i].close()
                self.lsConn[i].close()
        except:
            pass

if __name__ == '__main__':
    db = Database()
    print db.getKeys("md_flow")

