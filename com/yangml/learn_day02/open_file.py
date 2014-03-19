#coding=gbk
'''
Created on 2014年3月19日

@author: bling
'''
#文本文件的输入输出
#创建文件对象
f = open("test.txt","r")
#content = f.read(1024)
#print content,'1'
#content = f.readline()
#print content,'2'
#print f.next()
content = f.readline()
f.close()
print content
ff = open("write.txt","w")
ff.write(content)
ff.close()