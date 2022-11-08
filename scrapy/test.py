import requests
import urllib.request
import urllib.parse

url = "http://www.baidu.com"

response = requests.get(url)
"""
response 服务器返回的数据
response的数据类型是HttpResponse
字节‐‐>字符串
解码decode
字符串‐‐>字节
编码encode
"""
print(type(response))

# 字节形式读取二进制 扩展：rede(5)返回前几个字节
# print(response.read(5).decode('utf-8'))

# 读取一行
# print(response.readline().decode('utf-8'))

# 一行一行读取直到结束
# print(response.readlines())

# 请求网页 请求图片 请求视频
# requests.urlretrieve(url, filename="urllib_request_demo.html")

url = 'https://www.baidu.com/s?wd='
headers = {
    'User‐Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/74.0.3729.169 Safari/537.36'
}
url = url + urllib.parse.quote('小野')
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode('utf‐8'))
