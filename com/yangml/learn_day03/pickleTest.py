#coding=gbk
'''
Created on 2014��4��7��

@author: bling
'''
'''
#1) ���ڴ��еĶ���ת����Ϊ�ı�����
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
