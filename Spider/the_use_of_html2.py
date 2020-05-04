import lxml.html
import requests


#获取url对应源代码
source=requests.get('https://tieba.baidu.com/f?kw=%E8%B5%98%E5%A9%BF&ie=utf-8').content.decode()


#获取相应网页源代码
selector=lxml.html.fromstring(source)


#获取帖子标题
content=selector.xpath('//div[@class="col2_right j_threadlist_li_right "]/div[@class="threadlist_lz clearfix"]/div[@class="threadlist_title pull_left j_th_tit "]/text()')

for each in content:
    print(each)












