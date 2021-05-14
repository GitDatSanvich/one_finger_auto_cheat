import sys
import time
import tkinter.messagebox

from main import screen

print("启动aofdp自动化脚本！")

print("请全屏游戏以确保脚本正常运行")
# 弹框确认游戏全屏
if not tkinter.messagebox.askokcancel('提示', '请全屏游戏以确保脚本正常运行'):
    sys.exit(0)
# 确认
print("等待五秒")
time.sleep(5)
print("开始读屏")

# 获取屏幕分辨率 定位识别点
screen.start()
