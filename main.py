from PyQt5.QtWidgets import QApplication
from pages.login import LoginPage
# from pages.register import RegisterPage


app = QApplication([])
win = LoginPage()

win.show()
app.exec_()
