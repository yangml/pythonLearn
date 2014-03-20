#coding=gbk
'''
Created on 2014年3月20日

@author: bling
'''
#异常处理
'''
re = iter(range(10))
for i in range(20):
    re.next()
print "haha"
'''
re = iter(range(10))
try:
    for i in range(20):
        print re.next()
except StopIteration:
    print 'here is end ',i
print 'haha' 
a='oo'
try:
    print(a*2)
except TypeError:
    print("TypeError")
except:
    print("Not Type Error & Error noted")
def test_func():
    try:
        1/0
    except NameError:
        print("Catch NameError in the sub-function")
try:
    test_func()
except ZeroDivisionError:
        print("Catch error in the main program")
#抛出异常
print 'Lalala'
raise StopIteration
print 'Hahaha'
raise StopIteration()
