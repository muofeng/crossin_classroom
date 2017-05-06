import requests
url = 'https://xueqiu.com/p/discover'
req_header = {
    'User-Agent': 'Chrome',
}
req = requests.get(url, headers=req_header)             # 加入header信息模拟浏览器
print(req.encoding)
data = req.text
print(type(data))
print(data)

