# 整数
print(6)
# 浮点数
print(6.6)
# 字符串
print("六六六")

# 单行注释
"""
    多行注释
"""

# 变量
num = 10
print("变量是：", num)
num = num - 3
print("变量变了：", num)

# 数据类型
str = "string"
flo = 6.6
print(type(str), type(flo), type(num))

"""
    标识符：内容标识，用于给变量、类、方法等命名。

    下划线命名法：`user_name`、`nick_name`
"""

# 数据输入
# num1 = input("请输入数据：")
# print("输入的数据是 %s " % num1)

# 比较运算符
bool = True
print(f"{bool} 类型是：{type(bool)}")

num2 = 10
print(f"num == num2 ====>{num == num2}")

if num2 > num:
    print(f"{num2}大于{num}")
    num += 1
i = 0;
j = 0;
while i <= 10:
    print(i)
    i += 1;
    while j <= 20:
        j += 5
        print("j:", j)

i = 1
while i <= 9:
    j = 1
    while j <= i:
        # 内层循环的print语句，不要换行，通过\t制表符进行对齐（\t:等同于在键盘上按下tab键）
        print(f"{j} * {i} = {j * i}\t", end="")
        j += 1
    i += 1
    print()  # print空内容，就是输出一个换行

"""
    for
    for 临时变量 in 待处理数据集(序列):
    循环满足条件时执行...
"""

name = "zhangsan"
for i in name:
    print(i)

for i in range(0, 10, 2):
    print(i)

for i in range(10):
    if i == 2: continue
    print(i)
    if i == 5: break
