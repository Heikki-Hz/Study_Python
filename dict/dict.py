# -*- coding: utf-8 -*-
names = {'Heikki':95, 'Tom':96, 'Pright':97}
print(names['Heikki'])

#���˳�ʼ�������key�ķ���
names['Lucy'] = 100
print('Lucy is %s' % names['Lucy'])

#���key�治����
print('Hi' in names)

#keyֻ�ܶ�Ӧһ��value ��so ��һ��key���¸�ֵ�Ļ��Ḳ����ǰ��value
names['Lucy'] = 80
print('Lucy is %s' % names['Lucy'])

#ͨ��get�ж�key�Ƿ����(����ֱ�ӷ���none��Ҳ�����Լ�ָ��value)
re = names.get('Tom', -1)
print(re)
re = names.get('James', -1)
print(re)
re = names.get('James')
print(re)

#Del Key
names.pop('Heikki')
print(names)
