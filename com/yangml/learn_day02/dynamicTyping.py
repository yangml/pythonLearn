#coding=gbk
'''
Created on 2014��3��20��

@author: bling
'''
#��̬����
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
#�Ӷ�̬���Ϳ������Ĳ�������
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