#coding=gbk
'''
Created on 2014��3��18��

@author: bling
'''
#���庯��
def square_sum(a,b):
    c = a**2+b**2
    return c
print square_sum(2,5)

a = 10
def change_integer(a):
    a = a + 1
    return a

print change_integer(a)
print a,type(a)

b = [1,2,3]
def change_list(b):
    b[0] = b[0]+3
    return b
print change_list(b)
print b,type(b)
year = 2001
def checked_year(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        print year,"������"
    else:
        print year,"��������"
    return "suceess"
print checked_year(year)