from PyQt5.QtWidgets import *
from db.connect_db import MySQL


class RegisterPage(QWidget):
    def __init__(self, obj):
        super().__init__()
        self.mysql = MySQL()
        self.setGeometry(100, 100, 300, 400)
        self.setStyleSheet("* {font-size: 22px}")

        self.login_window = obj

        self.main_v_lay = QVBoxLayout()
        self.input_v_lay = QVBoxLayout()
        self.btn_h_lay = QHBoxLayout()

        self.label = QLabel("Ro'yxatdan o'tish")

        self.full_name_edit = QLineEdit()
        self.full_name_edit.setPlaceholderText("To'liq ismingiz")
        self.username_edit = QLineEdit()
        self.username_edit.setPlaceholderText("Foydalanuvchi nomingiz")
        self.password_edit = QLineEdit()
        self.password_edit.setPlaceholderText("Parol")
        self.password_repeat_edit = QLineEdit()
        self.password_repeat_edit.setPlaceholderText("Parolni qayta yozing")

        self.input_v_lay.addWidget(self.label)
        self.input_v_lay.addWidget(self.full_name_edit)
        self.input_v_lay.addWidget(self.username_edit)
        self.input_v_lay.addWidget(self.password_edit)
        self.input_v_lay.addWidget(self.password_repeat_edit)

        self.main_v_lay.addLayout(self.input_v_lay)
        self.main_v_lay.addStretch()

        self.btn_back = QPushButton("Kirish")
        self.btn_back.clicked.connect(self.backToLogin)
        self.btn_reg = QPushButton("Ro'yxatdan o'tish")
        self.btn_reg.clicked.connect(self.register)

        self.btn_h_lay.addWidget(self.btn_back)
        self.btn_h_lay.addWidget(self.btn_reg)

        self.main_v_lay.addLayout(self.btn_h_lay)

        self.setLayout(self.main_v_lay)

    def register(self):
        check = True
        if self.password_edit.text() != self.password_repeat_edit.text():
            message = "Parollar mos emas"
            icon = QMessageBox.Warning
            check = False

        if not self.full_name_edit.text() or not self.username_edit.text() or not self.password_edit.text() or not self.password_repeat_edit.text():
            message = "Maydonlar to'liq to'ldirilmagan"
            icon = QMessageBox.Warning
            check = False

        if check == True:
            try:
                self.mysql.createUser(self.username_edit.text(
                ), self.password_edit.text(), self.full_name_edit.text())
                print("User yaratildi")
                self.hide()
                self.login_window.show()
                return
            except:
                message = "Bu foydalanuvchi nomi band"
                icon = QMessageBox.Critical

        self.msg = QMessageBox()
        self.msg.setText(message)
        self.msg.setIcon(icon)
        self.msg.show()

    def backToLogin(self):
        pass
