import keyboard  
import time  
import pyautogui
import pyperclip
import random
import json

pos=[]
alt = True

def detect(e): 
    global pos
    pos.append((mouse_x, mouse_y))
    print("成功添加鼠标坐标值:", mouse_x, mouse_y)

def end(e):
    global alt
    alt = False
    time.sleep(1)
    print("程序已结束")
    print("共收集到", len(pos),"个坐标值")
    for i in range(len(pos)):
        print("第", i+1, "个坐标值:", pos[i] ,end='\n')
    with open('pos.json', 'w') as file:
        json.dump(pos, file)
    print("成功将坐标存储到pos.json文件中")
    
keyboard.on_press_key("d", detect)
keyboard.on_press_key("e", end)

print("程序已启动，按d进行检测，按e停止。")

while True:
    if alt:
        time.sleep(1)
        mouse_x, mouse_y = pyautogui.position()
        print("鼠标坐标:", mouse_x, mouse_y)    
        
     



  
