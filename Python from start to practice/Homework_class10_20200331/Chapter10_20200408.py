import json
import os
def save_the_new_number():
    '''
    得到用户最喜欢的数字
    '''
    number = input('What is your favourite number?')
    filename = 'e:/code/vscode_Pythoncode/Python from start to practice/favourite_number.json'
    with open (filename,'w')as f:
        json.dump(number,f)
    return number


def load_the_number():
    '''
    从文件中读取数字
    '''
    try:
        filename = 'e:/code/vscode_Pythoncode/Python from start to practice/favourite_number.json'
        with open (filename,'r')as f:
            number = json.load(f)
            return number
    except FileNotFoundError:
        return None
    

def print_message():
    '''
    打印相应消息
    '''
    number = load_the_number()
    if number:
        number = number
    else:
        number = save_the_new_number()
    print(f"I know your favourite number! It\'s {number}.")

print_message()










