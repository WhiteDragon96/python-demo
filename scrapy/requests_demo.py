import requests

url = 'http://www.baidu.com/s?'
baidu_translate_url = 'http://fanyi.baidu.com/sug'

headers_response = requests.get("http://www.baidu.com")
print(headers_response.headers)
heads = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Cookie": "BIDUPSID=F9A4E449BDEFDAA59AAC5E8687D57159; PSTM=1613635021; BD_UPN=12314753; ISSW=1; __yjs_duid=1_1b986c06d8e31dfd70224052da0d906d1619140220239; H_WISE_SIDS=107311_110085_127969_164870_179350_181589_183031_184009_184267_185632_186539_186635_186743_186840_187087_187449_187485_187828_188452_188552_189094_189711_189731_189755_190034_190679_190756_190803_191068_191245_191368_191478_191501_191810_192206_192359_192383_192407_192890_193284_193291_193558_193753_193890_194085_194122_194130_194513_194520_194583_194602_194877_194889_194920_195149_195178_195189_195342_195477_195542_195577_195592_195610_195625_195678_195969_196000_196049_196229_196276_196322_196382_196427_196462_196642_196700_196754_196925_196940_197009_197157_197215_197222_197288_197291_197576; BDUSS=J4eGNnd2paMnhNOEdEUi1JR3NvUGd6ZnJpYnlzWH5UNXdkM05sOW5jY2pNZzVpSVFBQUFBJCQAAAAAAAAAAAEAAABbJw43usO-w7K7vPpDYwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACOl5mEjpeZhN3; BDUSS_BFESS=J4eGNnd2paMnhNOEdEUi1JR3NvUGd6ZnJpYnlzWH5UNXdkM05sOW5jY2pNZzVpSVFBQUFBJCQAAAAAAAAAAAEAAABbJw43usO-w7K7vPpDYwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACOl5mEjpeZhN3; BAIDUID=E11213FB82C18B169534C487152A1771:SL=0:NR=10:FG=1; ISSW=1; BDSFRCVID_BFESS=tRLOJexroG0604nDki1tt8fJteKKvV3TDYLEOwXPsp3LGJLVg66sEG0PtOUBIE_bIJ9eogKKKgOTHICF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJ-j_K05JID3H48k-4QEbbQH-UnLqb3NBgOZ04n-ah02MCtmhxOOMj_35a7hBJ3-W23q-DOm3UTdsq76Wh35K5tTQP6rLt-qJj74KKJxbp7lElTHBP5zy6F8hUJiBMnMBan7alOIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbRO4-TFMe5cyeM5; H_WISE_SIDS_BFESS=107311_110085_127969_164870_179350_181589_183031_184009_184267_185632_186539_186635_186743_186840_187087_187449_187485_187828_188452_188552_189094_189711_189731_189755_190034_190679_190756_190803_191068_191245_191368_191478_191501_191810_192206_192359_192383_192407_192890_193284_193291_193558_193753_193890_194085_194122_194130_194513_194520_194583_194602_194877_194889_194920_195149_195178_195189_195342_195477_195542_195577_195592_195610_195625_195678_195969_196000_196049_196229_196276_196322_196382_196427_196462_196642_196700_196754_196925_196940_197009_197157_197215_197222_197288_197291_197576; MCITY=-%3A; H_PS_PSSID=36561_37551_37688_36885_37623_36786_37540_37499_37582_26350; BAIDUID_BFESS=E11213FB82C18B169534C487152A1771:SL=0:NR=10:FG=1; delPer=0; BD_CK_SAM=1; PSINO=5; sug=3; sugstore=0; ORIGIN=0; bdime=0; H_PS_645EC=c748GhX5GQoSPE7lNSbCcaoJeciRbezGgib7hlbQg9yumvGcmPqyWs8TlG8; BA_HECTOR=a18g2hak2k05a52025210nv31hm90vh1f; ZFY=wJB3iz4vky88LI4B2MeFpUIN7S3vWkWrMMy68CjaDPU:C",
    # "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\""
}
print("============================================get??????============================================")
data = {
    'wd': '??????'
}

try:
    response = requests.get(url, headers=heads, data=data)
    response.encoding = 'utf-8'
    print(response.text)
except Exception as e:
    print(f"get???????????????,{e}")

print("============================================post??????============================================")
try:
    translate_data = {'kw': 'eye'}
    translate_reaponse = requests.post(baidu_translate_url, headers=heads, data=translate_data)
    translate_reaponse.encoding = 'utf-8'
    print(translate_reaponse.text)
except Exception as e:
    print(f"post???????????????,{e}")

print("============================================??????============================================")

tongjiju_url = 'https://www.douyin.com/'

response_tongji = requests.get(tongjiju_url,headers=heads)
print(response_tongji.apparent_encoding)
response_tongji.encoding = response_tongji.apparent_encoding
print(response_tongji.text)
