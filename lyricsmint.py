import requests
from bs4 import BeautifulSoup

url = 'https://lyricsmint.com/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
divtag = soup.select('#carousel div.relative')
print(len(divtag))

aTag = [x.find('a') for x in divtag]
# print(aTag)
imagesrc = [x.find('img') for x in aTag]
srclist = [img['src'] for img in imagesrc]
print(srclist)

urls = [a['href'] for a in aTag]
urls2 = [f"{url}{a['href']}" for a in aTag]
print(urls2)

# Download Images
i = 1
for src in srclist:
    tempRes = requests.get(src)
    f = open(f'img-{i}.png', 'wb')
    f.write(tempRes.content)
    f.close()
    i+=1
