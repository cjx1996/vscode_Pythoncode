class Person:

    def __init__(self, name, height):

        # self.属性 = 形参
        self.name = name
        self.height = height

    def __str__(self):

        return "我的名字叫 %s 体重是 %.2f 公斤" % (self.name, self.height)

    def run(self):
        print("%s 爱跑步, 跑步锻炼身体" % self.name)
        self.height -= 0.5

    def eat(self):
        print("%s 喜欢吃东西, 吃东西好快乐" % self.name)
        self.height += 1


xiaoming = Person("小明", 70)

xiaoming.run()
xiaoming.eat()

print(xiaoming)





