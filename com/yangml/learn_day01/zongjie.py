#coding=gbk
'''
Created on 2014年3月18日

@author: bling
'''
print dir(list)
print help(list)
n = [1,2,5,3,5]
print n.count(5)
print n.index(3,);
print n.append(6);
print n
print n.sort()
print n
print n.pop()
print n
n.remove(2)
print n
n.insert(0, 9)
print n
#运算符是特殊方法
print dir(tuple)
print help(tuple)
print [1,2,3]+[4,5,6]
#print [1,2,3]-[3,4]
class superList(list):
    def __sub__(self,b):
        a = self[:]
        b = b[:]
        while len(b)>0:
            element_b = b.pop()
            if element_b in a:
                a.remove(element_b)
        return a
print superList([1,2,3])-superList([3,4])