#coding:utf8
'''
Created on Oct 12, 2016

@author: Administrator
'''

from __future__ import unicode_literals

import json
from django.shortcuts import render
from django.http import HttpResponse

import hello as H
import ps_flow as pf  
    
def index(request):
    return HttpResponse('寻英大数据挖掘中……')

    
def get_hello(request):
    callback = request.GET['callback']
    key = request.GET['key']
    
    data = H.server(key)
    
    return HttpResponse('%s(%s)' % (callback, json.dumps(data)), content_type='application/json') 

def get_flow(request):
    callback = request.GET['callback']
    dateStart = request.GET['dateStart']
    dateEnd = request.GET['dateEnd']
    print 'get_flow'
    data = pf.getFlow(dateStart, dateEnd)
    
    return HttpResponse('%s(%s)' % (callback, json.dumps(data)), content_type='application/json') 



#    return HttpResponse(json.dumps(name_dict), content_type='application/json')