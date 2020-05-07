from pynput import keyboard,mouse

import pyautogui
import time
import pynput
'''
保存图像按钮坐标(49,148)
页码输入栏坐标(205,692)
修改格式按钮坐标(370，398)
jpg格式坐标(386,433)
键入文件名位置坐标(387,370)
'''
Key=keyboard.Key
Button=mouse.Button
Keyboard=keyboard.Controller()
Mouse=mouse.Controller()


total=183
number=1
time.sleep(5)
while  number<=total:
    #跳转到相应页面
    pyautogui.moveTo(205,692,duration=0.25)
    Mouse.click(Button.left)
    Keyboard.type(str(number)+'/'+str(total))
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    
    time.sleep(1)

    #点击保存图像
    pyautogui.moveTo(49,148,duration=0.25)
    Mouse.click(Button.left)
    time.sleep(0.5)

    
    #选择文件格式
    pyautogui.moveTo(370,398,duration=0.25)
    Mouse.click(Button.left)
 
    pyautogui.moveTo(386,433,duration=0.25)
    Mouse.click(Button.left)
    

    #键入文件名
    pyautogui.moveTo(387,370,duration=0.25)
    Mouse.click(Button.left)
    Keyboard.type(str(number-1))
    



    #确认文件保存方式
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    time.sleep(0.5)

    #确认文件已保存
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
   
    number=number+1

    












