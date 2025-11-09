import sys
import csv

from PyQt6.QtWidgets import QApplication, QMainWindow, QButtonGroup, QLineEdit, QWidget, QPushButton, QLabel, \
    QRadioButton
from PyQt6.QtGui import QFont, QColor, QIcon, QPixmap
from PyQt6 import uic
from PyQt6.QtCore import QSize, Qt
from texts_for_theory import all_teories
import pywinstyles
import sqlite3
import os
import hashlib

NUMBER_OF_TEORY = 0
X, Y = 546, 274
COUNT_RESOLVED_CARDS = 0

if not os.path.isfile('forregistrationform.db'):
    connection = sqlite3.connect('forregistrationform.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Acaunts (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    gender TEXT NOT NULL,
    count_card TEXT NOT NULL)
    ''')
    connection.commit()
    connection.close()


class MaterialSelection(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(828, 492)
        self.move(X, Y)
        self.setWindowTitle("Your Informatics Compass")
        self.choose_one_of_numbers = QLabel(self)
        self.choose_one_of_numbers.resize(414, 141)
        self.choose_one_of_numbers.move(207, 25)
        with open("Fibrary.qss", "r") as f:
            qss = f.read()
        self.setStyleSheet(qss)
        self.choose_one_of_numbers.setText(
            """<html><head/><body><p><span style=" font-size:20pt; font-weight:600;">Выберите одно из заданий</span></p></body></html>""")
        self.choose_one_of_numbers.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.returnbtn = QPushButton(self)
        self.returnbtn.move(20, 15)
        self.returnbtn.resize(120, 60)
        self.regfont = QFont('Arial', 12)
        self.returnbtn.setFont(self.regfont)
        self.returnbtn.setText("← Назад")
        self.returnbtn.clicked.connect(self.return_back)
        x, y = 34, 141
        count_num_theoryes = 1
        for btnrow in range(2):
            for btncol in range(5):
                self.newfont = QFont('Arial', 20)
                self.buttonchoice = QPushButton(self)
                self.buttonchoice.resize(140, 140)
                self.buttonchoice.move(x, y)
                self.buttonchoice.setFont(self.newfont)
                self.buttonchoice.setText(f"{count_num_theoryes}")
                count_num_theoryes += 1
                self.buttonchoice.clicked.connect(self.go_to_the_theory)
                x += 151
            y += 151
            x = 34

    def go_to_the_theory(self):
        global NUMBER_OF_TEORY, X, Y
        Y = self.geometry().y() - 31
        X = self.geometry().x()
        NUMBER_OF_TEORY = int(self.sender().text()) - 1
        self.hide()
        self.windowmain = TeoryInApp()
        pywinstyles.apply_style(self.windowmain, "dark")
        self.windowmain.show()

    def return_back(self):
        global X, Y
        Y = self.geometry().y() - 31
        X = self.geometry().x()
        self.hide()
        self.windowmain = StartApp()
        pywinstyles.apply_style(self.windowmain, "dark")
        self.windowmain.show()


class TeoryInApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(828, 492)
        self.move(X, Y)
        self.setWindowTitle("Your Informatics Compass")
        with open("Fibrary.qss", "r") as f:
            qss = f.read()
        self.setStyleSheet(qss)
        self.regfont = QFont('Arial', 12)
        self.appname = QLabel(self)
        self.appname.resize(780, 391)
        self.appname.move(25, 69)
        self.appname.setFont(self.regfont)
        self.appname.setText(all_teories[NUMBER_OF_TEORY])
        self.returnbtn = QPushButton(self)
        self.returnbtn.move(281, 25)
        self.returnbtn.resize(218, 50)
        self.newfont = QFont('Arial', 16)
        self.returnbtn.setFont(self.newfont)
        self.returnbtn.setText("← К теории")

        self.returnbtn.clicked.connect(self.return_back)

    def return_back(self):
        global X, Y
        Y = self.geometry().y() - 31
        X = self.geometry().x()
        self.hide()
        self.windowmain = MaterialSelection()
        pywinstyles.apply_style(self.windowmain, "dark")
        self.windowmain.show()


class StartApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(828, 492)
        self.move(X, Y)
        self.setWindowTitle("Your Informatics Compass")
        with open("for_main_menu.qss", "r") as f:
            qss = f.read()
        self.setStyleSheet(qss)
        self.appname = QLabel(self)
        self.appname.resize(800, 71)
        self.appname.move(20, 20)
        self.regfont = QFont('Arial', 20)
        self.appname.setText(
            """<html><head/><body><p align="center"><span style=" font-size:20pt; font-weight:600;">Your Informatic Compass</span></p></body></html>""")
        self.theorybtn = QPushButton(self)
        self.theorybtn.setFont(self.regfont)
        self.theorybtn.setText("Теория")
        self.theorybtn.resize(623, 121)
        self.theorybtn.move(93, 110)
        self.tasksbtn = QPushButton(self)
        self.tasksbtn.setFont(self.regfont)
        self.tasksbtn.setText("Задания")
        self.tasksbtn.resize(623, 121)
        self.tasksbtn.move(93, 243)
        self.theorybtn.clicked.connect(self.gototheory)

    def gototheory(self):
        global X, Y
        Y = self.geometry().y() - 31
        X = self.geometry().x()
        self.hide()
        self.windowmain = MaterialSelection()
        pywinstyles.apply_style(self.windowmain, "dark")
        self.windowmain.show()


class RegistrationForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(350, 370)
        self.setWindowTitle("Your Informatics Compass Register")
        with open("Fibrary.qss", "r") as f:
            qss = f.read()
        self.setStyleSheet(qss)
        self.toname = QLineEdit(self)
        self.toname.resize(250, 30)
        self.toname.move(50, 70)
        self.toname.setPlaceholderText("Псевдоним")
        self.togendertext = QLabel(self)
        self.togendertext.setStyleSheet("color: 'gray';")
        self.togendertext.setText("Пол:")
        self.togendertext.move(55, 205)
        self.togenderm = QRadioButton(self)
        self.togenderm.move(155, 205)
        self.togenderm.setText("М")
        self.togenderw = QRadioButton(self)
        self.togenderw.move(245, 205)
        self.togenderw.setText("Ж")
        self.topassword = QLineEdit(self)
        self.topassword.resize(250, 30)
        self.topassword.move(50, 118)
        self.topassword.setPlaceholderText("Пароль")
        self.todoublepassword = QLineEdit(self)
        self.todoublepassword.resize(250, 30)
        self.todoublepassword.move(50, 166)
        self.todoublepassword.setPlaceholderText("Повторите пароль")
        self.entrance = QPushButton(self)
        self.entrance.resize(134, 30)
        self.entrance.move(108, 260)
        self.entrance.setText("Зарегестрироваться")
        self.entrance.clicked.connect(self.checktoentrance)
        self.regfont = QFont('Arial', 7)
        self.nameerror = QLabel(self)
        self.nameerror.setFont(self.regfont)
        self.nameerror.setStyleSheet("color: 'gray';")
        self.nameerror.resize(250, 10)
        self.nameerror.move(50, 102)
        self.todoublepassworderror = QLabel(self)
        self.todoublepassworderror.setFont(self.regfont)
        self.todoublepassworderror.setStyleSheet("color: 'gray';")
        self.todoublepassworderror.resize(250, 13)
        self.todoublepassworderror.move(55, 197)
        self.topassworderror = QLabel(self)
        self.topassworderror.setFont(self.regfont)
        self.topassworderror.setStyleSheet("color: 'gray';")
        self.topassworderror.resize(250, 13)
        self.topassworderror.move(55, 148)
        self.togendererror = QLabel(self)
        self.togendererror.setFont(self.regfont)
        self.togendererror.setStyleSheet("color: 'gray';")
        self.togendererror.resize(250, 13)
        self.togendererror.move(55, 230)
        self.hapiningnowlabel = QLabel(self)
        self.hapiningnowlabel.resize(250, 30)
        self.hapiningnowlabel.move(90, 25)
        self.regfont = QFont('Arial', 20)
        self.hapiningnowlabel.setFont(self.regfont)
        self.hapiningnowlabel.setText("Регистрация")
        self.gotoentryformbtn = QPushButton(self)
        self.gotoentryformbtn.setStyleSheet(
            "background-color: #0f0f0f; border: 0px solid #d10000; border-radius: 0px; padding: 5px; color: 'gray'")
        self.gotoentryformbtn.resize(134, 30)
        self.gotoentryformbtn.move(108, 310)
        self.gotoentryformbtn.setText("Войти")
        self.gotoentryformbtn.clicked.connect(self.entry)

    def checktoentrance(self):
        global COUNT_RESOLVED_CARDS
        connection = sqlite3.connect('forregistrationform.db')
        cursor = connection.cursor()
        names = cursor.execute("SELECT username FROM Acaunts").fetchall()
        if len(self.toname.text()) > 20:
            self.nameerror.setText("Имя должно содержать не более 20 символов.")
            self.todoublepassworderror.setText("")
            self.topassworderror.setText("")
            self.togendererror.setText("")
            return
        elif len(self.toname.text()) == 0:
            self.nameerror.setText("Это поле не может быть пустым.")
            self.todoublepassworderror.setText("")
            self.topassworderror.setText("")
            self.togendererror.setText("")
        elif self.toname.text() in names:
            self.nameerror.setText("Это имя уже существует.")
            self.todoublepassworderror.setText("")
            self.topassworderror.setText("")
            self.togendererror.setText("")
            return
        elif len(self.topassword.text()) == 0:
            self.topassworderror.setText("Это поле не может быть пустым.")
            self.nameerror.setText("")
            self.todoublepassworderror.setText("")
            self.togendererror.setText("")
            return
        elif len(self.topassword.text().split()) != 1:
            self.topassworderror.setText("В пароле не должно быть пробелов.")
            self.nameerror.setText("")
            self.todoublepassworderror.setText("")
            self.togendererror.setText("")
            return
        elif self.topassword.text() != self.todoublepassword.text():
            self.todoublepassworderror.setText("Пароли не совпадают.")
            self.nameerror.setText("")
            self.topassworderror.setText("")
            self.togendererror.setText("")
            return
        elif not self.togenderm.isChecked() and not self.togenderw.isChecked():
            self.togendererror.setText("Пол не выбран.")
            self.nameerror.setText("")
            self.topassworderror.setText("")
            self.todoublepassworderror.setText("")
        else:
            gendernow = "М" if self.togenderm.isChecked() else "Ж"
            cursor.execute("""INSERT INTO Acaunts(username, password, gender, count_card) VALUES(?, ?, ?, ?);""", (
                self.toname.text(), hashlib.md5(self.topassword.text().encode("utf-8")).hexdigest(), gendernow,
                COUNT_RESOLVED_CARDS))
            connection.commit()
            cursor.close()
            self.hide()
            self.windowmain = StartApp()
            pywinstyles.apply_style(self.windowmain, "dark")
            self.windowmain.show()

    def entry(self):
        self.hide()
        self.windowmain = Entry_Form()
        pywinstyles.apply_style(self.windowmain, "dark")
        self.windowmain.show()


class Entry_Form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(350, 300)
        self.setWindowTitle("Your Informatics Compass Register")
        with open("Fibrary.qss", "r") as f:
            qss = f.read()
        self.setStyleSheet(qss)
        self.toname = QLineEdit(self)
        self.toname.resize(250, 30)
        self.toname.move(50, 70)
        self.toname.setPlaceholderText("Псевдоним")
        self.topassword = QLineEdit(self)
        self.topassword.resize(250, 30)
        self.topassword.move(50, 118)
        self.topassword.setPlaceholderText("Пароль")
        self.entrance = QPushButton(self)
        self.entrance.resize(134, 30)
        self.entrance.move(108, 175)
        self.entrance.setText("Войти")
        self.entrance.clicked.connect(self.checktoentrance)
        self.regfont = QFont('Arial', 7)
        self.nameerror = QLabel(self)
        self.nameerror.setFont(self.regfont)
        self.nameerror.setStyleSheet("color: 'gray';")
        self.nameerror.resize(250, 10)
        self.nameerror.move(50, 102)
        self.topassworderror = QLabel(self)
        self.topassworderror.setFont(self.regfont)
        self.topassworderror.setStyleSheet("color: 'gray';")
        self.topassworderror.resize(250, 13)
        self.topassworderror.move(55, 148)
        self.hapiningnowlabel = QLabel(self)
        self.hapiningnowlabel.resize(100, 30)
        self.hapiningnowlabel.move(140, 25)
        self.regfont = QFont('Arial', 20)
        self.hapiningnowlabel.setFont(self.regfont)
        self.hapiningnowlabel.setText("Вход")
        self.gotoregistrationformbtn = QPushButton(self)
        self.gotoregistrationformbtn.setStyleSheet(
            "background-color: #0f0f0f; border: 0px solid #d10000; border-radius: 0px; padding: 5px; color: 'gray'")
        self.gotoregistrationformbtn.resize(134, 30)
        self.gotoregistrationformbtn.move(108, 230)
        self.gotoregistrationformbtn.setText("Зарегистрироваться")
        self.gotoregistrationformbtn.clicked.connect(self.registration)

    def checktoentrance(self):
        global COUNT_RESOLVED_CARDS
        connection = sqlite3.connect('forregistrationform.db')
        cursor = connection.cursor()
        all_names_and_passwords = [element for coort in
                                   cursor.execute(
                                       "SELECT username, password, gender, count_card FROM Acaunts").fetchall() for
                                   element in (coort[0] + ' ' + coort[1] + ' ' + coort[2] + ' ' + coort[3]).split()]
        cursor.close()
        if self.toname.text() not in all_names_and_passwords[::4]:
            self.nameerror.setText("Не существует пользователя с таким именем.")
            self.topassworderror.setText("")
            return
        elif hashlib.md5(self.topassword.text().encode("utf-8")).hexdigest() != all_names_and_passwords[
            all_names_and_passwords.index(self.toname.text()) + 1]:
            self.topassworderror.setText("Неверный пароль.")
            self.nameerror.setText("")
            return
        else:
            self.hide()
            self.windowmain = StartApp()
            pywinstyles.apply_style(self.windowmain, "dark")
            self.windowmain.show()

    def registration(self):
        self.hide()
        self.windowmain = RegistrationForm()
        pywinstyles.apply_style(self.windowmain, "dark")
        self.windowmain.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RegistrationForm()
    pywinstyles.apply_style(ex, "dark")
    ex.show()
    sys.exit(app.exec())
