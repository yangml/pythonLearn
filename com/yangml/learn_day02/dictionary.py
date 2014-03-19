#coding=gbk
'''
Created on 2014年3月19日

@author: bling
'''
#基本概念
dic = {'tom':11,'sam':56,'jun':20,'jun':19}
print dic,type(dic)
print dic['jun']
dic['jun']=30
print dic
dic={}
print dic
dic['yangml']=10
print dic
#词典元素的循环调用
dic = {'tom':11,'sam':56,'jun':20,'jun':19}
for key in dic:
    print dic[key],type(dic[key])
#词典的常用方法
print dic.keys()
print dic.values()
print dic.items()
dic.clear()
print dic
dic = {'tom':11,'sam':56,'jun':20,'jun':19}
del dic['tom']
print dic,len(dic)