import json
import urllib.request

url = "http://py4e-data.dr-chuck.net/comments_1357658.json"
data = html = urllib.request.urlopen(url).read()


info = dict(json.loads(data))
summ = 0
for item in info['comments']:
    num_str = item['count']
    num = int(num_str)
    summ += num

print(summ)

    
