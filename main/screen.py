# 屏幕读取开始
import pyautogui
import win32api
import win32con
import win32gui

wait = 0.1


def start():
    # 获取分辨率
    total_screen_x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    total_screen_y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    # 以1/20的屏幕大小为单位寻找解析位置
    union_x = total_screen_x / 20
    union_y = total_screen_y / 20
    # 获取窗口图像
    hwnd = win32gui.FindWindow(None, 'One Finger Death Punch 2')

    # 模式解析
    print(hwnd)
    pyautogui.rightClick()