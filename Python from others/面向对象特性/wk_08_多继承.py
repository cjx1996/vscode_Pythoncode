class A:

    def test_a(self):
        print("父类A")


class B:

    def test_b(self):
        print("父类B")


class C(A, B):
    """多继承可以让子类对象, 同时具有多个父类的属性和方法"""
    pass


# 创建子类
c = C()
c.test_a()
c.test_b()