#coding=gbk
'''
Created on 2014��3��19��

@author: bling
'''
#��������
dic = {'tom':11,'sam':56,'jun':20,'jun':19}
print dic,type(dic)
print dic['jun']
dic['jun']=30
print dic
dic={}
print dic
dic['yangml']=10
print dic
#�ʵ�Ԫ�ص�ѭ������
dic = {'tom':11,'sam':56,'jun':20,'jun':19}
for key in dic:
    print dic[key],type(dic[key])
#�ʵ�ĳ��÷���
print dic.keys()
print dic.values()
print dic.items()
dic.clear()
print dic
dic = {'tom':11,'sam':56,'jun':20,'jun':19}
del dic['tom']
print dic,len(dic)