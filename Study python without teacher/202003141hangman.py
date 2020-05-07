'''
本次为综合练习章节，开发名为‘hangman’的小游戏，具体规则如下：
1、玩家一挑选一个秘密单词，单词中有多少个字母，则划多少条横线
2、玩家二每次猜一个字母。
3、如果玩家二猜测的字母正确，玩家一将下划线修改为正确的字母，如果单词中有一个字母出现两次，玩家二也必须猜两次。
如果玩家二猜测错误，玩家一则画出上吊的人的一部分身体（从头部开始）。
4、如果玩家二在玩家一画完上吊的人之前猜对单词，玩家二胜利，反之失败。
在编写的程序中，计算机将扮演玩家一，用户扮演玩家二。
'''

def hangman(word):
    '''
    定义保存游戏的函数，定义个变量
    :param word:str
    :param rletters:list,将word中的各个字母组成list
    :param board:list 根据word的大小定义'_'数目
    :param win:bool 定义玩家二是否获胜
    '''
    #第一部分
    wrong=0
    stages=["",
    "_________           ",
    "|                   ",
    "|         |         ",
    "|         0         ",
    "|        /|\\        ",
    "|        / \\        ",
    "|                   "

    ]
    
    rletters=list(' '.join(word))
    board=['_',' ']*len(word)
    win=False
    print('Welcome to Hangman.')

    #第二部分
    '''
    一个维持游戏运行的循环
    '''
    while wrong<len(stages)-1:
        print('\n')
        msg='Guess a letter:'
        char=input(msg)
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]='-'
        else:
            wrong+= 1
        print(''.join(board))
        e=wrong+1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print("You win!")
            print(word)
            win=True
            break
    if not win:
        print('\n'.join(stages[0:wrong]))
        print('You lose! It was \"{}\"'.format(word))

#此处添加了单词列表，从列表中随机选取单词，增加了游戏的复杂性
letters=['good','kick','doctor','actor','will','when','who','are','is','am']
letters.append('browse')
letters.append('keyboard')
import random
t=random.randint(0,len(letters))
hangman(letters[t])















