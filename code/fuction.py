import math

def my_abs(x):
    if x>0:
	return x
    else:
	return x+abs(x)


def nop():
    pass

def move(x,y,step,angle=0):
    nx = x+step*math.cos(angle)
    ny = y-step*math.sin(angle)
    return nx,ny


def power(x,n=2):
    s = 1
    while n>0:
        s = s*x
	n = n-1
    return s


def enroll(name,gender,age=6,city='beijing'):
    print('name=',name)
    print('gender=',gender)
    print('age=',age)
    print('city=',city)
    return None


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

def person(name,age,**kj):
    print('name=',name,'age=',age,'other=',kj)
