#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#定义一个函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return(-x)

n = 10
m = -19

print(my_abs(n))
print(my_abs(m))

#空函数
def nop():
    pass

#函数的参数
def power(argv1, argv2 = 2):
    s = 1
    tmp = argv2
    while(argv2 > 0):
        argv2 = argv2 - 1
        s = s * argv1 
    print('%d-th power %d is %d' % (tmp, argv1,  s))
    return s

power(2, 4)
power(5)
power(3, 3)

#可变参数的练习
list1 = [1, 2]
list2 = [1, 2, 3]
list3 = [1, 3, 5, 7]

def calc(*number):
    sum = 0
    for n in number:
        sum += n * n
    return sum
print(calc(1, 2))
print(calc(1, 2, 3))
print(calc(1, 3, 5, 7))
print(calc(*list1))

print('Use list to do this thing')
#上面列子用list实现
def calc_list(number):
    sum = 0

    for x in number:
        sum += x * x 

    # #看来使用while比较浪费.不知道在不该函数定义的情况下害有没有别的方式
    #numberlen = len(number)
    # while(numberlen > 0):
        # sum += numberlen * numberlen
        # numberlen -= 1

    return sum


print(calc_list(list1))
print(calc_list(list2))
print(calc_list(list3))
            

#关键字参数
#d = {'Heikki':95, 'Tom':90}
print('Please input your name:')
name = input()
print('Please input your age:')
age = input()
print('Please input your city:')
city = input()
print('Please input your job:')
job = input()

kw = {name:age}
def person(name, age, **keyword):
    if keyword: 
        print('name:', name, 'age:', age, 'other:', 
                name ,'(%s)' % kw[name])
    else:
        print('name:', name, 'age:', age)
print(person(name, age, **kw))
print(person('Heikki', 30))
print(person('Heikki', 30, city = 'ShangHai'))

#命名关键字参数
def person_key(name, age, *, city = 'Beijin', job = 'Python'):
    if 'city' and 'job':
        print('name:', name, 'age:', age, 'city:', city, 'job:', job)
    elif 'job':
        print('name:', name, 'age:', age, 'job:', job)
    elif 'city':
        print('name:', name, 'age:', age, 'city:', city)
    else:
        print('name:', name, 'age:', age)

print(person_key(name, age, city = city, job = job))
print(person_key(name, age))
