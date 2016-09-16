# coding=utf-8
""" practise a test module"""
__author__ = 'Kevin'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print('hello,%s!', args[1])
    else:
        print('you have many argument!')


if __name__ == '__main__':
    test()

# _表示私有的，不应该被直接引用
def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
