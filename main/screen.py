# 屏幕读取开始
import math
import sys
import time

import win32api
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
    # 创建bitmap准备保存图片
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
    # x_total = math.ceil(x_end - x_start)
    # x_unit = math.ceil(x_total / 20)
    # x_center = math.ceil(x_total / 2)
    # y_total = math.ceil(y_end - y_start)
    # y_unit = math.ceil(y_total / 20)
    # y_center = math.ceil(y_total / 2)
    # box = (x_center + 3 * x_unit, y_center + 4 * y_unit, x_center + math.ceil(3.5 * x_unit),
    #        y_center + math.ceil(4.5 * y_unit))
    # box = (x_center - math.ceil(3.5 * x_unit), y_center + 4 * y_unit, x_center - 3 * x_unit,
    #        y_center + math.ceil(4.5 * y_unit))
    # crop = image_from_bytes.crop(box)
    # crop.show()

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
    while True:
        time.sleep(0.1)
        image_from_bytes = find_window_get_screen(hwnd, x_start, y_start, x_end, y_end)
        # 解析
        # 计算参数设置
        x_total = math.ceil(x_end - x_start)
        x_unit = math.ceil(x_total / 20)
        x_center = math.ceil(x_total / 2)
        y_total = math.ceil(y_end - y_start)
        y_unit = math.ceil(y_total / 20)
        y_center = math.ceil(y_total / 2)
        # 计数器
        counter = 0
        all_counter = 0

        # 打击点左侧
        for i in range(x_center - math.ceil(3.5 * x_unit), x_center - math.ceil(3.4 * x_unit)):
            for j in range(y_center + 4 * y_unit, y_center + math.ceil(4.5 * y_unit)):
                r, g, b = image_from_bytes.getpixel((i, j))
                all_counter = all_counter + 1
                if b >= 200:
                    counter = counter + 1
        print(all_counter)
        print(counter)
        if counter > all_counter * 0.8:
            print("左侧来敌人")
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            time.sleep(0.1)
        # 逻辑复位
        all_counter = 0
        counter = 0

        # 打击点右侧
        for i in range(x_center + math.ceil(3.4 * x_unit), x_center + math.ceil(3.5 * x_unit)):
            for j in range(y_center + 4 * y_unit, y_center + math.ceil(4.5 * y_unit)):
                r, g, b = image_from_bytes.getpixel((i, j))
                all_counter = all_counter + 1
                if r >= 200:
                    counter = counter + 1
        print(all_counter)
        print(counter)
        if counter > all_counter * 0.8:
            print("右侧来敌人")
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
            time.sleep(0.1)
        # 逻辑复位
        all_counter = 0
        counter = 0
