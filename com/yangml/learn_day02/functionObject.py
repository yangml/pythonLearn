#coding=gbk
'''
Created on 2014��3��19��

@author: bling
'''
#lambda����
func = lambda x,y:x+y
print func(1,2)
#������Ϊ��������
def test(f,a,b):
    print 'test'
    print f(a,b)
test(func,3,4)
test((lambda x,y:x**2+y),6,4)
#map()����
re = map((lambda x:x+2), [1,2,3])
print re
re = map((lambda x,y:x**2+y),[1,2,3],[4,5,6])
print re
#filter()����
def func1(a):
    if a>100:
        return True
    else:
        return False
print filter(func1, [10,101,120,99])
#reduce()����
print reduce((lambda x,y:x*y), [1,2,3,4,5])