# coding=utf-8
import os
import subprocess
'执行linux命令'
print(os.system('ls -al'))

print(subprocess.call('ls -al'.split()))

