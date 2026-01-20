from PyQt5.QtWidgets import *

from db.connect_db import MySQL


class CreateTwit(QWidget):
    def __init__(self, user_id, obj):
        super().__init__()
        self.main_v_lay = QVBoxLayout()

        self.mysql = MySQL()

        self.setGeometry(100, 100, 400, 500)
        self.setStyleSheet("* {font-size: 22px;}")

        self.home_page = obj
        self.id = user_id

        self.title_page = QLabel("Yangi post yozing")
        self.main_v_lay.addWidget(self.title_page)
        self.main_v_lay.addStretch()

        self.post_v_lay = QVBoxLayout()

        self.title = QLineEdit()
        self.title.setPlaceholderText("Sarlavhasi")
        self.text = QTextEdit()
        self.text.setPlaceholderText("Bu yerga postingizni yozing")

        self.post_v_lay.addWidget(self.title)
        self.post_v_lay.addWidget(self.text)

        self.main_v_lay.addLayout(self.post_v_lay)

        self.main_v_lay.addStretch()

        self.btn_h_lay = QHBoxLayout()
        self.btn_back = QPushButton("Orqaga qaytish")
        self.btn_post = QPushButton("Yangi post")
        self.btn_post.clicked.connect(self.createPost)

        self.btn_h_lay.addWidget(self.btn_post)
        self.btn_h_lay.addWidget(self.btn_back)

        self.main_v_lay.addLayout(self.btn_h_lay)

        self.setLayout(self.main_v_lay)

    def createPost(self):
        if not self.title.text() or not self.text.toPlainText():
            self.msg = QMessageBox()
            self.msg.setText("Kerakli maydonlarni to'ldiring...")
            self.msg.setIcon(QMessageBox.Warning)
        else:
            self.mysql.createPost(
                self.id, self.title.text(), self.text.toPlainText())
            self.hide()
            self.home_page.show()
