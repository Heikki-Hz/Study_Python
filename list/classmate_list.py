#-*-coding:utf-8*-

#init list
classmates = ['Mach', 'Boy', 'Heikki']
a = 0

print(classmates)

#计算list长度
a = len(classmates)
print(a)
print('--------')

#查找list方法
print('Find')
print(classmates[0])
print('--------')
print(classmates[2])
print('--------')
print(classmates[-1])

print('--------')
print('Insert')
#插入数据到list中
classmates.insert(1, 'Tom')
print(classmates)

#删除list中的数据
print('Del')
classmates.pop(1)
print(classmates)
print('--------')
classmates.pop()
print(classmates)
print('--------')
print('Switch')
#替换元素成别的元素
classmates[1] = 'Clo'
print(classmates)




