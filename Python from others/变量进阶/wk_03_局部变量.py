def demo1():

    # 定义一个局部变量
    # 1. 执行了下方的代码之后, 才会被创建
    num = 10

    print("在demo1函数内部的变量是 %d" % num)


def demo2():

    # 局部变量同名的变量不会影响
    num = 100

    print("在demo1函数内部的变量是 %d" % num)

# 在函数内部定义的变量, 不能再其他位置使用
# print("%d" % num)


demo1()


demo2()