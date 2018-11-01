import sys

from PyQt5.QtWidgets import QApplication


class App:
    NAME = 'Control dock'
    VERSION = '0.1.0'
    ICON = 'resources/icon.png'

    def __init__(self):
        self.__app = QApplication(sys.argv)

    def run(self):
        self.__app.exec()
