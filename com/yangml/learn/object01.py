#coding=gbk
'''
Created on 2014年3月18日

@author: bling
'''
from __builtin__ import range
class Bird1(object):
    hava_feather = True
    way_of_reproduction  = 'egg'
    def move(self,dx,dy):
        position = [0,0]
        position[0] = position[0]+dx
        position[1] = position[1]=dy
        return position
class Human(object):
    laugh = "yangml"
    def show_laugh(self):
        print self.laugh
    def show_100th(self):
        for i in range(1):
            self.show_laugh()
yang_ml = Human()
print yang_ml.show_100th()
#__init__()方法
class happyBird(Bird1):
    def __init__(self, more_words):
        print 'We are happy birds.',more_words
summer = happyBird('快乐')
print summer.__init__('happy happy')
#对象的性质
class Human1(object):
    def __init__(self,input_gender):
        self.gender = input_gender
    def printgender(self):
        print self.gender
person = Human1('male')
print person.printgender()
        