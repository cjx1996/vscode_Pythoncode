# 要求: 居中对齐以下内容

poem = ["连峰去天不盈尺,",
        "枯松倒挂倚绝壁."]

for poem_str in poem:
    # 居中对齐
    print("|%s|"%poem_str.center(20, " "))

poem1 = ["连峰去天不盈尺,",
        "枯松倒挂倚绝壁."]


for poem_str in poem1:
    # 左对齐 右对齐rjust
    print("|%s|"%poem_str.ljust(20, " "))
