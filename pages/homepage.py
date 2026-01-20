from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from db.connect_db import MySQL
from pages.new_twit import CreateTwit


class HomePage(QWidget):
    def __init__(self, user, obj):
        super().__init__()

        self.mysql = MySQL()

        self.user = user

        self.setGeometry(100, 100, 400, 500)
        self.setStyleSheet("* {font-size: 22px;}")

        self.main_v_lay = QVBoxLayout()
        self.title_h_lay = QHBoxLayout()

        self.btn_profile = QPushButton(self.user[2])
        self.btn_profile.setIcon(QIcon('images/user.svg'))
        self.btn_profile.clicked.connect(self.profile)

        self.btn_write_post = QPushButton()
        self.btn_write_post.setIcon(QIcon('images/write.svg'))
        self.btn_write_post.clicked.connect(self.writePost)

        self.title_h_lay.addWidget(self.btn_profile)
        self.title_h_lay.addStretch()
        self.title_h_lay.addWidget(self.btn_write_post)

        self.main_v_lay.addLayout(self.title_h_lay)

        # Post qismi
        self.post_v_lay = QVBoxLayout()
        self.getAllPosts()

        self.main_v_lay.addLayout(self.post_v_lay)

        # Post qismi tugadi

        self.setLayout(self.main_v_lay)

    def profile(self):
        pass

    def writePost(self):
        self.hide()
        self.new_twit = CreateTwit(self.user[0], self)
        self.new_twit.show()

    def getAllPosts(self):
        for p in self.mysql.getPosts():
            print(p)
            post = QPushButton(f"{p[0]}\n{p[1]}\n{p[3]} - {p[2]}")
            self.post_v_lay.addWidget(post)
