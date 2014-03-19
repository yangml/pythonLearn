#coding=gbk
'''
Created on 2014年3月19日

@author: bling
'''
def f(a,b,c):
    return a+b+c
print f(1,2,3)
#关键字传递
print f(a=1,b=3,c=4)
print f(1,b=9,c=1)
#参数默认值
def f1(a,b,c=10):
    return a+b+c
print f1(1, 2, 1)
print f1(1,2)
#包裹传递
def func(*name):
    print type(name)
    print name
func(2,3,4)
func(5,6,7,8,9)
def func1(**name):
    print type(name)
    print name
func1(a=4,b=6,v=7)
func1(d=4,t=9,g=0)
#解包裹
def func2(a,b,c):
    print a+b+c
arg = (2,3,4)
func2(*arg)
dict = {'a':1,'b':2,'c':3}
func2(**dict)