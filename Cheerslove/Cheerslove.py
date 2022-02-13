import time
import win32api
import win32con
import win32gui
from PIL import ImageGrab
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow
from threading import Thread

# new pyinstaller method:
#
# pyuic5 -o gui.py gui.ui
# pyinstaller --hidden-import=PyQt5 -w -F -i Cheerslovei.ico Cheerslove.py
#
# -w 打包的exe文件中隐藏控制台文件
# -F 在dist文件夹中只保存打包的exe文件
# -i 打包的exe文件采用选定的ico图标

# initialize
access = False
flag = True
window = 0


# button click
def button():
    global window
    window = win32gui.FindWindow(0, "《风暴英雄》")
    if window != 0:
        ui.label_2.setText("按下面按钮开始!")
        ui.pushButton.setText("已找到窗口")
        ui.radioButton.setEnabled(True)
        ui.pushButton.setEnabled(False)
    if window == 0:
        ui.label_2.setText("未找到, 请重试!")


def radio():
    global access, flag
    access = bool(1 - access)
    if access and flag:
        flag = False
        thread.start()


# main process control
def mainprocess():
    while True:
        if access and (window != 0):
            img = ImageGrab.grab()
            load_img = img.load()
            if img.size == (2560, 1440):
                if load_img[1511, 1361] == (63, 254, 122):
                    time.sleep(0.75 / 1.8)
                    win32api.SendMessage(window, win32con.WM_KEYDOWN, 0x2E, 0)
                    win32api.SendMessage(window, win32con.WM_KEYUP, 0x2E, 0)
            elif img.size == (1920, 1080):
                if load_img[1132, 1050] == (8, 253, 63):
                    time.sleep(0.75 / 1.8)
                    win32api.SendMessage(window, win32con.WM_KEYDOWN, 0x2E, 0)
                    win32api.SendMessage(window, win32con.WM_KEYUP, 0x2E, 0)


# gui & main process control
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
app = QApplication([])
mainw = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(mainw)
mainw.show()
ui.pushButton.clicked.connect(button)
ui.radioButton.clicked.connect(radio)
ui.radioButton.setEnabled(False)
thread = Thread(target=mainprocess)
app.exec_()

# os.system("mode con cols=50 lines=4")
# os.system("title 常驻荷枪实弹")
# if window == 0:
#     access = False
#     print(" \n"
#           "未找到游戏窗口, 请先打开游戏窗口再启动,\n"
#           "程序将在3秒内自动关闭...")
#     time.sleep(3)
#     exit(0)
# else:
#     access = True
#     print(" \n"
#           "已加载按键绑定, 进入游戏后可以进行测试,\n"
#           "关闭该窗口即可结束按键绑定!")
# pyinstaller -F -i C:\Users\Administrator\Desktop\TEST.ico C:\Users\Administrator\Desktop\AutoClick.py
# use this command in cmd to create .exe file!
