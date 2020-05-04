file_name = 'e:/code/vscode_Pythoncode/Python from start to practice/pi_digits.txt'   #absolute path
file_name = 'vscode_Pythoncode/Python from start to practice/pi_digits.txt'       #relative path

with open(file_name) as file_object:   
    contents = file_object.read()
    print(contents)
    print(contents.rstrip())

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    print(line.rstrip())
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))


#Error
try:
    print(5/0)
except ZeroDivisionError:
    print('You can\'t divide by zero.')


#use error to avoid break
print('Give me two numbers, and I\'ll divide them.')
print('Enter \'q\' to quit.')
    #test exception
'''
while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input('Second number: ')
    if second_number == 'q':
        break

    try:

        answer = int(first_number)/int(second_number)
    except Exception:
        print('You should enter right character.')
    else:
        print(answer)
'''


#analyse text
title = 'Alice in Wonderland'
print(title.split())

#do nothing while fails
def count_words(filename):
    '''计算一个文件大致包含多少个单词'''
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        #计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print('The file ' + filename + ' has about ' + str(num_words) +' words.')
filename = 'alice.txt'
count_words(filename)










