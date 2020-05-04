xiaoming = {"name": "小明",
            "age": 18,
            "height": 1.75}

# 1. 取值
print(xiaoming['name'])

# 2. 增加 / 修改
xiaoming['address'] = "chengdu"
xiaoming['age'] = 19

print(xiaoming)

# 3. 删除

xiaoming.pop('age')
print(xiaoming)
