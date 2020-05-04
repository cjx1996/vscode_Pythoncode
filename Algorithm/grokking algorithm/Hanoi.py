def move(x,y):
    print('move '+x+' to '+y)
x='A'
y='B'
z='C'
def hanoi(n,x,y,z):
    

    if n==1:
        move(x,y)
    elif n>1:
        hanoi(n-1,x,z,y)
        move(x,y)
        hanoi(n-1,z,y,x)
    else:
        print("The wrong input!")


hanoi(10,x,y,z)