# 列表生成式方式一
l = [x * x for x in range(1, 10)]
print(l)
l = (x * x for x in range(1, 10))
print(l)
print(next(l))
print(next(l))
for n in l:
    print(n)



# 列表生成式方式二
# #著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
def fib(max):
    n = 0
    a = 0
    b = 1
    while n < max:
        print(n, b)
        t = (b, a + b)  # t是一个tuple
        a = t[0]
        b = t[1]
        n += 1
    return None


fib(10)


# 要把fib函数变成generator，只需要把print(b)改为yield b就可以了
def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
        print(b)
    return 'done'
fib1(5)