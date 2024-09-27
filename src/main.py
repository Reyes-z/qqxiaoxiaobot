import keyboard  
import time  
import pyautogui
import pyperclip
import random
import json
from send import send_msg , wait_time

pyautogui.FAILSAFE=False
mode = -1
pos = [(200,750),(1000,750),(1600,750)] # 这里就是所有QQ窗口对话框的坐标，按需更改。


with open('pos.json', 'r') as file:
    pos = json.load(file)
print("成功载入pos文件中坐标信息。\n坐标数据为",pos)

def start():
    print("开始执行")
    global mode
    print("1.自动修炼模式\n2.自动修炼自动突破模式\n3.修仙签到与宗门丹药领取\n4.自定义指令模式\n")
    mode = int(input(" 请输入一个数字(1, 2, 3, 4):"))
    print("你输入的数字是:", mode)
    print("若在运行过程中按空格，程序将下一轮操作前停止。")

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
        
    elif mode == 4:
        message = (input("请输入需要执行的自定义命令"))
        for i in range(len(pos)):
            pyautogui.click(pos[i])
            send_msg(message)
            time.sleep(1)
        print("自定义命令执行完成")
        program_attitude(1)