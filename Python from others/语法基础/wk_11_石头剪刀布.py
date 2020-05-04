# 导入随机工具包
import random

# 从控制台输入要出的拳 ---石头 (1) / 剪刀 (2) / 布 (3)
player = int(input("请输入您要出的拳 石头 (1) / 剪刀 (2) / 布 (3)"))

# 电脑 随机 出拳
computer = random.randint(1, 3)

print("玩家出的是%d - 电脑出的是%d" % (player, computer))

if ((player == 1 and computer == 2)
        or(player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
        print("赢了哟!")
elif player == computer:
    print("平局, 再来!")
else:
    print("遗憾, 败北!")
