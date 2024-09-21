import keyboard  
import time  
import pyautogui
import pyperclip
import random


def send_message(meassage):  
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