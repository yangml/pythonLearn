#coding=gbk
'''
Created on 2014年4月7日

@author: bling
'''
'''
#1) 将内存中的对象转换成为文本流：
import pickle
# define class
class Bird(object):
    hava_feather = True
    way_of_reproduction = 'egg'
summer = Bird() # construct an object
pickelstring = pickle.dumps(object) # serialize object
'''
import pickle
# define class
class Bird(object):
    have_feather = True
    way_of_reproduction  = 'egg'

summer       = Bird()                        # construct an object
fn           = 'a.pkl'
with open(fn, 'w') as f:                     # open file with write-mode
    picklestring = pickle.dump(summer, f)   # serialize and save object
