"""
| 操作                                    | 功能                                              |
| --------------------------------------- | ------------------------------------------------- |
| `文件对象 = open(file, mode, encoding)` | 打开文件获得文件对象                              |
| `文件对象.read(num)`                    | 读取指定长度字节，不指定num读取文件全部           |
| `文件对象.readline()`                   | 读取一行                                          |
| `文件对象.readlines()`                  | 读取全部行，得到列表                              |
| `for line in 文件对象`                  | for循环文件行，一次循环得到一行数据               |
| `文件对象.close()`                      | 关闭文件对象                                      |
| `with open() as f`                      | 通过`with open`语法打开文件，可以自动关闭文件对象 |

"""

file = open("1.base.py", "r", encoding="UTF-8")
# 读取文件
# print(f"文件内容：\n{file.read()}")
# 读取一行
print(f"读取一行：{file.readline()}")
# 读取全部行，得到列表

# lines = file.readlines()
# print(f"lines对象类型：{type(lines)}  内容：\n{lines}")

# for循环读取文件行
for f in file:
    print(f)

# file.close()

# with open 语法操作文件 -- 此方式可以自动关闭文件
with open("1.base.py", "r", encoding="UTF-8") as with_file:
    print(with_file.readline())

# 文件写入
# flush作用: 避免频繁操作硬盘，导致效率下降，因此在文件写好之后，再一次性写入磁盘中

# 1、打开文件 -- 如果文件存在将清空原有内容重新写入
write_file = open("./test.txt", "w", encoding="UTF-8")
# 2、文件写入 -- 写入到缓冲区
write_file.write("Hello Write")
# 3、内容刷新 -- 真正写入文件
write_file.flush()
# 4、close关闭 内置了flush功能
write_file.close()

# 文件追加
write_add_file = open("./test.txt", "a", encoding="UTF-8")
write_add_file.write("\n追加内容")
write_add_file.flush()













