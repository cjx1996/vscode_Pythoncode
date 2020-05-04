def demo(*args, **kwargs):

    print(args)
    print(kwargs)


# 元组变量/字典变量
gl_nums = (1, 2, 3)
gl_dict = {"name": "小明", "age": 18}


demo(gl_nums, gl_dict)

# 打印结果 -- 都传给了args
# ((1, 2, 3), {'name': '小明', 'age': 18})
# {}


#  两者相同
demo(*gl_nums, **gl_dict)  # 拆包语法
demo(1, 2, 3, name="小明", age=18)  # 常规写法
# 打印结果
# (1, 2, 3)
# {'name': '小明', 'age': 18}


