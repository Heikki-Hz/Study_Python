# -*- coding: utf-8 -*-
names = {'Heikki':95, 'Tom':96, 'Pright':97}
print(names['Heikki'])

#除了初始化是添加key的方法
names['Lucy'] = 100
print('Lucy is %s' % names['Lucy'])

#检查key存不存在
print('Hi' in names)

#key只能对应一个value ，so 对一个key重新赋值的话会覆盖以前的value
names['Lucy'] = 80
print('Lucy is %s' % names['Lucy'])

#通过get判断key是否存在(可以直接返回none，也可以自己指定value)
re = names.get('Tom', -1)
print(re)
re = names.get('James', -1)
print(re)
re = names.get('James')
print(re)

#Del Key
names.pop('Heikki')
print(names)
