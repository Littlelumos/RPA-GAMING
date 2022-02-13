import pyautogui
import win32api
import win32con
import win32gui
from PIL import Image, ImageGrab

# with open('Aptechka.lua', '+r', encoding='UTF-8') as f:
#     t = f.read()
#     t = t.replace('你很缺智力啊 - 厄运之槌', '你很缺智力啊 - 白银之手')
#     f.seek(0, 0)
#     f.write(t)
#     f.truncate()
# exit()
dungeon = 5
klz = 10
raid = 25
minLeft = 10000
minDown = 10000
long = 0
height = 0
screen = pyautogui.screenshot("screen.png")
img = Image.open("screen.png")
x = img.size[0]
y = img.size[1]

# initialize the variables
for a in range(0, x - 275, 80):
    for b in range(0, y - 275, 40):
        if img.getpixel((a, b)) == (0, 0, 0):
            left = a
            right = a
            up = b
            down = b
            while img.getpixel((left, up)) == (0, 0, 0):
                up += 1
            up -= 1
            while img.getpixel((left, up)) == (0, 0, 0):
                left -= 1
            left += 1
            while img.getpixel((right, down)) == (0, 0, 0):
                down -= 1
            down += 1
            while img.getpixel((right, down)) == (0, 0, 0):
                right += 1
            right -= 1
            if (right - left + 1) * (up - down + 1) < 8000:
                if (right - left + 1) * (up - down + 1) > 2500:
                    long = right - left + 1
                    height = up - down + 1
                    if minLeft > left:
                        minLeft = left
                    if minDown > down:
                        minDown = down
print("宽度和高度为: ", long, height)
print("左下角锚点为: ", minLeft, minDown)

# main process
if True:
    while True:
        img = ImageGrab.grab()
        yPos = 1
        for xPos in range(1, 5):
            load_img = img.load()
            if load_img[minLeft + xPos * long - 3, minDown + height - height * (yPos - 1) - 5] == (242, 251, 248):
                mosX, mosY = win32gui.GetCursorPos()
                win32api.SetCursorPos([minLeft + xPos * long - 3, minDown - height * (yPos - 1) + 35])
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                win32api.SetCursorPos([mosX, mosY])
                break
