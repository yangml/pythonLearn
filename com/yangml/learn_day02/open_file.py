#coding=gbk
'''
Created on 2014��3��19��

@author: bling
'''
#�ı��ļ����������
#�����ļ�����
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