import urllib.request
import urllib.parse
word = input('searching: ')
word = urllib.parse.quote(word)
url = 'http://www.baidu.com/s?wd=%s' % word
print(url)
req = urllib.request.urlopen(url)
data = req.read().decode('utf-8')
with open('searching.html', 'w', encoding='utf-8') as f:
    f.write(data)


