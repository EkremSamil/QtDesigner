from PyQt5.QtWidgets import QApplication
from main_page import Form

app = QApplication([])
window = Form()
window.show()
app.exec_()