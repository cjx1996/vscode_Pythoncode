import requests
import os

i=366

#建立文件url及header
part1='http://159.226.241.32:8093/asserts/3fe2234d0f694b0e9961812bf73ad78c/image/{}/100?'.format(i-1)
part2='accessToken=accessToken&formMode=true&islarge=true&extenParams='
part3='{"type":"restful","url":"http://book.sciencereading.cn/shop/book/Booksimple/getReadablePages.do","method":"get","heads":{},"params":'
part4='{"member_id":"guestUser","book_id":"B58A6236D81858334E053020B0A0A3528000","role_id":"","user_ip":"60.12.8.167"}}\n'      
newline=part1+part2+part3+part4
header={'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Mobile Safari/537.36',
        'Referer':'http://book.sciencereading.cn/shop/book/Booksimple/onlineRead.do'
        ,'Accept':'image/webp,image/apng,image/*,*/*;q=0.8'
        ,'Host':'159.226.241.32:8093'
        ,'Connection':'keep-alive'
        ,'Accept-Encoding':'gzip, deflate'
        ,'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8'
}
url='''
    http://159.226.241.32:8093/asserts/688b781063d841e4b52bf75f16b64687/annots/210?formMode=true&pageIndex=210&extenParams=%7B%22type%22%3A%22restful%22%2C%22url%22%3A%22http%3A%2F%2Fbook.sciencereading.cn%2Fshop%2Fbook%2FBooksimple%2FgetReadablePages.do%22%2C%22method%22%3A%22get%22%2C%22heads%22%3A%7B%7D%2C%22params%22%3A%7B%22member_id%22%3A%22guestUser%22%2C%22book_id%22%3A%22B58A6236D81858334E053020B0A0A3528000%22%2C%22role_id%22%3A%22%22%2C%22user_ip%22%3A%2260.12.8.167%22%7D%7D
  '''

while i<=366:
    #建立文件名及索引地址
    file_name=str(i)+'.png'
    file_path=os.path.join('d://','迅雷下载','数学大辞典',file_name)

    
   
    #读取url内容，并写入文件
    r=requests.get(newline)
    with open(file_path,'wb')as f:
        print(r.content)
        f.write(r.content)
        f.close
    i=i+1
  






























