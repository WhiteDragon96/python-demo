"""
    # 定义函数
    def 函数名(形参):
        函数体
        return 返回值

    # 调用函数
    函数名(实参)
"""


def sayHi():
    print("Hi")


def add(a, b, c):
    return a + b + c


sayHi()
print(f"a+b+c的结果是：{add(1, 2, 3)}")
print(
    f"无返回值函数 返回内容：{sayHi()} 返回内容类型：{type(sayHi())}"
)  # 无返回值函数 返回内容：None 返回内容类型：<class 'NoneType'>

# None用于if判断
if not None:
    print("None值 相当于 False ...")


# 嵌套调用
def inter_say_hello():
    print("调用sayHi()")
    sayHi();


inter_say_hello();


# 将函数内部定义的变量声明为全局变量 - global关键字

def global_num():
    global num
    num = 666
    print("局部变量声明为全局变量：", num)


global_num()
print(num)


# 函数多个返回值
def test_return():
    return 1, "hello", True


a, b, c = test_return()
print(f"多个返回值,a:{a},b:{b},c:{c}")


def user_info(name, age, sex='male'):
    print(f"user name is:{name},age:{age},sex:{sex}")


# 位置传参
user_info("zhangsan", 18, 'male')

# 关键字参数
user_info(name="关键字参数", age=20, sex="woman")

#### 缺省参数
# 不传递参数值时会使用默认的参数值
user_info("缺省参数", 25)


# 不定长参数 `*`标记形参 形参一般命名`args`
# 以元组形式接收参数
def user_info(*args):
    print(f"不定长 - 位置不定长：{args} 类型:{type(args)}")


user_info(1, 2, 3, 4, 5, "wangwu")


# 关键字传递 => `**`标记形参
# 以字典形式接收参数
# 形参一般命名`kwargs`

def user_info(**kwargs):
    print(f"不定长 - 关键字不定长：{kwargs} 类型:{type(kwargs)}")


user_info(name="小白", age=18, sex="男", type="不定长")


### 匿名函数
#### 函数作为参数传递
# 作用：传入计算逻辑，而非传入数据

def test_func(add2):
    print(f"类型：{type(add2)},结果：{add2(1, 2)}")


def add2(a, b):
    return a + b


test_func(add2)

# lambda匿名函数

# 1. 匿名函数用于临时构建一个函数，只用一次的场景
# 2. 匿名函数的定义中，函数体只能写一行代码，如果函数体要写多行代码，不可用lambda匿名函数，应使用def定义具名函数
# 语法：`lambda 传入参数: 函数体(一行代码)`

test_func(lambda a, b:
          a + b)
