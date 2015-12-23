# -*- coding:utf-8 -*-

#Create a Set 重复在set中自动被过滤掉了
names = ['Heikki','Heikki', 'Tom', 'Lucy']
s = set(names)
print(s) #打印出来的顺序不一定是有序的

#Add 元素
s.add('Pright')
print(s)

#Remove Key
s.remove('Tom')
print(s)

#两个Set
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])

print(s1 & s2)
print(s1 - s2)
print(s1 | s2)
