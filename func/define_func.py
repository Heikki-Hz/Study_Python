#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#����һ������
def my_abs(x):
    if x >= 0:
        return x
    else:
        return(-x)

n = 10
m = -19

print(my_abs(n))
print(my_abs(m))

#�պ���
def nop():
    pass

#�����Ĳ���
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

#�ɱ��������ϰ
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
#����������listʵ��
def calc_list(number):
    sum = 0

    for x in number:
        sum += x * x 

    # #����ʹ��while�Ƚ��˷�.��֪���ڲ��ú������������º���û�б�ķ�ʽ
    #numberlen = len(number)
    # while(numberlen > 0):
        # sum += numberlen * numberlen
        # numberlen -= 1

    return sum


print(calc_list(list1))
print(calc_list(list2))
print(calc_list(list3))
            

#�ؼ��ֲ���
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

#�����ؼ��ֲ���
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
