#coding=gbk
'''
Created on 2014��3��29��

@author: bling
'''
#os.path��
import os.path
path='/home/vamei/doc/file.txt'
print (os.path.basename(path))
print (os.path.dirname(path))

info = os.path.split(path)
path2 = os.path.join('/', 'home', 'vamei', 'doc', 'file1.txt')
p_list = [path, path2]
print os.path.commonprefix(p_list)
print os.path.normpath(path)
print path
'''
print(os.path.exists(path))    # ��ѯ�ļ��Ƿ����

print(os.path.getsize(path))   # ��ѯ�ļ���С
print(os.path.getatime(path))  # ��ѯ�ļ���һ�ζ�ȡ��ʱ��
print(os.path.getmtime(path))  # ��ѯ�ļ���һ���޸ĵ�ʱ��

print(os.path.isfile(path))    # ·���Ƿ�ָ�򳣹��ļ�
print(os.path.isdir(path))     # ·���Ƿ�ָ��Ŀ¼�ļ�
'''
#glob��
import glob
print glob.glob('/*')
def selectTree(currentpath,count):
    print currentpath
    if os.path.exists(currentpath):
        print 2
        return
    if os.path.isfile(currentpath):
        filename = os.path.basename(currentpath)
        print '\t'*count+'������'+filename
    elif os.path.isdir(currentpath):
        print '\t'*count+'������'+currentpath
        pathlist =  os.listdir(currentpath)
        for eachpath in pathlist:
           selectTree(currentpath+'/'+eachpath,count+1)
selectTree('/',1) 
    
