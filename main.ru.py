import sys
import csv

from PyQt6.QtWidgets import QApplication, QMainWindow, QButtonGroup, QLineEdit, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QFont, QColor
from texts_for_theory import first_teory

class MaterialSelection(QMainWindow):
    pass
class TasksInApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(828, 492)
        self.setWindowTitle("Your Informatics Compass")
        self.setStyleSheet("""
                QMainWindow {
                    background-color: #a1d0d4;
                }
        """)
        self.regfont = QFont('Arial', 16)
        self.appname = QLabel(self)
        self.appname.resize(771, 391)
        self.appname.move(30, 61)
        self.appname.setFont(self.regfont)
        self.appname.setText(first_teory)


class StartApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(828, 492)
        self.setWindowTitle("Your Informatics Compass")
        self.setStyleSheet("""
                QMainWindow {
                    background-color: #75dfff;
                }
        """)
        self.appname = QLabel(self)
        self.appname.resize(800, 71)
        self.appname.move(20, 20)
        self.regfont = QFont('Arial', 20)
        self.appname.setText("""<html><head/><body><p align="center"><span style=" font-size:20pt; font-weight:600;">Your Informatic Compass</span></p></body></html>""")
        self.theorybtn = QPushButton(self)
        self.theorybtn.setFont(self.regfont)
        self.theorybtn.setStyleSheet("background-color: #91f8ff; border-width: 1000%")
        self.theorybtn.setText("Теория")
        self.theorybtn.resize(811, 121)
        self.theorybtn.move(10, 110)
        self.tasksbtn = QPushButton(self)
        self.tasksbtn.setFont(self.regfont)
        self.tasksbtn.setStyleSheet("background-color: #4df3ff;")
        self.tasksbtn.setText("Задания")
        self.tasksbtn.resize(811, 121)
        self.tasksbtn.move(10, 232)
        self.theorybtn.clicked.connect(self.gototheory)


    def gototheory(self):
        self.hide()
        self.windowmain = TasksInApp()
        self.windowmain.show()




class RegistrationForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(350, 370)
        self.setWindowTitle("Your Informatics Compass Register")
        self.toname = QLineEdit(self)
        self.toname.resize(250, 30)
        self.toname.move(50, 70)
        self.toname.setPlaceholderText("Псевдоним")
        self.togender = QLineEdit(self)
        self.togender.resize(250, 30)
        self.togender.move(50, 115)
        self.togender.setPlaceholderText("Пол")
        self.topassword = QLineEdit(self)
        self.topassword.resize(250, 30)
        self.topassword.move(50, 160)
        self.topassword.setPlaceholderText("Пароль")
        self.todoublepassword = QLineEdit(self)
        self.todoublepassword.resize(250, 30)
        self.todoublepassword.move(50, 205)
        self.todoublepassword.setPlaceholderText("Повторите пароль")
        self.entrance = QPushButton(self)
        self.entrance.resize(100, 30)
        self.entrance.move(125, 260)
        self.entrance.setText("Войти")
        self.entrance.clicked.connect(self.checktoentrance)
        self.nameerror = QLabel(self)
        self.nameerror.resize(250, 10)
        self.nameerror.move(50, 102)
        self.todoublepassworderror = QLabel(self)
        self.todoublepassworderror.resize(250, 10)
        self.todoublepassworderror.move(50, 237)
        self.hapiningnowlabel = QLabel(self)
        self.hapiningnowlabel.resize(250, 30)
        self.hapiningnowlabel.move(100, 25)
        self.regfont = QFont('Arial', 20)
        self.hapiningnowlabel.setFont(self.regfont)
        self.hapiningnowlabel.setText("Регистрация")


    def checktoentrance(self):
        self.hide()
        self.windowmain = StartApp()
        self.windowmain.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RegistrationForm()
    ex.show()
    sys.exit(app.exec())
