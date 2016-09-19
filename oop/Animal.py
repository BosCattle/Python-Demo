# coding=utf-8
import logging


class Animal(object):
    def run(self):
        print("run is starting")


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("dog is starting")


class Pig(Animal):
    def run(self):
        print("pig is starting")


a = Animal()
b = Dog("dog", 10)
c = Pig()

a.run()
b.run()
c.run()

print(type(a) == type(b))
print(isinstance(b, Animal))
print(dir(Pig))

print(hasattr(b, 'name'))
print(setattr(b, 'name', 'Kevin'))
print(b.name)


# 实例属性等级高于类属性，所有，两种类型在相同的类中不要相同

class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = '0'
n= int(s)
logging.basicConfig(level=logging.INFO)
logging.info('n = %d' % n)
print(10/n)
