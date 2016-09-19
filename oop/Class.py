# coding=utf-8
class Student(object):
    def __init__(self, name, age, score=100):
        self.name = name
        self.age = age
        self.score = score

    def print_s(self):
        print('%s: %d' % (self.name, self.age))

    def print_score(self):
        if self.score <= 60:
            print("及格")
        elif self.score <= 90:
            print("优秀")
        elif self.score == 100:
            print("满分")


std = Student('Kevin', 20)

std.print_s()
std.print_score()


# __表示私有变量，实例无法访问
class PrivateStudent(object):
    def __init__(self, name, age, score):
        self.__name = name
        self.__age = age
        self.__score = score

    def print_score(self):
        print(self.__score)


priStd = PrivateStudent("kevin", 20, 90)
priStd.print_score()


