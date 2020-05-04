class Cat:
    """这是一个猫类"""

    def eat(self):

        print("%s 爱吃鱼" % self.name)

    def drink(self):

        print("%s 要喝水" % self.name)


# 创建猫对象
tom = Cat()

tom.name = "Tom"
tom.eat()
tom.drink()

print(tom)

# 再创建一个猫对象
lazy_cat = Cat()

lazy_cat.name = "大懒猫"
lazy_cat.eat()
lazy_cat.drink()

print(lazy_cat)

