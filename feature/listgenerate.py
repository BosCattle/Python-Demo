import os

print(list(range(90, 100)))
print([x * x for x in range(1, 11)])
print([x * x for x in range(90, 101)])
print([x * x for x in range(90, 101) if x % 2 == 0])
print([m + n for m in range(20, 30) for n in range(90, 101)])

# 列出当前目录的所有目录和文件
print([dic for dic in os.listdir('.')])
item = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G'}
for k, v in item.items():
    print(k, v)


