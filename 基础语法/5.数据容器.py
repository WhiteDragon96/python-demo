"""
    数据容器：一种可以存储多个元素的python数据类型。
    1. list: 列表 []
    2. tuple: 元组 ()
    3. str: 字符串 ""
    4. set: 集合 {}
    5. dict: 字典
"""

# list
my_list = [1, 2, 3, 4]
print(my_list)

# 定义一个嵌套的列表
my_list2 = [[1, 2, 3], [4, 5, 6]]
print(my_list2)
print(type(my_list2))

# 删除元素3
index = my_list.index(3)
del my_list[index]
print(my_list)


# 遍历列表
def while_list():
    my_list = ["java", "python", "go", "lua"]
    # 循环控制变量：通过下标索引来控制，默认是0
    # 每一次循环，将下标索引变量+1
    # 循环条件：下标索引变量 < 列表的元素数量
    index = 0
    while index < len(my_list):
        print(my_list[index])
        index += 1;


while_list();

for element in my_list:
    print(element)

# tuple 元组

"""
    元组特点：
    
    1. 可以容纳多个数据
    2. 可以容纳不同类型的元素（混装）
    3. 数据是有序存储的（下标索引）
    4. 允许重复数据存在
    5. 不可以修改（修改/增加/删除元素等） -- tips: 可以修改内部list中的元素
    6. 支持while/for循环
"""

t1 = ("zhengqingya", 666, True, 666)
print(f"t1 类型：{type(t1)}  内容：{t1}")

print(t1.count(666))

for item in t1:
    print(item)

"""
    str 字符串
    
    字符串特点：
    
    1. 只可以存储字符串
    2. 长度任意（取决于内存大小）
    3. 支持下标索引
    4. 允许重复字符串存在
    5. 不可以修改（修改/增加/删除元素等） -- tips: 不可修改字符串本身，但可通过replace替换得到一个新字符串
    6. 支持while/for循环
"""

my_name = "whte_white"
for item in my_name:
    print(item)

### 切片
#
# 切片：从一个序列中取出一个子序列
#
# 语法：`序列[起始下标: 结束下标: 步长]`

print(my_name[1:2])
print(my_list[::2])

"""
    ### set 集合
    
    集合特点：
    
    1. 可以容纳多个元素
    2. 可以容纳不同类型的元素（混装）
    3. 数据是无序存储的（不支持下标索引）
    4. 不允许重复数据存在
    5. 可以修改(增加/删除元素等)
    6. 支持for循环，不支持while循环（因为不支持下标索引）
"""

my_set = {"java", "python", "go", "go", "lua"}
my_set2 = {"java1", "python", "go1", "go", "lua"}

for item in my_set:
    print(item)

print(f"set随机取出一个元素：{my_set.pop()}")

# 两个集合的差集
# 用于查找两个集合之间的差，该方法以该集合(set1)调用，另一个集合(set2)作为参数传递，并且它返回set2中不存在的元素集。
print(my_set2.difference(my_set))

# 在集合 1 中，删除集合 2 中存在的元素，集合 1 被修改，集合 2 不变
my_set.difference_update(my_set2)
print(my_set)

# 合并集合，得到 1 个新集合，原有的 2 个集合内容不变
print(my_set.union(my_set2))

"""
    ### dict 字典
    
    字典特点：
    
    1. 可以容纳多个元素
    2. 可以容纳不同类型的元素
    3. 每一份数据是`key:value`键值对
    4. key和value可以是任意数据类型（key不可为字典）
    5. 可以通过key获取到value，key不可重复（重复会覆盖原有数据）
    6. 不支持下标索引
    7. 可以修改（增加/删除/更新元素等）
    8. 支持for循环，不支持while循环
    
    # 定义字面量
    {key:value, key:value, key:value ...}
"""

my_dict = {"name": "zhangsan", "age": 18, "sex": "male"}
print(f"my_dict:{my_dict}")
print(len(my_dict))
for key in my_dict.keys():
    print(f"key is:{key},value is:{my_dict[key]} ")

print(max(my_list))

# 降序
print(f"sorted my_list:{sorted(my_list, reverse=True)}")
# 升序
print(f"revered my_list:{sorted(my_list, reverse=False)}")

# 字符串大小比较
print("aaabbb" > "aaab")
