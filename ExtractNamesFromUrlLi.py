
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

def getLink18(url,position):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    name=''
    link=''
    count=0
    tags = soup('a')
    for tag in tags:
        if(count==(position-1)):
            print(tag.contents[0])
            return tag.get('href', None)
        count= count +1


initUrl='http://py4e-data.dr-chuck.net/known_by_Shea.html'
numberOfLoopsToRepeat=7
numberOfpositions=18
numLoops=0
lastname=''
while numLoops<(numberOfLoopsToRepeat):
    initUrl=getLink18(initUrl,numberOfpositions)
    numLoops=numLoops+1

print('initUrl:', initUrl)




