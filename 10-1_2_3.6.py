import urllib.request
import json
url = 'https://api.douban.com/v2/movie/top250'
req = urllib.request.urlopen(url)
data = req.read().decode('utf-8')
data_dic = json.loads(data)                             # �õ�json��ʽ���ַ���
print(data_dic)
print(data_dic.keys())
print(data_dic['title'])