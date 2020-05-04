# 注意: 定义好函数之后, 只表示这个函数封装了一段代码而已
# 如果不主动调用函数, 函数是不会主动执行的
# 代码规范函数上面要空两行

name = "kkw"


def say_hello():
    print("hello world")
    print("hello world")
    print("hello world")


print(name)
# 只用在调用函数时,  之前定义的函数才会被执行
# 函数执行完成之后,  会重新回到之前的程序中,  继续执行后续的代码
say_hello()

print(name)

# 执行结果 :
# kkw
# hello world
# kkw

