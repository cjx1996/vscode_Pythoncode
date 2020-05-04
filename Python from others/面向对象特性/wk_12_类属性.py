class Tool(object):

    # 使用赋值语句定义类属性, 记录所有工具对象的数量
    count = 0

    def __init__(self, name):
        self.name = name

        # 让类属性的值+1
        Tool.count += 1


# 1. 创建工具对象
tool1 = Tool("剪刀")
tool2 = Tool("石头")
tool3 = Tool("布")

print(Tool.count)