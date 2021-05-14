# 屏幕读取开始
import win32api
import win32con
import win32gui

global wait

wait = 0.1


def start():
    # 获取分辨率
    total_screen_x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    total_screen_y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    print(total_screen_x)
    print(total_screen_y)

    # 以1/20的屏幕大小为单位寻找解析位置
    union_x = total_screen_x / 20
    union_y = total_screen_y / 20
    # 获取图像
    hwnd = win32gui.FindWindow(None, 'C:\Windows\system32\cmd.exe')
    # 模式解析


hwnd_title = dict()


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


win32gui.EnumWindows(get_all_hwnd, 0)

for h, t in hwnd_title.items():
    if t is not "":
        print(h, t)
#   while True:
#      time.sleep(wait)
