# -*- coding:utf-8 -*-

#Create a Set �ظ���set���Զ������˵���
names = ['Heikki','Heikki', 'Tom', 'Lucy']
s = set(names)
print(s) #��ӡ������˳��һ���������

#Add Ԫ��
s.add('Pright')
print(s)

#Remove Key
s.remove('Tom')
print(s)

#����Set
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])

print(s1 & s2)
print(s1 - s2)
print(s1 | s2)
