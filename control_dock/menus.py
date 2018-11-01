from PyQt5.QtWidgets import QMenu

from control_dock.menu_actions import ExitAction


class FileMenu(QMenu):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.__exit_action = ExitAction()

    def build(self):
        self.setTitle('&File')
        self.addSeparator()
        self.addAction(self.__exit_action)
