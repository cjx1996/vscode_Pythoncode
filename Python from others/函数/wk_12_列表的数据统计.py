name_list = ["张三", "李四", "王五"]

# len(length 长度) 函数可以统计列表中元素的总数
name_len = len(name_list)
print("列表中包含了%d 个元素" %name_len)

# count 方法可以统计里边中某一个数据出现的次数
count = name_list.count("张三")
print("张三出现了 %d 次" % count)