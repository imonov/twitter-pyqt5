from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from db.connect_db import MySQL
from pages.new_twit import CreateTwit
from pages.profile_page import ProfilePage


class HomePage(QWidget):
    def __init__(self, user, obj):
        super().__init__()

        self.mysql = MySQL()

        self.user = user

        self.posts = None

        self.setGeometry(100, 100, 400, 500)
        self.setStyleSheet("* {font-size: 22px;}")
        self.main_v_lay = QVBoxLayout()
        self.title_h_lay = QHBoxLayout()

        self.btn_profile = QPushButton(f"/@{self.user[1]}")
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
        for x in self.getAllPosts():
            self.post_v_lay.addWidget(QPushButton(f"{x[0]}\n{x[1]}"))
        print(self.posts)

        self.main_v_lay.addLayout(self.post_v_lay)

        # Post qismi tugadi

        self.setLayout(self.main_v_lay)

    def profile(self):
        self.profile_window = ProfilePage(self, self.user)
        self.hide()
        self.profile_window.show()

    def writePost(self):
        self.close()
        self.new_twit = CreateTwit(self.user[0], self)
        self.new_twit.show()

    def getAllPosts(self):
        return self.mysql.getPosts()

    def showEvent(self, event):
        self.getAllPosts()
