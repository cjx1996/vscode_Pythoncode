class Employee():
    '''存储雇员的信息'''
    def __init__(self, first, last, wage):
        '''
        定义雇员的基本信息，包括姓，名，年薪
        '''
        self.first = first
        self.last = last
        self.wage = wage

    def give_raise(self, number=5000):
        '''给员工增加年薪，默认增加5000,也可以增加其他值'''
        self.wage = self.wage + number


























