import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea


class App:
    NAME = 'Control dock'
    VERSION = '0.1.0'
    ICON = "./resources/icon/favicon-16x16.png"

    def __init__(self):
        self.__app = QApplication(sys.argv)
        self.__main_window = QMainWindow()
        self.__mdi = QMdiArea()

    def run(self):
        path = os.path.dirname(os.path.abspath(__file__))
        icon = QIcon(path+"/resources/icon/favicon-16x16.png")
        self.__main_window.setWindowIcon(icon)
        self.__main_window.setWindowTitle(self.NAME + " v."+self.VERSION)
        self.__main_window.setCentralWidget(self.__mdi)
        self.__main_window.show()
        self.__app.exec()
