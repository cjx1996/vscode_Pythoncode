'''
In this file, we will try to develop the game named War.In this game, each player get a card.
The winner is the one whose card's number is the biggest.
'''
#定义卡牌类
class Card:
    suits=['spades','hearts','diamonds','clubs']#表示花色

    values=[      #表示数值
        None,     #前面两个None使得v的值和在values中位置相匹配
        None,
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        'Jack',
        'Queen',
        'King',
        'Ace'
    ]
    def __init__(self, v, s):
        '''
        suit和value的值都是整型数
        定义卡牌的两个属性，大小value和花色suit，除了此处外还需要将数值和列表list联系起来。
        '''
        self.value = v
        self.suit = s
    
    def __lt__(self,c2):
        '''
        根据魔法方法__lt__提供对'<'的重定义
        '''
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        '''
        根据魔法方法__gt__提供对'>'的重定义
        '''
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False
        
    def __repr__(self):
        '''
        定义类的字符串描述，当打印或查看某个对象时，返回给函数的返回值
        '''

        v = self.values[self.value] + ' of ' + self.suits[self.suit]
        return v

#表示牌堆的类
from random import shuffle
class Deck:
    '''
    根据Card类，创建包含52个Card类的对象，并随机打乱
    '''
    def __init__(self):
        self.cards = []
        for i in range (2, 15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)        #随机排列，模拟洗牌的动作

    def rm_card(self):
        '''
        根据pop函数，提供随机从卡牌堆抽取卡牌的函数
        '''

        if len(self.cards) == 0:
            return
        return self.cards.pop()





#玩家类
class Player:
    '''
    :param wins:int, 胜场数
    :param card:Card,目前手中抽取的卡牌
    :param name:str,玩家姓名
    
    '''
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


#表示游戏本身的类
class Game:
    def __init__(self):
        '''
        定义游戏本身的数据，两个玩家，一个牌堆。

        '''
        name1 = input('p1 name ')
        name2 = input('p2 name ')
        self.deck =Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        '''
        动作：输出每回合谁胜利
        '''
        w = "{} wins this round".format(winner)
        print(w)
    
    def draw(self, p1n, p1c, p2n, p2c):
        '''
        动作：输出每个玩家抽到什么牌

        '''
        d= '{} drew {} {} drew {}'.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards= self.deck.cards
        print('beginning War!')
        while len(cards)>=2:
            m= 'q to quit. Any' + 'key to play:'
            response=input(m)
            if response == 'q':
                break
            p1c= self.deck.rm_card()
            p2c= self.deck.rm_card()
            p1n= self.p1.name
            p2n= self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins+=1
                self.wins(self.p2.name)
        win = self.winner(self.p1,self.p2)

        print('War is over. {} wins'.format(win))

    def winner(self, p1, p2):
        '''
        动作：根据玩家对象的数据wins，输出游戏结果

        '''
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return 'It was a tie!'

game = Game()
game.play_game()


























