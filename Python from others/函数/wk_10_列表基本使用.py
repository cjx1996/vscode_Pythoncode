name_list = ["zhangsan", "lisi", "wangwu"]

# 1. 取值和取索引
# list index out of range - 列表索引超出范围
# 取值
print(name_list[0])

# 取索引
print(name_list.index("wangwu"))

# 2. 修改
name_list[1] = "李四"

print(name_list)

# 3. 增加
# append 方法可以向列表的末尾追加数据
name_list.append("小明")
# insert 方法可以在列表的指定索引位置插入数据
name_list.insert(1, "大明")

# extend 方法可以把其他列表中的完整内容, 追加到当前列表的末尾
temp_list = ["一剪梅", "呵呵哒"]
name_list.extend(temp_list)

# 4. 删除
# remove 方法可以从列表中删除指定的数据
name_list.remove("wangwu")
# pop 方法默认可以把里边中最后一个元素删除
name_list.pop()
# pop 方法可以指定要删除元素索引
name_list.pop(4)
# clear 方法可以清空列表
name_list.clear()

print(name_list)