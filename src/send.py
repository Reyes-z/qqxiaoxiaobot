import keyboard  
import time  
import pyautogui
import pyperclip
import random


# mode = 2
# pos = [(200,750),(1000,750),(1600,750)]

def send_msg(meassage):  
    # 输入消息 共耗时3.7s 
    
    pyperclip.copy("@xiaoxiao")
    time.sleep(0.3)
    pyautogui.hotkey('Ctrl', 'V')
    time.sleep(1.5)
    pyautogui.press('enter')
    time.sleep(0.3)
    pyperclip.copy(meassage)
    pyautogui.hotkey('Ctrl', 'V')
    time.sleep(1)
    pyautogui.press(' ')
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(0.3)
    

def wait_time(pos,mode):
    
    wt=int(60-((3.7)*len(pos)*mode+1))
    st=random.randint(wt,wt+2)
    # print("等待时间:",wt)
    return st
    