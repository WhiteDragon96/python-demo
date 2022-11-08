"""
### JSON

JSON是一种轻量级的数据交互格式。
JSON本质上是一个带有特定格式的字符串。

Python数据和JSON数据 相互转换
`json.dumps(data, ensure_ascii=False)` : python中的列表或字典 转 json字符串，`ensure_ascii=False`：解决中文乱码问题
`json.loads(json_str)`: json字符串 转 python中的列表或字典
"""
import json

dict_data = [{"name": "admin", "age": 18}, {"name": "test", "age": 20}]
print(dict_data)
json_str = json.dumps(dict_data, ensure_ascii=False)
print(json_str)
