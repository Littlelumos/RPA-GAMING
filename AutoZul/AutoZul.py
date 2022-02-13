import _thread
import os
import time

import win32api
import win32con
import win32gui

num = 0
runtime = False
wow = win32gui.FindWindow(0, "魔兽世界")
os.system("mode con cols=36 lines=6")
os.system("title 自动祖尔聚怪")


def hide_wow():
    win32gui.ShowWindow(wow, 0)


def unhide_wow():
    win32gui.ShowWindow(wow, 1)


def reg_insert():
    win32gui.RegisterHotKey(0, 99, 0, win32con.VK_INSERT)
    win32gui.RegisterHotKey(0, 98, 0, win32con.VK_DELETE)


def event_handle():
    global num
    global runtime
    msg = win32gui.GetMessage(0, 0, 0)
    if msg[1][2] == 99:
        if wow == win32gui.GetForegroundWindow():
            i = os.system("cls")
            print(" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
                  "  检测到在窗口内按下insert键\n"
                  "  开始执行泛化操作!\n"
                  " >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            runtime = True
    elif msg[1][2] == 98:
        i = os.system("cls")
        print(" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
              "  程序已中止!\n"
              "  重新按下insert键开始操作\n"
              " >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        num = 0
        runtime = False
    time.sleep(0.01)


def get_wow():
    global wow
    if wow != 0:
        i = os.system("cls")
        print(" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
              "  已查找到窗口\n"
              "  按下insert开始使用...\n"
              " >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    else:
        i = os.system("cls")
        print(" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
              "  未查找到窗口\n"
              "  程序将在3秒后关闭...\n"
              " >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        time.sleep(3)
        exit(0)


def bind_click(x, y):
    position = win32api.MAKELONG(x, y)
    win32api.SendMessage(wow, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, position)
    win32api.SendMessage(wow, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, position)
    time.sleep(0.01)


def run_process():
    global runtime
    while True:
        if runtime:
            main_process()
            time.sleep(24)
        time.sleep(0.1)


def main_process():
    global runtime
    global num
    flag = 4
    while flag >= 0:
        win32api.SendMessage(wow, win32con.WM_KEYDOWN, 0x20, 0)
        win32api.SendMessage(wow, win32con.WM_KEYUP, 0x20, 0)
        win32api.SendMessage(wow, win32con.WM_KEYDOWN, 0x58, 0)
        win32api.SendMessage(wow, win32con.WM_KEYUP, 0x58, 0)
        time.sleep(0.1)
        flag = flag - 1
    num = num + 1
    i = os.system("cls")
    print(" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
          "  AutoZul 正在运行中...\n")
    print("  程序已运行 ", num, " 次\n"
          " >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


if True:
    get_wow()
    reg_insert()
    _thread.start_new_thread(run_process, ())
    while True:
        event_handle()
    # TEST X,Y CLICK
    # while True:
    #    bind_click(1280, 420)
