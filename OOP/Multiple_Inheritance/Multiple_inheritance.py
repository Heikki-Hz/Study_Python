#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    pass

#大类
class Manmmal(Animal):
    pass

class Bird(Animal):
    pass
#各种动物
class Bat(Manmmal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

#小类
class RunnableMixin(object):
    def run(slef):
        print('Running .....')

    
class FlyableMixin(object):
    def fly(slef):
        print('Flying .....')

class Dog(Animal, Runnable):
    pass
