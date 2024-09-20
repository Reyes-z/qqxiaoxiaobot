import keyboard  
import time  
import pyautogui
import pyperclip
import random
# 定义一个变量来追踪是否应该执行代码  
should_run = False  


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
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(0.3)
    pyperclip.copy(meassage)
    pyautogui.hotkey('Ctrl', 'V')
    time.sleep(1)
    pyautogui.press(' ')
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(0.3)
    
    
    
# def send_tupo():  
#     # 输入消息  
#     pyperclip.copy("@xiaoxiao")
#     pyautogui.hotkey('Ctrl', 'V')
#     time.sleep(0.6) 
#     pyautogui.press('enter')
#     time.sleep(0.5)
#     pyperclip.copy("修炼")
#     pyautogui.hotkey('Ctrl', 'V')
#     time.sleep(0.5)
#     pyautogui.press(' ')
#     time.sleep(0.5)
#     pyautogui.press('enter')
#     time.sleep(0.6) 
# 监听空格键  
keyboard.on_press_key("space", toggle_execution)

# 移动到指定输入框坐标位置,并点击
# def move_to_input_click():
#     pyautogui.click(10,10)
  
print("程序已启动，按空格键开始/停止执行代码。")  
  
# 保持程序运行  
while True:  
    time.sleep(1)
    if should_run:  
        
        pyautogui.click(200,750)  
        send_message("修炼")
         
        # send_xiulian()
        # send_tupo()
        
        # time.sleep(1)
        # pyautogui.click(1000,750)
        # send_xiulian()
        # send_tupo()
        
        # time.sleep(1)
        # pyautogui.click(1600,750)
        # send_xiulian()
        # send_tupo()
        
        # time.sleep(1)
        
        # time.sleep(random.randint(43, 46)) 