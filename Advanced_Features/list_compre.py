#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#List comprehensios test

L = list(range(1, 11));
print(L);

#[1*1, 2*2, 3*3 ...]
L = [];

for k in range(1, 11):
    L.append(k * k);

print(L);

List = [x * x for x in range(1, 11)];
print(List);

List = [x * x for x in range(1, 11) if x % 2 == 0];
print(List);

List = [m + n for m in 'ABC' for n in 'XYZ']
print(List);

import os;
List = [d for d in os.listdir('../.')];
print(List);

d = {'x': 'A', 'y': 'B', 'z': 'C'};
List = [k + '.' + v for k, v in d.items()];
print(List);

List = ['Hello', 'Yes', 'OK'];
print([s.lower() for s in List])


List = ['Hello', 'Yes', 10, 'OK', 'Heikki'];
print([s.lower() for s in List if isinstance(s, str)])

L1 = [];
for s in List:
    if isinstance(s, str):
        L1.append(s.lower());
print(L1);


