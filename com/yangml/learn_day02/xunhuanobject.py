#coding=gbk
'''
Created on 2014年3月19日

@author: bling
'''
#什么是循环对象
f = open("test.txt","r")
for line in f:
    print line
#生成器
def gen():
    a=100
    yield a
    a = a*8
    yield a
    yield 1000
for i in gen():
    print i
def gen1():
    for i in range(10):
        yield i
for i in gen1():
    print i
G = (x for x in range(4))
for i in G:
    print i
#表推导
L=[]
for i in range(10):
    L.append(i**2)
print L
L = [x**2 for x in range(10)]
print L
xl = [1,3,5]
yl = [9,12,13]
L  = [ x**2 for (x,y) in zip(xl,yl) if y > 10]
print L
