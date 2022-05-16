import json
import urllib.request, urllib.parse, urllib.error
import ssl

jsonurl = 'http://py4e-data.dr-chuck.net/comments_1546840.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = jsonurl
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
totalCount=0
info = json.loads(data)
for item in info["comments"]:
    totalCount=totalCount+int(item['count'])
print(totalCount)