import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

def parse(string):
    f = re.findall("known_by_\S+",string)
    splitted = f[0].split(".")
    splitted = splitted[0].split("_")
    name = splitted[2]
    return name

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
pos = 17
proccess = 7
url = 'http://py4e-data.dr-chuck.net/known_by_Rossi.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
hrefs = []
names = []
for tag in tags:
    hrefs.append(tag.get('href',None))

for i in range(proccess):
    url = hrefs[pos]
    name = parse(url)
    names.append(name)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    hrefs.clear()
    for tag in tags:
        hrefs.append(tag.get('href',None))

print(names[-1])