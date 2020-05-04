a = [1, 2, 3]
print("%s 的内存地址是 %d" % (a, id(a)))
a.remove(a[0])
print("%s 的内存地址是 %d" % (a, id(a)))  # 使用方法来改变数据, 内存地址不会发生改变

a = [0, 1, 2, 3]
print("%s 的内存地址是 %d" % (a, id(a)))  # 重新定义内存地址会发生改变, 因为引用地址变了

# 字典
d = {"name": "小明", 1: "整数", (1,): "元组"}  # 正确的

# l = {[1, 2]: "列表"}  # 会报错

# print(l)

print(hash(1))
print(hash("hello"))
print(hash("hello"))
print(hash("hello1"))
print(hash("(1,)"))




