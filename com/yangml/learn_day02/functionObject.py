#coding=gbk
'''
Created on 2014年3月19日

@author: bling
'''
#lambda函数
func = lambda x,y:x+y
print func(1,2)
#函数作为参数传递
def test(f,a,b):
    print 'test'
    print f(a,b)
test(func,3,4)
test((lambda x,y:x**2+y),6,4)
#map()函数
re = map((lambda x:x+2), [1,2,3])
print re
re = map((lambda x,y:x**2+y),[1,2,3],[4,5,6])
print re
#filter()函数
def func1(a):
    if a>100:
        return True
    else:
        return False
print filter(func1, [10,101,120,99])
#reduce()函数
print reduce((lambda x,y:x*y), [1,2,3,4,5])