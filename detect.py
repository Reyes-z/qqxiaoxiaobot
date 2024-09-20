import keyboard  
import time  
import pyautogui
import pyperclip
import random

should_detect = False

def toggle_mouse(e  ):  
    global should_detect  
    # 切换should_run变量的状态  
    should_detect = not should_detect  
    print("执行状态已切换:", "开始检测" if should_detect else "停止检测")


keyboard.on_press_key("space", toggle_mouse)

   
print("程序已启动，按空格键开始/停止执行代码。")
  
while True:  
    time.sleep(1)
    if should_detect:
           
        mouse_x, mouse_y = pyautogui.position()
        print("鼠标位置的坐标值:", mouse_x, mouse_y)
        
        time.sleep(1)
