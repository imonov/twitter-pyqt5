from PyQt5.QtWidgets import *
from PyQt5.QtSvg import *

from db.connect_db import MySQL


class ProfilePage(QWidget):
    def __init__(self, obj, user):
        super().__init__()

        self.mysql = MySQL()

        self.user = user
        self.home_window = obj

        self.setGeometry(100, 100, 300, 400)
        self.setStyleSheet("* {font-size: 22px;}")

        self.main_v_lay = QVBoxLayout()

        self.title_h_lay = QHBoxLayout()
        self.profile_image = QSvgWidget("images/user.svg")
        self.profile_image.setFixedSize(50, 50)
        self.title_h_lay.addWidget(self.profile_image)

        self.title_v_lay = QVBoxLayout()
        self.full_name = QLabel(self.user[3])
        self.user_name = QLabel(self.user[1])
        self.title_v_lay.addWidget(self.full_name)
        self.title_v_lay.addWidget(self.user_name)
        self.title_h_lay.addLayout(self.title_v_lay)
        self.title_h_lay.addStretch()

        self.main_v_lay.addLayout(self.title_h_lay)
        self.main_v_lay.addStretch()
        fetched_Posts = self.mysql.getPostById(self.user[0])

        # My posts qismi

        self.post_v_lay = QVBoxLayout()
        self.post_label = QLabel("Mening postlarim")
        self.post_v_lay.addWidget(self.post_label)
        self.posts_list = QVBoxLayout()

        for x in fetched_Posts:
            self.posts_list.addWidget(QPushButton(f"{x[1]}\n{x[2]}\n{x[4]}"))

        # my posts tugadi

        self.main_v_lay.addLayout(self.posts_list)

        self.setLayout(self.main_v_lay)
