#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is runing')

class Dog(Animal):
    def run(self):
        print('Dog is runing')
    def stop(self):
        pass

class Cat(Animal):
    def run(self):
        print('Cat is runing')

animal = Animal()

dog = Dog()
dog.run()

cat = Cat()
cat.run()

print('--------------------------')
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
print('--------------------------')

#判断class的类型
print(isinstance(dog, Dog))
print('Dog 的类型是否与Animal一样',isinstance(dog, Animal))
print('animal 的类型是否与Dog一样',isinstance(animal, Dog))


print(dir(Dog))
print(len('ABC'))
