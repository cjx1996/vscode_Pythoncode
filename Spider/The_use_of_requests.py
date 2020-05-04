import requests
import random
import csv
import re

#使用get方式获取网页内容
html=requests.get('http://exercise.kingname.info/exercise_requests_get.html').content.decode()
print('html:\n'+html)


#使用formdata方式获取网页内容
data={'name':'yigeren','password':1234}
html_formdata=requests.post('http://exercise.kingname.info/exercise_requests_post',data=data).content.decode()
print('formdata方式获取网页内容:\n'+html_formdata)


#使用json方式获取网页内容
html_formdata2=requests.post('http://exercise.kingname.info/exercise_requests_post',json=data).content.decode()
print('json方式获取网页内容:\n'+html_formdata2)


#获取页面标题
title=re.search('<title>(.*?)</title>',html,re.S).group(1)
print('网页标题为:'+title)


#提取正文
content_list=re.findall('<p>(.*?)</p>',html,re.S)
content_str='\n'.join(content_list)
print('网页正文内容为:'+content_str)














