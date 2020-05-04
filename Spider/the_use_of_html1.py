import lxml.html
import os
import csv
import re
import requests
from multiprocessing import Pool

#获取目标url的源代码
source=requests.get('http://www.biquge.info/48_48749/').content.decode()


#获取相应网页源代码
selector=lxml.html.fromstring(source)


#starts-with和contains的使用
content=selector.xpath('//div[@class="box_con"]/div[@id="list"]/dl/dd/a[starts-with(@href,"51199")]/text()')
content2=selector.xpath('//body/div/div/div/div[@id="info"]/p/a[contains(@href,"html")]/text()')

#打印内容
for each in content:
    print(each)

for each in content2:
    print(each)


#html中的先抓大再抓小
content3=selector.xpath('//body/div/div/div[@id="list"]')  #先抓大
chapter_list=content3[0].xpath('dd/a/@title')  #再抓小   可省略两道斜线
for each in chapter_list:
    print(each+'2')

#使用string(.)进行先抓大再抓小
content4=selector.xpath('//body/div/div/div[@id="list"]')[0]
chapter_list2=content4.xpath('string(.)')
print(chapter_list2)




















