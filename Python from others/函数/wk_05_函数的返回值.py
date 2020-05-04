def sun_sum(num1, num2):
    """"两个数求和"""
    result = num1 + num2
    # 使用返回值,  告诉调用函数一方计算的结果
    return result
    # 注意: return 就表示返回, 下方的代码不会被执行

# 使用变量接收


sum_result = sun_sum(2, 5)

print("计算结果: %d" % sum_result)
