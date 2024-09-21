import keyboard  
import time  
import pyautogui
import pyperclip
import random
# 定义一个变量来追踪是否应该执行代码  
should_run = False 
a = 2
 

def toggle_execution(e  ):  
    global should_run  
    # 切换should_run变量的状态  
    should_run = not should_run  
    print("执行状态已切换:", "开始执行" if should_run else "停止执行")  

def send_message(meassage):  
    # 输入消息  
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
     
    
# 监听空格键  
keyboard.on_press_key("space", toggle_execution)

  
print("程序已启动，按空格键开始/停止执行代码。")  
  
# 保持程序运行  
while True:  
    time.sleep(1)
    if should_run:
        if a == 1:
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
            
        elif a == 2:
            
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
            
        elif a == 3:
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
         
        # time.sleep(random.randint(58, 61)) 