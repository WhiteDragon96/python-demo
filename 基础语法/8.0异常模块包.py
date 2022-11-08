# 捕获常规异常
"""
语法：
try:
    可能出现异常的代码
except:
    出现异常后执行...
"""

try:
    print("要出现异常了")
    a = 1 / 0
except Exception as e:
    print("程序出现了异常")
    print(e)  # division by zero

print("=======================================异常else=======================================")
#### 异常else

# 没有异常时执行代码
"""
try:
    print("hi")
except Exception as e:
    print(e)
else:
    print("没有异常时执行...")
"""

try:
    print("要出现异常了")
except Exception as e:
    print(e)
else:
    print("没有异常")

print("=======================================异常finally=======================================")

"""
#### 异常finally

不管有没有异常都执行代码
"""

try:
    print("hi")
except Exception as e:
    print(e)
else:
    print("没有异常时执行...")
finally:
    print("不管有没有异常都执行....")

print("=======================================异常传递性=======================================")


# 通过异常具有传递性的特点，我们可以在外层调用处去捕获异常

def test_except():
    print("执行start...")
    a = 1 / 0
    print("执行start...")


try:
    test_except()
except ZeroDivisionError as e:
    print("出现异常了")
