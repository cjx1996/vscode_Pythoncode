#question3
class Shape():
    def __init__(self):
        pass
    def what_am_i(self):
        print('I am shape')






#question1
class Rectangle(Shape):
    def __init__(self,w,l):
        self.width=w
        self.len=l

    def calculate_perimeter(self):
        return 2*(self.width+self.len)


class Square(Shape):
    def __init__(self,s):
        self.side=s


    def calculate_perimeter(self):
        return 4*self.side

    #question2
    def change_size(self,number):
        self.side=self.side+number

tr1=Rectangle(30,40)
sqr1=Square(45)
shapes=[tr1,sqr1]

for shape in shapes:
    print(shape.calculate_perimeter())
    shape.what_am_i()

#question2
sqr1.change_size(4)
print(sqr1.calculate_perimeter())


#question4
class Horse():
    def __init__(self,size,weight,owner):
        self.size=size
        self.weight=weight
        self.owner=owner


class Rider():
    def __init__(self,name):
        self.name=name
    

rid1=Rider('Bob')
hs1=Horse(3,100,rid1)
print(hs1.owner.name)





















































