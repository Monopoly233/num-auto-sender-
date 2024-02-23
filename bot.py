import pyautogui
import keyboard
from pynput.mouse import Listener
import time

def on_click(x, y, button, pressed):
    if pressed:
        return False  # 返回False以停止监听

def main():
    # 从用户那里获取一个起始数字
    start_number = int(input("please input a num: "))

    print("move your mouse and run。")
    
    # 监听一次鼠标点击
    with Listener(on_click=on_click) as listener:
        listener.join()

    number = start_number
    try:
        while True:
            pyautogui.write(str(number))  # 键入数字
            pyautogui.press('enter')      # 按下回车
            number += 1                   # 数字加一
            time.sleep(0.8)               # 稍微等待一下，以便观察效果

            # 如果用户按下了'esc'键，则退出循环
            if keyboard.is_pressed('esc'):
                break
    except KeyboardInterrupt:
        print("script is stopped by user.")

if __name__ == "__main__":
    main()
