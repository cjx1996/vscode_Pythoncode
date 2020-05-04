class Cat:

    def __init__(self, new_name):
        # self.属性名 = 属性的初始值
        self.name = new_name

        print("%s 来了" % self.name)

    def __del__(self):

        print("%s 走了" % self.name)


# tom是全局变量,会在分割线下执行del方法
tom = Cat("Tom")

# 使用 del 关键字可以删除一个对象, 销毁了, 就会在分隔线之前执行
# del tom

print("-" * 50)






