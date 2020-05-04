class Animal:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):

    def bark(self):
        print("叫")


class XiaoTianQuan(Dog):

    def fly(self):
        print("I can fly")


xtq = XiaoTianQuan()
xtq.run()
xtq.bark()
xtq.fly()
