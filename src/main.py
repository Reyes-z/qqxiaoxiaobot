import keyboard  
import time  
import pyautogui
import pyperclip
import random
from send import send_msg , wait_time

mode = -1
pos = [(200,750),(1000,750),(1600,750)]

def start():
    print("开始执行")
    global mode
    mode = int(input("1.自动修炼模式\n2.自动修炼自动突破模式\n3.修仙签到与宗门丹药领取\n 请输入一个数字 (1, 2, 3): "))
    print("你输入的数字是:", mode)
    print("运行过程中按空格，程序停止下进行一轮操作。")

def program_attitude(e):
    global mode   
    mode = -1
    start()
    
start()  
keyboard.on_press_key("space", program_attitude)

while True:
    time.sleep(1)
    if mode == 1:
        for i in range(len(pos)):
            pyautogui.click(pos[i])
            send_msg("修炼")
            time.sleep(1)
        # time.sleep(random.randint(47, 48))
        time.sleep(wait_time(pos,mode)) # type: ignore
        
    elif mode == 2:
        for i in range(len(pos)):
            pyautogui.click(pos[i])
            send_msg("修炼")
            send_msg("破")
            time.sleep(1)
        time.sleep(wait_time(pos,mode)) # type: ignore
        
    elif mode == 3:
        for i in range(len(pos)):
            pyautogui.click(pos[i])
            send_msg("修仙签到")
            send_msg("宗门丹药领取")
            time.sleep(1)
        print("签到与领取完成")
        program_attitude(1)