import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

xmlurl = 'http://py4e-data.dr-chuck.net/comments_1546839.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = xmlurl
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
tree = ET.fromstring(data)

results = tree.findall('.//count')
sumComments=0
for comment in results:
    sumComments=sumComments + int(comment.text)
print(sumComments)