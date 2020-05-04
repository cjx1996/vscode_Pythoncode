#定义换行标记
newline='************************************************************'


#字符串大小写问题
print('1、字符串大小写问题')
name='ada lovelace'
print(name.title()+'\t这是将单词视为姓名')
print(name.upper()+'\t这是将单词完全大写')
print(name.lower()+'\t这是将单词完全小写')
print(newline)


#字符串合并（拼接）问题
print('2、字符串合并（拼接）问题')
first_name='ada'
last_name='lovelace'
fullname=first_name+' '+last_name
print(fullname+'\t\t这是字符串拼接')
print('Hello, '+fullname.title()+'！'+'\t这是一句格式良好的简单问候语')
message='Hello, '+fullname.title()+'!'
print(message+'\t这是将问候语句储存在变量中')
print(newline)


#使用制表符和换行符
print('3、制表符与换行符的使用')
print('Python'+'\t\t这是未添加制表符的输出')
print('\tPython'+'\t这是添加了制表符的输出'+'(制表符代表当前八个字符已经结束，开始新的八个字符)')
print('Languages:\nPyhon\nC\nJavaScript\t\t这是换行符的使用')
print('Languages:\n\tPyhon\n\tC\n\tJavaScript\t这是换行符加上制表符的使用')
print(newline)


#删除空白
print('4、删除空白')
favourite_language=" 'python ' " 
print(favourite_language)
print(favourite_language.lstrip())
print(favourite_language)
favourite_language=favourite_language.lstrip()
print(favourite_language)
print(favourite_language.strip())
print(newline)


#使用字符串避免语法错误
print('5、使用字符串避免错误')
message="One of Python's strengths is its diverse community."
print(message+'\t句子里有单引号则字符串用双引号，有双引号则用单引号')
texts='my mother has said"I\'m very proud of my age"'
print(texts+'\t\t既有单引号又有双引号时使用转义字符\\')
print('\\n \\t \\'+'\t\t\t\t\t\t\t转义字符\\可用于打出各特殊含义代码')
print(newline)


#6、小结
print('6、小结')
print('本章主要学习：')
a='varable\nstring\nthe use of the function of stripe\nthe use of int and float\nthe use of annotation\nthe principle of programming'
print(a)















































































