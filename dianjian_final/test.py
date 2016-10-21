'''
Created on Oct 19, 2016

@author: Administrator
'''
class Obj(object):
    pass
def main():
    ls = []
    line = ['12', 23]
    ls.append(line)
    line = ['1212', 3]
    ls.append(line)
    
    print ls
#    list=["a", "b", "c"]
##    for i in range(1,len(list),2):
##        Obj = type('Obj',(),{list[i]:lambda self,s:obj.__setattr__(s.split(" = ")[0],s.split(" = ")[1])})
#   
#    obj = Obj()
##    for i in range(0,len(list),2):
##        obj.__setattr__(list[i],list[i])   
#       
#   
#    obj.a = 1
##    obj.b("a = 2")
##    obj.b("c = 3")
#    obj.c = 5
#    obj.d = 12
#    print obj.a
#    print obj.c
#    print obj.d
    
if __name__ == '__main__':
    main()