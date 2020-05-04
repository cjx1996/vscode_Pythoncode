xiaoming = {"name": "小明",
            "age": 18}

# 1. 统计键值对数量
print(len(xiaoming))

# 2. 合并字典
temp_dict = {"height": 1.75,
            "age": 20}
# 注意: 如果要合并的字典存在相同键, 会覆盖原字典上的键值
xiaoming.update(temp_dict)


# 3. 清空字典
xiaoming.clear()
