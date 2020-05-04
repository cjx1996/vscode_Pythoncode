# 1. 打开文件
file = open("README")

# 2. 读取文件内容
while True:
    text = file.readline()

    #  判断时候有内容
    if not text:
        break
    print(text)

# 3. 关闭
file.close()
