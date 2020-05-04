# 1. 打开文件
file = open("README")
file2 = open("README2", "w")

# 2. 读, 写文件内容
while True:
    # 读取一行内容
    text = file.readline()
    # 判断时候读取到内容
    if not text:
        break
    # 每次写入文件指针会到文件的末尾
    file2.write(text)

# 3. 关闭
file.close()
file2.close()