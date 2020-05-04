# 1. 打开文件
file = open("README")
file2 = open("README2", "w")

# 2. 读, 写文件内容
text = file.read()
file2.write(text)

# 3. 关闭
file.close()
file2.close()