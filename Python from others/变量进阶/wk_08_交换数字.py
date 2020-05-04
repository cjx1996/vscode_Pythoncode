# 需求:a, b 数字交换
a = 6
b = 100

# 1. 使用其他变量
c = a
a = b
b = c
# 2. 不使用其他变量
a = a + b
b = a - b
a = a - b
# 3. 元组, 括号可以省略(Python专有)
a, b = b, a

print(a)
print(b)

