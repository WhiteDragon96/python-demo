import os

# path定义要获取的文件名称的目录
path = "../"

listdir = os.listdir(path)

for dir in listdir:
    print(f"类型为：{type(dir)},内容是：{dir}")
