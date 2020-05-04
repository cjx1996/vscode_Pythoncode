print([1, 2]*5)
print((1, 2)*5)
print("12" + "34")
print((1, 2) + (3, 4))
print([1, 2] + [3, 4])  # 合并成一个新的数组
t_list = [1, 2]
t_list.extend([3, 4])  # 在原基础上增加
print(t_list)  # [1, 2, 3, 4]
t_list.append(0)
print(t_list)  # [1, 2, 3, 4, 0]
t_list.append([7, 8])
print(t_list)  # [1, 2, 3, 4, 0, [7, 8]]


