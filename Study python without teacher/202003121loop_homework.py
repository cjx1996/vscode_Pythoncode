#question1
for i in ['The Walking Dead','Entourage','The Sopranas','The Vampire Diaries']:
    print(i)

#question2
for i in range(25,51):
    print(i)

#question3
x=[
    "The Walking Dead",
    'Entourage',
    'The Sopranas',
    'The Vampire Diaries'
]
for i in range(0,len(x)):
    print(i)
    print(x[i])

#question4
list_nunber=[1,2,4,5,44,23,54,66,43,23,6652,323]
'''
while True:
    letter=input("Enter q to exit:")
    if letter!='q':
        number=input("Guess a number:")
        try:
            number=int(number)
            if number in list_nunber:
              print('You are right!')
            else:
                print('Sorry, you are wrong.')
        except Exception:
            print("You should type the number!")
    else:
        break
'''

#question5
list1=[8,19,148,4]
list2=[9,1,33,83]
added=[]
for i in list1:
    for j in list2:
        added.append(i*j)
print(added)

























