# 屏幕读取开始
import sys

import win32con
import win32gui
import win32ui
from PIL import Image

wait = 0.1


def find_window_get_screen(hwnd, x_start, y_start, x_end, y_end):
    hwnd_dc = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
    # mfcDC创建可兼容的DC
    save_dc = mfc_dc.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    bit_map = win32ui.CreateBitmap()
    # 为bitmap开辟空间
    bit_map.CreateCompatibleBitmap(mfc_dc, x_end - x_start, y_end - y_start)
    # 高度saveDC，将截图保存到saveBitmap中
    save_dc.SelectObject(bit_map)
    # 获取窗口位置
    # 截取从左上角（0，0）长宽为（w，h）的图片
    save_dc.BitBlt((0, 0), (x_end, y_end), mfc_dc, (0, 0), win32con.SRCCOPY)
    # 获取 图片 bites 内容
    bites = bit_map.GetBitmapBits(True)
    #
    image_from_bytes = Image.frombytes("RGB", (x_end - x_start, y_end - y_start), bites, "raw", "BGRX")
    return image_from_bytes


def start():
    # 获取窗口图像
    hwnd = win32gui.FindWindow(None, 'One Finger Death Punch 2')
    if hwnd == 0:
        print("游戏未启动 脚本暂停")
        sys.exit(0)
    # 窗口位置
    total_placement = win32gui.GetWindowPlacement(hwnd)
    print(total_placement)
    placement = total_placement[4]
    x_start = placement[0]
    y_start = placement[1]
    x_end = placement[2]
    y_end = placement[3]
    image_from_bytes = find_window_get_screen(hwnd, x_start, y_start, x_end, y_end)
    # 解析图像
    for i in range(256):
        for j in range(256):
            r, g, b = image_from_bytes.getpixel((i, j))
            print(r, g, b)
    # print(bit_map_info)
    # pyautogui.rightClick()
