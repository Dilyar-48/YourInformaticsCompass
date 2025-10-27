import sys
import csv

from PyQt6.QtWidgets import QApplication, QMainWindow, QButtonGroup, QLineEdit, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QFont, QColor


class Pseudonym(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(350, 370)
        self.setWindowTitle("Your Informatics Compass Register")
        self.toname = QLineEdit(self)
        self.toname.resize(250, 30)
        self.toname.move(50, 40)
        self.toname.setPlaceholderText("Псевдоним")
        self.togender = QLineEdit(self)
        self.togender.resize(250, 30)
        self.togender.move(50, 85)
        self.togender.setPlaceholderText("Пол")
        self.topassword = QLineEdit(self)
        self.topassword.resize(250, 30)
        self.topassword.move(50, 130)
        self.topassword.setPlaceholderText("Пароль")
        self.todoublepassword = QLineEdit(self)
        self.todoublepassword.resize(250, 30)
        self.todoublepassword.move(50, 175)
        self.todoublepassword.setPlaceholderText("Повторите пароль")
        self.entrance = QPushButton(self)
        self.entrance.resize(100, 30)
        self.entrance.move(125, 230)
        self.entrance.setText("Войти")
        self.entrance.clicked.connect(self.checktoentrance)
        self.nameerror = QLabel(self)
        self.nameerror.resize(250, 10)
        self.nameerror.move(50, 72)
        self.todoublepassworderror = QLabel(self)
        self.todoublepassworderror.resize(250, 10)
        self.todoublepassworderror.move(50, 207)


    def checktoentrance(self):
        with open("all_peoples.csv", newline='', encoding="utf-8") as file:
            reader = csv.reader(file)
            all_accounts = ["".join(row).split(";") for row in reader]
            self.nameerror.setText("")
            self.todoublepassworderror.setText("")
            if self.toname.text() in [line[0] for line in all_accounts]:
                self.nameerror.setFont(QFont("comic_sans", 7))
                self.nameerror.setStyleSheet("color: red;")
                self.nameerror.setText("Имя уже занято")
            elif self.topassword.text() != self.todoublepassword.text():
                self.todoublepassworderror.setFont(QFont("comic_sans", 7))
                self.todoublepassworderror.setStyleSheet("color: red;")
                self.todoublepassworderror.setText("Неверный пароль")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Pseudonym()
    ex.show()
    sys.exit(app.exec())
