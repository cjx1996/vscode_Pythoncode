# 定义一个行变量
row = 1
# 第一个循环, 循环次数代表多少行数
while row <= 9:
    # 定义一个列变量
    col = 1
    # 第二个循环, 代表每一行循环出来的内容
    while col <= row:
        print("%d * %d = %d" % (col, row, row*col), end="\t")
        col += 1
    print("")
    row += 1
