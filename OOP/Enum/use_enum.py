#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'JUL',\
        'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

Week = Enum('Week', ('Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun'))

@unique
class WeekDay(Enum):
    Sun = 0
    mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fir = 5
    Sat = 6

print(WeekDay.Fir)

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

for name, member in Week.__members__.items():
    print(name, '=>', member, ',', member.value)
