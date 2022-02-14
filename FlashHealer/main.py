import configparser

import win32gui
from PIL import Image, ImageGrab
from PyQt5 import QtCore
from paladin import paladinUI
# from priest import priestUI
# from shaman import shamanUI
from PyQt5.QtWidgets import QApplication, QMainWindow

if True:
    import numpy
    from matplotlib import pyplot

    testmode = False


def activateWindow():
    global window, alreadyGetWow, ColorValue
    window = win32gui.FindWindow(0, "魔兽世界")
    if window != 0:
        # enable the buttons
        if not alreadyGetWow:
            ui.pushButton_5.setEnabled(True)
            ui.pushButton_6.setEnabled(True)
            ui.groupBox_3.setEnabled(True)
            ui.groupBox.setEnabled(True)
            ui.label_16.setText(str(window))
            alreadyGetWow = True

        # figure out how many players in group
        img = ImageGrab.grab()
        loadImg = img.load()
        sizeX, sizeY = img.size[0], img.size[1]
        listBlack = []

        # pixel check
        def check(a, b):
            global ColorValue
            # Blacklist of the coordinate
            if a > sizeX * 0.8 and y < sizeY * 0.2:
                return False
            if y > sizeY * 0.8:
                return False
            ua, ub = a, b
            upixel = img.getpixel((ua, ub))
            while upixel[0] < ColorValue and upixel[1] < ColorValue and upixel[2] < ColorValue and ua < sizeX - 1:
                ua += 1
                upixel = img.getpixel((ua, ub))
                if not (upixel[0] < ColorValue and upixel[1] < ColorValue and upixel[
                    2] < ColorValue and ua < sizeX - 1):
                    ua -= 1
                    upixel = img.getpixel((ua, ub))
                    break
            while upixel[0] < ColorValue and upixel[1] < ColorValue and upixel[2] < 27 and ub < sizeY - 1:
                ub += 1
                upixel = img.getpixel((ua, ub))
                if not (upixel[0] < 27 and upixel[1] < 27 and upixel[2] < 27 and ub < sizeY - 1):
                    ub -= 1
                    break
            mpixel = img.getpixel((a, b))
            while mpixel[0] < ColorValue and mpixel[1] < ColorValue and mpixel[2] < ColorValue and a > 1:
                a -= 1
                mpixel = img.getpixel((a, b))
                if not (mpixel[0] < ColorValue and mpixel[1] < ColorValue and mpixel[2] < ColorValue and a > 1):
                    a += 1
                    mpixel = img.getpixel((a, b))
                    break
            while mpixel[0] < ColorValue and mpixel[1] < ColorValue and mpixel[2] < ColorValue and b > 1:
                b -= 1
                mpixel = img.getpixel((a, b))
                if not (mpixel[0] < ColorValue and mpixel[1] < ColorValue and mpixel[2] < ColorValue and b > 1):
                    b += 1
                    break
            if ua - a > 60 and ub - b > 30:
                listBlack.append((ua, ub))
                if testmode:
                    pyplot.scatter(ua, ub, s=3)
                return True
            else:
                return False

        # loop the right x,y coordinate
        for x in range(1, sizeX, 60):
            for y in range(1, int(sizeY * 0.9), 30):
                pixel = img.getpixel((x, y))
                if pixel[0] < ColorValue and pixel[1] < ColorValue and pixel[2] < ColorValue:
                    check(x, y)
        if testmode:
            pyplot.imshow(img)
            pyplot.show()
            print(listBlack)
    else:
        if testmode:
            print("NOT FOUND!")


def startHeal():
    global access
    access = True
    ui.label_14.setText("Yes")


def stopHeal():
    global access
    access = False
    ui.label_14.setText("No")


if __name__ == '__main__':
    # initialize the variables
    window, playerHurt, playerNear = 0, 0, 0
    ColorValue = 1
    access, alreadyGetWow = False, False
    # create the main gui
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication([])
    mainw = QMainWindow()

    # read the class of the player
    cf = configparser.ConfigParser()
    cf.read("config.ini")
    playerClass = cf.get("main-config", "class")
    if playerClass == "paladin":
        ui = paladinUI()
        ui.setupUi(mainw)
        skill = cf.get("main-config", "skill")
        ui.pushButton.clicked.connect(activateWindow)
        ui.pushButton_5.clicked.connect(startHeal)
        ui.pushButton_6.clicked.connect(stopHeal)
    # if playerClass == "priest":
    #     ui = priestUI()
    #     ui.setupUi(mainw)
    # if playerClass == "shaman":
    #     ui = shamanUI()
    #     ui.setupUi(mainw)

    # show the main window
    mainw.show()
    app.exec_()
