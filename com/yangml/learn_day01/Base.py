#coding=gbk
'''
基本数据类型
'''
print "hello world"
a = 10
print a,type(a)
a = 'hell'
print a,type(a)
a = 1.333
print a,type(a)
a = True
print a,type(a)
'''
sequence序列
'''
s1=(2,4,2,'love',0,2,3,7,False)
print s1,type(s1)
s2=[True,5,'smile']
print s2,type(s2)
s3=[1,[3,5,'other']]
print s3,type(s3)
s4=(1,(3,5,'other'))
print s4,type(s4)
print s1[0]
print s2[2]
print s3[1][2]
s2[2]='fail'
print s2
print s1[:5]
print s1[2:]
print s1[0:5:2]
print s1[2:0:-1]
print s1[-1]
print s1[-3]
str ='qwweerttyyy'
print str[2:4],type(str)
print 1+9
print 9.22-0.22
print 400/200
print 2*3.333
print 3**2
print 10%3
print 5==6
print 8.0!=8.0
print 4>6,4>0
print 3<4,3>0
print 5 in s1
print True and False,True and True,False and False
print False or True
print not True
print 5>=0 and 5<6
