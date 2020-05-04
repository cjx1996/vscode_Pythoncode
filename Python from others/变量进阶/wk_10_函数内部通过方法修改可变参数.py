def demo(num, num_list):

    print("函数内部的代码")

    # 使用方法修改列表的内容
    num += num
    # 本质上是在动用列表的 extend 方法
    num_list += num_list
    print(num)
    print(num_list)
    print("函数执行完成")


gl_num = 2
gl_list = [1, 2, 3]
demo(gl_num, gl_list)

print(gl_num)
print(gl_list)

# 函数执行结果
# 4
# [1, 2, 3, 1, 2, 3]
# 函数执行完成
# 2
# [1, 2, 3, 1, 2, 3]