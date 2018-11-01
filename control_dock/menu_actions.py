from PyQt5.QtWidgets import QAction


class ExitAction(QAction):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setText("&Exit")
        self.setToolTip("Close program.")
