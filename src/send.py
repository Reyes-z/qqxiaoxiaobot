import keyboard  
import time  
import pyautogui
import pyperclip
import random


def send_message(meassage):  
    # 输入消息 共耗时3.7s 
    time_start = time.time()
    
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
    
    time_end = time.time()
    time_cost = time_end - time_start