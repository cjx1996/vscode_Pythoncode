class Cat:

    def __init__(self, new_name):

        self.name = new_name

        print("%s 来了" % self.name)

    def __del__(self):

        print("%s 走了" % self.name)

    def __str__(self):

        # 必须返回一个字符串
        return "我是一只猫%s" % self.name


# tom是全局变量,会在分割线下执行del方法
tom = Cat("Tom")
print(tom)

# 打印结果
# Tom 来了
# 我是一只猫Tom
# Tom 走了






