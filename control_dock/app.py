import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from control_dock.components import MainWindow, Workspace, Toolbar, MenuBar
from control_dock.config import Config


class App:
    """
    Application.
    """
    def __init__(self):
        self.__config = Config()
        self.__app = QApplication(sys.argv)
        self.__main_window = MainWindow()
        self.__workspace = Workspace()
        self.__toolbar = Toolbar()
        self.__menu_bar = MenuBar()

    def run(self):
        path = os.path.dirname(os.path.abspath(__file__))

        self.__app.setWindowIcon(QIcon(path + self.__config.get('app.icon')))
        self.__app.setApplicationName(self.__config.get('app.name'))
        self.__app.setApplicationVersion(self.__config.get('app.version'))

        self.__main_window.setCentralWidget(self.__workspace)
        self.__main_window.addToolBar(self.__toolbar)
        self.__main_window.setMenuBar(self.__menu_bar)
        self.__main_window.build()
        self.__main_window.show()

        self.__toolbar.build()

        self.__menu_bar.build()

        self.__app.exec()

