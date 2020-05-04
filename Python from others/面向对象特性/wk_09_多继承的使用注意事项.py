class A:

    def test(self):
        print("父类A")


class B:

    def test(self):
        print("父类B")


class C(A, B):
    """多继承可以让子类对象, 同时具有多个父类的属性和方法"""
    pass


# 创建子类
c = C()
c.test()

# 确定 C 类对象调用方法的顺序
print(C.__mro__)

# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
