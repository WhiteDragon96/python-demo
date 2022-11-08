"""
包：就是一个文件夹，里面有多个模块文件。 -- 通过包分类管理模块

从物理上看，包，在该文件夹下包含了一个`__init__.py`文件

创建包会自动生成`__init__.py`文件：标识这是一个python的包，非普通文件夹
"""

print("=======================================导入自定义包中的模块并使用=======================================")

import my_package.my_module as module

module.test()

print("=======================================__all__` 控制`import *`可使用模块=======================================")

"""
`__init__.py` -> `__all__` 控制`import *`可使用模块

导入自定义包中的模块并使用时发现`my_module3`无法调用，因为在`__init__.py`中未声明引用
"""

from my_package import *

my_module.test()
my_module2.test()
# my_module3.test() 无法调用

# 第三方包：非Python官方内置的包，可以通过安装它们扩展功能，提高开发效率。
"""
ex:
1. 科学计算中常用的：`numpy`包
2. 数据分析中常用的：`pandas`包
3. 大数据计算中常用的：`pyspark`、`apache-flink`包
4. 图形可视化常用的：`matplotlib`、`pyecharts`
5. 人工智能常用的：`tensorflow`
"""
from numpy import *
