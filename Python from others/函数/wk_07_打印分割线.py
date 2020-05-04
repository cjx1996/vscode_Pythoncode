# 需求 1
def print_line1():
    print("*" * 50)


print_line1()


# 需求 2
def print_line2(line):
    print(line * 50)


print_line2("-")


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


# 需求5
def print_line5(num):
    """
    :param num: 要打印的行数
    """
    row = 0
    while row < num:
        print_line3("+", 50)
        print("")
        row += 1

print_line5(5)