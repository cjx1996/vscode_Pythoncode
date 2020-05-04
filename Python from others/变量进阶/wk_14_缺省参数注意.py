def print_info(name, title, gender=True):
    """

    :param title: 职位
    :param name: 姓名
    :param gender: True 男生 False 女生
    """

    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("%s 是 %s" % (name, gender_text))


# 假设默认男生多
# 提示: 在指定缺省参数的默认值时, 应该使用最常见的值作为默认值!
print_info("xiaoming")
print_info("xiaoxue", False)