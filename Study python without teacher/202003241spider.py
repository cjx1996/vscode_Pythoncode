import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self,site):
        self.site= site
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = 'html.parser'
        sp = BeautifulSoup(html, parser)
        i=1
        with open('e:/code/Study python without teacher/news.txt','w',newline='')as f:
            for tag in sp.find_all('a'):  #根据标签寻找
                url = tag.get('href')#根据属性寻找
                if url is None or tag.string is None:
                    continue
                if 'html' in url :
                    f.write(str(i)+'\n')
                    f.write(url+'\n')
                    f.write(tag.string+'\n\n')
                    print(i)
                    print(url)
                    print(tag.string+'\n')
               
                    i+=1

news = 'https://news.baidu.com/'
Scraper(news).scrape()






































