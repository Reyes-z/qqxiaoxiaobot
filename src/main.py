import keyboard  
import time  
import pyautogui
import pyperclip
import random
from send import send_message
# 定义一个变量来追踪是否应该执行代码  
should_run = False 
mode=-1
def program_attitude(e):
    global should_run   
    should_run = not should_run  
    print("执行状态已切换:")
    if should_run:
        print("开始执行")
        global mode 
        mode = int(input("1.自动修炼自动突破模式\n2.自动修炼模式\n3.修仙签到与宗门丹药领取\n 请输入一个数字 (1, 2, 3): "))
        print("你输入的数字是:", mode)  
    else:
        print("停止执行")


keyboard.on_press_key("space", program_attitude)


print("程序已启动，按空格键开始/停止执行代码。")  

# 保持程序运行  
while True:  
    time.sleep(1)
    if should_run and mode >= 0 :
        try: 
            if mode == 1:
                time.sleep(1)
                pyautogui.click(200,750)  
                send_message("修炼")
                send_message("破")
        
                time.sleep(1)
            
                pyautogui.click(1000,750)
                send_message("修炼")
                send_message("破")
            
                time.sleep(1)
                pyautogui.click(1600,750)
                send_message("修炼")
                send_message("破") 
            
                time.sleep(1)
                time.sleep(random.randint(35, 38))
                
            elif mode == 2:
                
                time.sleep(1)
                pyautogui.click(200,750)  
                send_message("修炼")
        
                time.sleep(1)
            
                pyautogui.click(1000,750)
                send_message("修炼")
            
                time.sleep(1)
                pyautogui.click(1600,750)
                send_message("修炼") 
            
                time.sleep(1)
                time.sleep(random.randint(48, 51))
                
            elif mode == 3:
                time.sleep(1)
                pyautogui.click(200,750)  
                send_message("修仙签到")
                send_message("宗门丹药领取")
        
                time.sleep(1)
            
                pyautogui.click(1000,750)
                send_message("修仙签到")
                send_message("宗门丹药领取")
            
                time.sleep(1)
                pyautogui.click(1600,750)
                send_message("修仙签到")
                send_message("宗门丹药领取")
            
                time.sleep(1)
                time.sleep(random.randint(35, 38))   
            else:
                print("输入了错误的值请输入正确的数字.")
        except ValueError:
            print("非法输入请输入一个数字.")