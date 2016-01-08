#/usr/bin/env python3
# -*- coding:utf-8 -*-

#Test
name = ['Heikki', 'Heiout', 'Pright', 'Bobbi', 'Bod'];

i_name = input("Please enter name: ").title();
wname = [];


for n in name:
    if n[:len(i_name)] == i_name:
        wname.append(n);

if len(wname) != 0:
    print('Do you want to find %s ?' % (wname))
else:
    print('Do not found !')

        
