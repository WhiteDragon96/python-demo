print("=======================================类的定义和使用=======================================")
"""
# 定义类
class 类名:
    # 类的属性 -- 成员变量
    类的属性1: None
    类的属性2: None
    
    # 类的行为 -- 成员方法  tips:类外部叫函数，类里面叫方法。  self: 让成员方法能访问到当前类的成员变量的值
    def 方法名(self, 形参1, 形参2, ...):
        方法体...
    

# 创建对象
对象 = 类名()

# 对象属性赋值
对象.属性名 = "xxx"
"""

"""
=======================================常用类内置方法(魔术方法)=======================================
`__init__`: 构造方法: 创建类对象时设置初始化行为
`__str__`: 实现类对象转字符串的行为
`__lt__`: 用于2个类对象进行小于或大于比较
`__le__`:
`__eq__`: 用于2个类对象进行相等比较
"""


class User:
    name: None
    age: None

    def say_hi(self):
        print(f"hi {self.name}")

    # 构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"姓名：{self.name},年龄:{self.age}")

    # 对象输出字符串
    def __str__(self):
        return f"姓名：{self.name} 年龄：{self.age}"

    # 大小比较
    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    # 相等比较
    def __eq__(self, other):
        return self.age == other.age

    """
     封装
    1. 将动物的身高、体重、外貌等封装为属性(类的成员变量)
    2. 将动物的吃饭、睡觉、跑步等封装为行为(类的成员方法)
    私有成员(变量和方法)：不对外开放-即类对象无法使用，但在类中可以使用-即提供仅内部可使用的属性和方法。 命名定义以`__`开头
    """

    # 私有成员变量
    __basic_age = 18

    # 私有成员方法
    def __un_adult(self):
        print(f"{self.name}未成年...")

    # 公开方法
    def is_adult(self):
        # 内部调用私有成员变量
        if self.age > self.__basic_age:
            print(f"{self.name}成年了")
        else:
            # 内部调用私有成员方法
            self.__un_adult()


user = User("张三", 18)
user.say_hi()
print(user)

user2 = User("迪丽热巴", 20)
print(user == user2)
print(user < user2)

print("=======================================封装=======================================")
user.is_adult()
user2.is_adult()

print("=======================================继承=======================================")

"""
# 单继承
class 类名(父类名):
    类内容体...
    
    
# 多继承 -- tips: 如果父类中有同名方法或属性，先继承的优先级高于之后的
class 类名(父类名1, 父类名2, ...):
    类内容体...    
"""


class Animal:
    name: None

    def run(self):
        print(f"动物名字是: {self.name}")


class Person:
    name: None

    def run(self):
        print(f"[人类] {self.name} 跑...")


class Cat(Animal, Person):
    pass


cat = Cat()
cat.name = "皮皮"  # 动物名字是: 皮皮
cat.run()

print("=======================================复写=======================================")

"""
复写：对父类的成员属性或方法重新定义。

语法：子类中定义同名的成员属性或方法即可。

子类中调用父类成员语法：
# 方式1：
父类名.成员变量
父类名.成员方法(self)

# 方式2：
super().成员变量
super().成员方法()
"""


class Dog(Animal):
    def run(self):
        print(f"f {self.name}复写了父类方法")


dog = Dog();
dog.name = "皮皮"
dog.run()

print("=======================================类型注解=======================================")
"""
类型注解：对数据类型进行显式的说明、提示 ex：PyCharm的代码提示
tips: 仅做提示使用，就算数据类型和类型注解无法对应也不会导致代码的错误。

- 语法1：`变量: 类型`
- 语法2：在注释中，`# type: 类型`

"""
# 基础数据类型注解
# type: int
var_1: int = 666
var_2: str = "字符串"
var_3: float = 6.6
var_4: bool = True

# 类对象类型注解
dog2: Dog = Dog()

# 基础容器类型注解
my_str: str = "white"
my_list: list = [1, 2, 3]
my_set: set = {1, 2, 3}
my_dict: dict = {"name": "张三"}

# 容器类型详细注解
my_list: list[int] = [1, 2, 3]
my_set: set[int] = {1, 2, 3}
my_dict: dict[str, int] = {"age": 18}
my_tuple: tuple[str, int, bool] = ("zq", 18, True)

# 类型注解 - 函数(方法)形参和返回值
"""
语法：
# 形参类型注解
def 函数(方法)名(形参名1: 类型, 形参名2: 类型, ...):
    pass
    
# 返回值类型注解
def 函数(方法)名(形参名1: 类型, 形参名2: 类型, ...) -> 返回值类型:
    pass
"""


def annotataion(x: int, y: int) -> int:
    pass


# 使用`Union类型`进行联合类型注解

from typing import Union


# 定义联合类型注解
# Union[类型1, 类型2, ...]


def func(data: Union[int, str]) -> Union[int, str]:
    pass


func(1)


