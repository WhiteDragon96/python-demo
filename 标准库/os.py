import os

# 当前目录
print(os.getcwd())
print(dir(os))

os.system('ipconfig')

import sys

print(sys.argv)

import requests

respones = requests.get("http://localhost:8327//api/ecology-data//devices/data", headers={
    "Blade-Auth": "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJpc3N1c2VyIiwiYXVkIjoiYXVkaWVuY2UiLCJ0ZW5hbnRfaWQiOiIwMDAwMDAiLCJ0b2tlbl90eXBlIjoiYWNjZXNzX3Rva2VuIiwiY2xpZW50X2lkIjoibmV1c2Vuc2VfYWkiLCJleHAiOjE2Njc5NzkxNjgsIm5iZiI6MTY2NzM3NDM2OH0.DAw5bidXLBv_TqxFv7EZU-7oxNw_53YiZqbAQpeVpfC0Hokek3kg5kUlLuorbV4-yocBEDJBS07o2A6iKIJQNQ"})

print('-------二进制的文档格式----------')
print(respones.content)  # 二进制的文档格式
print('--------文本文档的格式---------')
print(respones.text)  # 文本文档的格式
print('--------获取头文件---------')
print(respones.headers)  # 获取头文件
print('--------查看状态码---------')
print(respones.status_code)  # 查看状态码

# 多线程

import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('__init__.py', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')

import logging
logging.info("logging")
logging.error('Error occurred')