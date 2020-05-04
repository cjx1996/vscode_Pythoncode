#coding:utf-8
import urllib.request
import re
import requests
import os
from multiprocessing import Pool,freeze_support

#根据url爬取，以作家分类爬取小说

class Chapter:
    #定义章节类，对每本书由最基础的章节构成。
    def __init__(self, book_place):
        '''
        :param url:str,章节的url
        '''
        
        self.place = book_place
    def save(self,url):
        '''
        :param place:path,where save this chapter 
        '''
        html = requests.get(url).content.decode('gbk')
        chapter_name=re.search(' size="4">(.*?)</font><strong>',html,re.S).group(1)
        text_block=re.search('<p>(.*?)</p>',html,re.S).group(1)
        text_block=text_block.replace('<br />','')
        text_block=text_block.replace('&nbsp;&nbsp;&nbsp;&nbsp;','    ')
        if  not  os.path.exists(self.place + '/' + chapter_name +'.txt'):

            with open(self.place + '/' + chapter_name + '.txt','w',encoding='utf-8')as f:
                f.write(text_block)
        print('This chapter complete.'+chapter_name)
    def __repr__(self):
        '''
        定义打印或调用类对象时的输出
        '''
        return self.place

class Book:
    def __init__(self,book_url,author_place):
        '''
        :param url:url,书籍对应url
        :param place:path,书籍将要保存在电脑的位置
        '''
        self.url = book_url   
        self.place = author_place 
        (self.cha_url_list,self.book_name) = self.get_chapters_list_and_name()
        
    
        '''
        for url in self.cha_url_list:
            url = url
            self.book_chapters.append(Chapter(self.place+'/'+self.book_name))
        '''
    def get_chapters_list_and_name(self):
        '''
        :return cha_url_list:list,章节url列表
        '''
        #获取目录页的源代码    
        source=requests.get(self.url).content.decode('gbk')
        #获取各章节地址
        cha_url_list=[]
        cha_block=re.findall('作者：(.*?)上一篇：',source,re.S)[0]
        cha_url=re.findall('a href="(.*?)"',cha_block,re.S)
        for url in cha_url:
            url = url
            cha_url_list.append(self.url  + url)

        #获取书籍名称
        book_name = re.findall('<font color="#dc143c">(.*?)</font>',source,re.S)[0]

        return cha_url_list,book_name
    def save(self):
        '''
        保存书籍
        '''
        self.mkdir()
        print('1')
        
        if __name__ == "__main__":
            pool = Pool(5)
            pool.map(Chapter(self.place + '/' + self.book_name).save,self.cha_url_list)
        
        print('2') 
        print('this book complete.'+self.book_name)  
      
        
    def mkdir(self):
        '''
        创建目录
        '''
        os.makedirs(self.place+'/'+self.book_name,exist_ok=True)
    def __repr__(self):
        '''
        定义打印或调用对象时输出内容
        '''
        return self.book_name

class Author:
    def __init__(self, author_url, place):
        self.url = author_url
        self.place = place
        (self.book_url_list,self.author_name) = self.get_lists_and_name()
        self.author_books =[]
        for url in self.book_url_list:
            self.author_books.append(Book(url,self.place +'/'+ self.author_name))
    def get_lists_and_name(self):
        '''
        返回书籍url列表
        '''
        #获取目录页的源代码    
        source=requests.get(self.url).content.decode('gbk')
        #获取各章节地址
        book_url_list=[]
        #cha_block=re.findall('作者：(.*?)上一篇：',source,re.S)[0]
        book_url=re.findall('<a target="_blank" href="(.*?)index.html">',source,re.S)
        for url in book_url:
            book_url_list.append('https://www.kanunu8.com'  + url)

        #获取作者姓名
        author_name = re.search('<Td height="60" valign="middle" align="center"><h2><b>(.*?)</b></h2></Td>',source,re.S).group(1)
        
        return book_url_list,author_name
    
    def mkdir(self):
        '''
        创建作者文集目录
        '''

        os.makedirs(self.place + '/' +self.author_name,exist_ok=True)

    def save(self):
        '''
        保存该作者文集
        '''
        self.mkdir()
        for item in self.author_books:
            item.save()
        print('This author complete!')

url = 'https://www.kanunu8.com/files/writer/4366.html'    
path ='e:/code/vscode_Pythoncode/Spider'
author1= Author(url,path)
author1.save()  






















