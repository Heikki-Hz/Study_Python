#-*-coding:utf-8*-

#init list
classmates = ['Mach', 'Boy', 'Heikki']
a = 0

print(classmates)

#����list����
a = len(classmates)
print(a)
print('--------')

#����list����
print('Find')
print(classmates[0])
print('--------')
print(classmates[2])
print('--------')
print(classmates[-1])

print('--------')
print('Insert')
#�������ݵ�list��
classmates.insert(1, 'Tom')
print(classmates)

#ɾ��list�е�����
print('Del')
classmates.pop(1)
print(classmates)
print('--------')
classmates.pop()
print(classmates)
print('--------')
print('Switch')
#�滻Ԫ�سɱ��Ԫ��
classmates[1] = 'Clo'
print(classmates)




