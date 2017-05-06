# encoding:utf-8
import urllib.request
import xml.sax
url = 'http://flash.weather.com.cn/wmaps/xml/china.xml'
req = urllib.request.urlopen(url)
data = req.read().decode('utf-8')                       # 获得xml格式的字符串
p = xml.sax.parseString()                               # 错的
print(p)



