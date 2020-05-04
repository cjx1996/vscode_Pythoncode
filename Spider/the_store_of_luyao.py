import re
from multiprocessing import Pool,freeze_support
import requests
import os
import json




#定义目录页网址为start_url
start_url='https://www.kanunu8.com/book3/8365/'


#获取目录页的源代码    
source=requests.get('https://www.kanunu8.com/book3/8365/').content.decode('gbk')


#获取各章节地址
cha_url_list=[]
cha_block=re.findall('作者：(.*?)上一篇：',source,re.S)[0]
cha_url=re.findall('a href="(.*?)"',cha_block,re.S)
for url in cha_url:
    cha_url_list.append(start_url+url)

#根据各章节地址列表保存,若存在则什么都不做，否则创建文件并保存
chapters_json = 'e:/code/vscode_Pythoncode/Spider/Chapters.json'
try:
    with open(chapters_json) as f_obj:
        pass
except FileNotFoundError:
    with open(chapters_json,'w')as f_obj:
        json.dump(cha_url_list, f_obj)

#创建已下载章节列表及文件，不断读取并不断加载
chapters_download_json= 'e:/code/vscode_Pythoncode/Spider/Chapters_download.json'
try:
    with open(chapters_download_json)as f_obj:
        chapters_download_list = f_obj.read().split()
except FileNotFoundError:
    
    with open(chapters_download_json,'w')as f_obj:
        pass
    chapters_download_list=[]
        


#定义根据得到的章节源代码提取正文和标题
def get_article(html):
    '''
    获取每一章的正文并返回章节名和正文
    :param html:正文源代码
    ：return:章节名，正文
    '''

    chapter_name=re.search(' size="4">(.*?)</font><strong>',html,re.S).group(1)
    text_block=re.search('<p>(.*?)</p>',html,re.S).group(1)
    text_block=text_block.replace('<br />','')
    text_block=text_block.replace('&nbsp;&nbsp;&nbsp;&nbsp;','    ')
   
    return chapter_name,text_block


#根据正文和标题保存到本地文件夹
def save(chapter,article):
    '''
    将每一章保存在本地。
    :param chapter:章节名，第X章
    :param article:正文内容
    :return:None
    '''
    #如果没有“平凡的世界”文件夹，就创建一个，如果有，则什么都不做
    os.makedirs('e:/code/vscode_Pythoncode/Spider/平凡的世界',exist_ok=True)
    with open(os.path.join('e:/','code','vscode_Pythoncode','Spider','平凡的世界',chapter+'.txt'),'w',encoding='utf-8')as f:
        f.write(article)
    

#根据url获得章节源代码并调用保存函数
def action(url):
    html=requests.get(url).content.decode('gbk')
    with open(chapters_download_json,'a') as f_obj:
        f_obj.write(url+'\n')
        
    (chapter,article)=get_article(html)
    save(chapter,article)


#main函数下进程
if __name__ == '__main__':
    
        pool=Pool(5)
       
        pool.map(action,list(set(cha_url_list).difference(set(chapters_download_list)))) 
    