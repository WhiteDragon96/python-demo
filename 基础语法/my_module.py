"""
`__all__`

控制`import *`时哪些功能可以被导入
"""

__all__ = ["test", "test3"]

"""
from my_module import *

test()
test3()
# test2() # 这里无法调用
"""


def test():
    print("test my module...")


def test2():
    print("test2 my module...")


def test3():
    print("test3 my module...")


test()

"""
当程序直接被执行时才进入if内部，如果是通过导入方式则不会被执行
这里不会执行test逻辑代码
"""
if __name__ == "__main__":
    test()
