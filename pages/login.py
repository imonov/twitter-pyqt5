from PyQt5.QtWidgets import *
from db.connect_db import MySQL
from pages.register import RegisterPage
from pages.homepage import HomePage


class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.mysql = MySQL()

        self.user = None

        self.setGeometry(100, 100, 300, 400)

        self.setStyleSheet("* {font-size: 22px;}")

        self.main_v_lay = QVBoxLayout()
        self.btn_h_lay = QHBoxLayout()

        self.login_edit = QLineEdit()
        self.login_edit.setPlaceholderText("Login")

        self.password_edit = QLineEdit()
        self.password_edit.setPlaceholderText("Parol")

        self.btn_register = QPushButton("Ro'yxatdan o'tish")
        self.btn_register.clicked.connect(self.register)
        self.btn_login = QPushButton("Kirish")
        self.btn_login.clicked.connect(self.login)

        self.btn_h_lay.addWidget(self.btn_register)
        self.btn_h_lay.addWidget(self.btn_login)

        self.main_v_lay.addWidget(self.login_edit)
        self.main_v_lay.addWidget(self.password_edit)
        self.main_v_lay.addLayout(self.btn_h_lay)
        self.setLayout(self.main_v_lay)

    def register(self):
        self.hide()
        self.register_page = RegisterPage(self)
        self.register_page.show()

    def login(self):
        if not self.login_edit.text() or not self.password_edit.text():
            self.msg = QMessageBox()
            self.msg.setText("Maydonlarni to'ldiring")
            self.msg.show()
            return

        if self.mysql.loginUser(self.login_edit.text()):
            if self.mysql.loginUser(self.login_edit.text())[2] == self.password_edit.text():
                self.user = self.mysql.loginUser(self.login_edit.text())
                self.home_window = HomePage(self.user, self)
                self.hide()
                self.home_window.show()
            else:
                self.msg = QMessageBox()
                self.msg.setText("Parol xato")
                self.msg.show()
            return
