#question 10-6
def pulse():
    try:
        num1 = input('Enter the first number:')
        num2 = input('Enter the second number:')
        num1 = int(num1)
        num2 = int(num2)
        print( num1 + num2 )

    except ValueError:
        print('You should input number but not others.')

#question 10-7
while True:
    try:
        print('Enter the "q" to exit.')
        num1 = input('Enter the first number:')
        if num1 == 'q':
            break
        num2 = input('Enter the second number:')
        if num2 == 'q':
            break
        num1 = int(num1)
        num2 = int(num2)
        print( num1 + num2 )

    except ValueError:
        print('You should input number but not others.')









































