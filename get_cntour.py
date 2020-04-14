import requests
from bs4 import BeautifulSoup
url="http://www.cntour.cn/"

response=requests.get(url)
#print(response.text)

soup=BeautifulSoup(response.text,'lxml')
soup.select("#main > div > div.mtop.firstMod.clearfix > div.leftBox > div.ui-tabs-panel.ui-tabs-hide > ul > li:nth-child(7) > a")

print(data)

for item in data:
    result={
        'title':item.get_text(),
        'link':item.get('href')
    }
print(result)