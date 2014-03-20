#coding=gbk
'''
Created on 2014年3月20日

@author: bling
'''
#动态类型
a=3
a='ty'
print a
a = 5
b = a
a = a + 2
print a,b
L1 = [1,2,3]
L2 = L1
L1 = 1
print L1,L2
L1 = [1,2,3]
L2 = L1
L1[0] = 10
print L1,L2
#从动态类型看函数的参数传递
def f(x):
    x = 100
    print x

a = 1
f(a)
print a
def f1(x):
    x[0] = 100
    print x

a = [1,2,3]
f1(a)
print a