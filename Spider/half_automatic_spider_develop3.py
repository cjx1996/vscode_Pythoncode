#coding:utf-8
import re
import csv


#逻辑上更合理的代码
#首先获得每一层的代码
with open('E:/code/vscode_Pythoncode/Spider/source.txt','r',encoding='UTF-8') as f:
    source=f.read()
every_reply=re.findall('l_post l_post_bright j_l_post clearfix(.*?)p_props_tail props_appraise_wrap',source,re.S)

#从每一层文本里进行提取发帖人姓名，内容，楼层，发帖时间
result_list=[]
for each in every_reply:
    result={}
    
    result['username']=re.findall('img username="(.*?)" class=',each,re.S)[0]
    result['content']=re.findall('d_post_content j_d_post_content " style="display:;">            (.*?)<',each,re.S)[0]
    result['floor']=re.findall('</a></span><span class="tail-info">.*?(\\d*楼)</span><span class=',each,re.S)[0]
    result['reply_time']=re.findall('楼</span><span class="tail-info">(.*?)</span></div>',each,re.S)[0]
    result_list.append(result)


#将得到的提取内容写入csv文件
with open('e:/code/vscode_Pythoncode/Spider/tieba2.csv','w',encoding='gbk',newline='') as f :
    writer=csv.DictWriter(f,['floor','username','content','reply_time'])
    writer.writeheader()
    writer.writerows(result_list)





















