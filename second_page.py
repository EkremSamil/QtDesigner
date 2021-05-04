from PyQt5.QtWidgets import*
from Anamenü import Ui_MainWindow

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)