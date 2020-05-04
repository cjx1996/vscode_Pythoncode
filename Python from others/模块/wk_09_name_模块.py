# 全局变量,函数,类,注意: 直接执行的代码不是向外界提供的工具!

# 文件被导入时, 能够直接执行的代码不需要被执行!


def say_hello():
    print("hello world")


if __name__ == "__main__":
    print("直接执行!!!")
    print(__name__)

    say_hello()
