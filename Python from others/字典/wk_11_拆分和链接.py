poem = "\t\n飞流直下三千尺\t疑\n是银河落九天"

print(poem)

# 1. 拆分字符串, split() 里面以什么分隔成列表
poem_list =poem.split()
print(poem_list)

# 2. 合并字符串
result = "".join(poem_list)
print(result)
