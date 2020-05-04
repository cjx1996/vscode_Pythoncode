import re
content='my weibo password is:1234567,QQ password is:33445566,credit card password is:8888888,Github password is:9999abc99999,help me remember them.'
#findall和search方法的使用
password_list=re.findall(':(.*?),',content)
name_list=re.findall('名字是(.*?)',content)
print('找到内容，返回：{}'.format(password_list))
print('找不到内容，返回:{}'.format(name_list))
password_search=re.search('password is:(.*?),',content)
password_search_no_find=re.search('xxx:(.*?),',content)
print(type(password_search))
print(password_search)
print(password_search.group())
print(password_search.group(0))
print(password_search.group(1))
print(password_search_no_find)
#先抓大再抓小
content2='有效用户：\n姓名：张三\n姓名：李四\n姓名：王五\n无效用户：\n姓名：不知名的小虾米\n姓名：隐身的张大侠'
user_big=re.findall('有效用户(.*?)无效用户',content2,re.S)
user_useful=re.findall('姓名：(.*?)\n',user_big[0])
#打印user_big
print(user_big)
print(user_big[0])
#打印user_useful
print(user_useful)
print(type(user_big))
print(type(user_useful))












