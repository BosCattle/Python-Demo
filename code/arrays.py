#!/usr/bin/env python3
# -*- coding: utf-8 -*-
classmates = ['dsdsd','kevin','double','fight']
print(classmates)
classmates.append('append')
print(classmates)
classmates.insert(0,'bash')
print(classmates)
classmates.pop()
print(classmates)
classmates.pop(1)
print(classmates)
classmates[0] = 'one'
print(classmates)

# tuple(元组，初始化之后不可以改变)
t = (1,2)
print(t)
m = ()
print(m)
# 定义一个元素的tuple，必须加上逗号
n = (1,)
print(n)
# tuple只是元素个数不可变，内部放一个数组就可以变
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])
