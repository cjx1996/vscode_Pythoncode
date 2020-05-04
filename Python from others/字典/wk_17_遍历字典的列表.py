students = [
    {"name": "小明"},
    {"name": "大明"}
]

# 在学员列表中搜索指定的名字
find_name = "大明"
for stu_dict in students:

    print(stu_dict)

    if stu_dict["name"] == find_name:
        print("找到了 %s" % stu_dict["name"])
        # 如果找到了, 应该退出循环
        break
else:
    # 如果搜索列表时, 所有的字典检查都没有这个人, 就执行这句代码
    # 就是执行了 break 就不会执行这句代码, 没有就会执行这句
    print("没有找到 %s" % find_name)

print("循环结束")