#coding=gbk
'''
Created on 2014��3��18��

@author: bling
'''
#������󣬹�Ϊ��
class Bird(object):
    hava_feather = True
    way_of_reproduction  = 'egg'
summer = Bird()
print summer.way_of_reproduction,summer.hava_feather
#����
class Bird1(object):
    hava_feather = True
    way_of_reproduction  = 'egg'
    def move(self,dx,dy):
        position = [0,0]
        position[0] = position[0]+dx
        position[1] = position[1]=dy
        return position
summer = Bird1()
print "after move:",summer.move(5, 8)
#����
class Chicken(Bird1):
    way_of_move = 'walk'
    possible_in_KFC = True

class Oriole(Bird1):
    way_of_move = 'fly'
    possible_in_KFC = False
summer = Chicken()
oriole = Oriole()
print summer.hava_feather
print oriole.move(55, 66)