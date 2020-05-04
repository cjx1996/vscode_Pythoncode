# 1.定义一个整数的变量记录循环的次数
i = 0

# 2.开始循环
while i < 10:
    # 满足条件, 循环结束
    print("hello python")
    if i > 3:
        break
    # 处理计数器
    i += 1

# 1.定义一个整数的变量记录循环的次数
j = 0

# 2.开始循环
while j < 5:
    # 满足条件, 循环结束

    if j == 3:
        j += 1
        continue
    # 处理计数器
    print(j)
    j += 1