#coding=gbk
'''
Created on 2014年3月18日

@author: bling
'''
#缩进
i=10
if i>0:
    x=1
    y=2
    print x,'==========',y
#if语句
if i>0:
    x = x+1
print x
i=1
if i>0:
    print 'positive i'
    i = i+1
elif i==0:
    print 'i is 0'
else:
    print 'negative i'
    i = i-1
print 'new i:',i
#-----------------
i  = 5
if i > 1:
    print 'i bigger than 1'
    print 'good'
    if i > 2:
        print 'i bigger than 2'
        print 'even better'
#for
s1 = [1,2,3,4,'for']
for a in s1:
    print a
idx = range(5)
print idx
for a in range(5):
    print a**2
#while
i=0
while i<10:
    print i
    i = i+1
#中断循环
for i in range(8):
    if i==5:
        continue
    print i
for i in range(8):
    if i==5:
        break
    print i