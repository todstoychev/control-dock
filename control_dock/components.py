import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMdiArea, QToolBar, QMenuBar

from control_dock.config import Config
from control_dock.menus import FileMenu


class MainWindow(QMainWindow):
    """
    Main application window.
    """

    def __init__(self, flags=None, *args, **kwargs):
        """
        :param flags:
        :param args:
        :param kwargs:
        """
        super().__init__(flags, *args, **kwargs)
        self.__config = Config()

    def build(self):
        path = os.path.dirname(os.path.abspath(__file__))
        self.setWindowTitle(self.__config.get('app.name') + ' v.' + self.__config.get('app.version'))
        self.setWindowIcon(QIcon(path + self.__config.get('app.icon')))


class Workspace(QMdiArea):
    def __init__(self):
        super().__init__()


class Toolbar(QToolBar):
    def build(self):
        self.setMovable(False)


class MenuBar(QMenuBar):
    def __init__(self):
        super().__init__()
        self.__file_menu = FileMenu()

    def build(self):
        self.addMenu(self.__file_menu)
        self.__file_menu.build()
