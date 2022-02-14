import configparser

import win32gui
from PIL import Image, ImageGrab
from PyQt5 import QtCore
from paladin import paladinUI
# from priest import priestUI
# from shaman import shamanUI
from PyQt5.QtWidgets import QApplication, QMainWindow


def activateWindow():
    global window
    window = win32gui.FindWindow(0, "魔兽世界")
    if window != 0:
        # enable the buttons
        ui.pushButton_5.setEnabled(True)
        ui.pushButton_6.setEnabled(True)
        ui.groupBox_3.setEnabled(True)
        ui.groupBox.setEnabled(True)
        ui.label_16.setText(str(window))

        # figure out how many players in group
        img = ImageGrab.grab()
        loadImg = img.load()
        sizeX, sizeY = img.size[0], img.size[1]
    else:
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
    access = False
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
