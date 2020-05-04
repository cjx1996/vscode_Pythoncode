name = "帅帅"


# 需求 3
def print_line3(line, num):
    print(line * num)


print_line3("+", 50)


# 需求4
def print_line4(line, num):
    """
    打印多行分割线
    :param line: 分割线字符
    :param num: 分割线数量
    """
    row = 0
    while row < 5:
        print(line * num)

        print("")  # 换行
        row += 1


print_line4("-", 50)