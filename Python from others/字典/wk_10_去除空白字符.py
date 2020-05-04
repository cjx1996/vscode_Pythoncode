poem = ["\t\n飞流直下三千尺",
        "疑是银河落九天"]

for poem_str in poem:
    # 先使用strip方法去除字符串中的空白字符
    # 再使用center 方法居中
    print("|%s|"%poem_str.strip().center(20, " "))