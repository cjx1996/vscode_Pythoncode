import os
file_path=os.path.join('E:\\','code','vscode_Pythoncode','download_list.txt')
i=0
j=1
with  open(file_path,'w')as f:
    while i<1447:
        if i%10==0:
            #f.write('#下面是从第'+str(j)+'幅图到第'+str(j+9)+'幅图\n')
            f.write('\r\n')
        part1='http://159.226.241.32:8093/asserts/688b781063d841e4b52bf75f16b64687/image/{}/100?'.format(i)
        part2='accessToken=accessToken&formMode=true&islarge=true&extenParams='
        part3='{"type":"restful","url":"http://book.sciencereading.cn/shop/book/Booksimple/getReadablePages.do","method":"get","heads":{},"params":'
        part4='{"member_id":"guestUser","book_id":"B58A6236D81858334E053020B0A0A3528000","role_id":"","user_ip":"60.12.8.167"}}\n'
        
        newline=part1+part2+part3+part4
        
        
        f.write(newline)
        if j%10==0:
            f.write('\r\n')
        i=i+1
        j=j+1












