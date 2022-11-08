# 模块
"""
 模块就是一个Python文件（以`.py`结尾），里面有类、函数、变量等，我们可以导入模块进行使用。

 语法：`[from 模块名] import [模块|类|变量|函数|*] [as 别名]`
"""

import time

time.sleep(2)
print("hello...")

# from 模块名 import 类、变量、方法等

from time import sleep

sleep(3)
print("hello...")

"""
from 模块名 import *
`*`：导入指定模块名的全部功能
"""

from time import *
print(thread_time())

# import 模块名 as 别名
import time as t
t.sleep(1)
print("hello...")

print("=======================================导入自定义模块使用=======================================")
"""
如果其它模块里有执行函数的代码，当我们在导入其它模块时，也会默认执行
比如 my_module 的test()因为import 会执行一次
"""
import my_module as my
my.test()

