import json

'''
---------------------------
2020.4.8        重构代码，划分函数

-------------------------------------------





------------------------------
'''


def get_stored_username():
    '''
    如果存储了用户名，就获取它
    '''
    filename = 'e:/code/vscode_Pythoncode/Python from start to practice/username.json'
    try :
        with open(filename)as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
        

def get_new_username():
    '''
    提示用户输入用户名
    '''
    username = input('What is your name?')
    filename = 'e:/code/vscode_Pythoncode/Python from start to practice/username.json'
    with open (filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def if_the_same_one(username):
    '''
    让用户判断是否是上一次的人
    '''
    if username:
        while True:
            decision = input(f'Are you {username}? Input Yes or No:')
            decision = decision.capitalize()
            if decision =='Yes' or decision =='No':
                return decision
    else:
        return 'No'
        
            


def greet_user():
    '''
    问候用户，并指出其名字
    '''
    username = get_stored_username()
    decision = if_the_same_one(username)

    if decision == 'Yes':
        print(f'Welcome back, {username}!')
    if decision == 'No':
        username = get_new_username()
        print(f'we\'ll remember you when you come back, {username}!')
  
greet_user()


#写入数据到文件
numbers = [2,3,5,8,13,21]
filename = 'e:/code/vscode_Pythoncode/Python from start to practice/numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

#载入数据

with open (filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)
















