#!/use/bin/env python3
#-*- coding:utf-8 -*-

List = [6, -19, 30, 35, 2, 5, 8]
print(sorted(List))
print(sorted(List, key = abs))
print(sorted(List, key = abs, reverse = True))

L = [('Bob', 75), ('Adam', 92),('Bart', 66), ('Lisa', 88)]

def by_name(t):
    print(t[0])
    return t[0]
def by_score(t):
    print(t[1])
    return t[1]
ret = sorted(L, key = by_name)
print(ret)
ret1 = sorted(L, key = by_score, reverse = True)
print(ret1)
