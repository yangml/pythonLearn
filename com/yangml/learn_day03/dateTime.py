#coding=gbk
'''
Created on 2014��3��23��

@author: bling
'''
#time��
import time
print ('start')
time.sleep(1)
print ('wake up')
st = time.gmtime()
print st
st = time.localtime()
print st
s = time.mktime(st)
print s
#datetime��
import datetime
t = datetime.datetime(2014,03,23,16,23,45)
print t
#2) ����
t      = datetime.datetime(2012,9,3,21,30)
t_next = datetime.datetime(2012,9,5,23,30)
delta1 = datetime.timedelta(seconds = 600)
delta2 = datetime.timedelta(weeks = 3)
print(t + delta1)
print(t + delta2)
print(t_next - t)
print(t>t_next)
#3) datetime�������ַ���ת��
from datetime import datetime
format = "output-%Y-%m-%d-%H%M%S.txt"
str = "output-1997-12-23-030000.txt"
t = datetime.strptime(str,format)
print t