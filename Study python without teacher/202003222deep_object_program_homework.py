#question1
class Square:
    square_list=[]


    def __init__(self,side):
        self.side=side
        self.square_list.append(self.side)
    

    #question2
    def print_size(self):
        print('{} by {} by {} by {}'.format(self.side,self.side,self.side,self.side))


#question1
sq1=Square(12)
sq2=Square(39)
sq3=Square(49)
sq4=Square(69)
print(Square.square_list)

#question2
sq1.print_size()

#question3
class Person():
    def __init__(self,age,weight,height):
        self.age=age
        self.weight=weight
        self.height=height
    
def personsifsame(p1,p2):
    if p1 is p2:
        return True
    if p1 is not p2:
        return False 
        
p1=Person(12,40,140)
p2=Person(12,40,140)
p3=p1
print(p1)
print(p2)
print(p3)
print(personsifsame(p1,p2))
print(personsifsame(p1,p3))










































































































































































