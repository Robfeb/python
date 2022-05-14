
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urlopen("http://py4e-data.dr-chuck.net/comments_1546837.html", context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
sumOfValues=0
tags = soup('span')
print(len(tags))
for tag in tags:
    sumOfValues=sumOfValues+int(tag.contents[0])
print('total sumOfValues:', sumOfValues)