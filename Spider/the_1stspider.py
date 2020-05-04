#!/user\bin\python
#coding:utf-8
import requests
link="http://grs.hdu.edu.cn/"
headers={'User-Agent':'Mozilla/5.0(Windows;U;Windows NT6.1;en-US;rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r=requests.get(link,headers=headers)
print(r.text)