from PyQt5.QtWidgets import *
from KullaniciGiris import Ui_Form
from second_page import MainWindow


class Form(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.signPB.clicked.connect(self.open_secondpage())
        self.second_page = MainWindow()

    def open_secondpage(self):
        self.MainWindow.open()







