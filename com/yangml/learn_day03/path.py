#coding=gbk
'''
Created on 2014年3月29日

@author: bling
'''
#os.path包
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
print(os.path.exists(path))    # 查询文件是否存在

print(os.path.getsize(path))   # 查询文件大小
print(os.path.getatime(path))  # 查询文件上一次读取的时间
print(os.path.getmtime(path))  # 查询文件上一次修改的时间

print(os.path.isfile(path))    # 路径是否指向常规文件
print(os.path.isdir(path))     # 路径是否指向目录文件
'''
#glob包
import glob
print glob.glob('/*')
def selectTree(currentpath,count):
    print currentpath
    if os.path.exists(currentpath):
        print 2
        return
    if os.path.isfile(currentpath):
        filename = os.path.basename(currentpath)
        print '\t'*count+'├──'+filename
    elif os.path.isdir(currentpath):
        print '\t'*count+'├──'+currentpath
        pathlist =  os.listdir(currentpath)
        for eachpath in pathlist:
           selectTree(currentpath+'/'+eachpath,count+1)
selectTree('/',1) 
    
