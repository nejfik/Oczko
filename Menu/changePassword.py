from PyQt5 import QtCore, QtGui, QtWidgets

import account
import sqlite3 as sql


class changeForm(object):
    def __init__(self, language):
        self.language = language
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(404, 574)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundLabel = QtWidgets.QLabel(Form)
        self.backgroundLabel.setGeometry(QtCore.QRect(50, 90, 291, 361))
        font = QtGui.QFont()
        font.setBold(False)
        self.backgroundLabel.setFont(font)
        self.backgroundLabel.setStyleSheet("image: url(:/images/changeBackground.png);")
        self.backgroundLabel.setText("")
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.passwordLine = QtWidgets.QLineEdit(Form)
        self.passwordLine.setGeometry(QtCore.QRect(130, 210, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.passwordLine.setFont(font)
        self.passwordLine.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color: rgb(24, 47, 38);\n"
"color: rgb(80, 93, 94);\n"
"padding-bottom: 7px;")
        self.passwordLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLine.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordLine.setDragEnabled(False)
        self.passwordLine.setObjectName("passwordLine")
        self.changeButton = QtWidgets.QPushButton(Form)
        self.changeButton.setGeometry(QtCore.QRect(130, 340, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.changeButton.setFont(font)
        self.changeButton.setStyleSheet("QPushButton#changeButton{\n"
"    background-color: rgb(24, 47, 38);\n"
"    color: rgb(255, 104, 3);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#changeButton:pressed{\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"    background-color: rgb(48, 94, 66);\n"
"    background-position:calc(100%-10px)center;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"    color: rgb(48, 94, 66);\n"
"}\n"
"")
        self.changeButton.setObjectName("changeButton")
        self.statusLabel = QtWidgets.QLabel(Form)
        self.statusLabel.setGeometry(QtCore.QRect(55, 289, 281, 51))
        font = QtGui.QFont()
        font.setBold(False)
        self.statusLabel.setFont(font)
        self.statusLabel.setStyleSheet("color: rgb(255, 46, 56);")
        self.statusLabel.setText("")
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName("statusLabel")
        self.closeLabel = QtWidgets.QLabel(Form)
        self.closeLabel.setGeometry(QtCore.QRect(324, 90, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        self.closeLabel.setFont(font)
        self.closeLabel.setStyleSheet("color: rgb(24, 47, 38);")
        self.closeLabel.setObjectName("closeLabel")
        self.closeButton = QtWidgets.QPushButton(Form)
        self.closeButton.setGeometry(QtCore.QRect(322, 95, 14, 17))
        self.closeButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        self.confirmLine = QtWidgets.QLineEdit(Form)
        self.confirmLine.setGeometry(QtCore.QRect(100, 260, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.confirmLine.setFont(font)
        self.confirmLine.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color: rgb(24, 47, 38);\n"
"color: rgb(80, 93, 94);\n"
"padding-bottom: 7px;")
        self.confirmLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmLine.setAlignment(QtCore.Qt.AlignCenter)
        self.confirmLine.setDragEnabled(False)
        self.confirmLine.setObjectName("confirmLine")

        # Obsługa języków
        if self.language == 1:
            self.backgroundLabel.setStyleSheet("image: url(:/images/changeBackground.png);")
        if self.language == 2:
            self.backgroundLabel.setStyleSheet("image: url(:/images/changeBackgroundPL.png);")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Obsługa przycisków
        self.closeButton.clicked.connect(Form.close)
        self.closeButton.clicked.connect(self.account)

        self.changeButton.clicked.connect(self.new_password)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Change password"))

        # Obsługa języków
        if self.language == 1:
            self.passwordLine.setPlaceholderText(_translate("Form", "NEW PASSWORD"))
            self.changeButton.setText(_translate("Form", "CHANGE"))
            self.closeLabel.setText(_translate("Form", "x"))
            self.confirmLine.setPlaceholderText(_translate("Form", "CONFIRM PASSWORD"))
        if self.language == 2:
            self.passwordLine.setPlaceholderText(_translate("Form", "NOWE HASŁO"))
            self.changeButton.setText(_translate("Form", "ZMIEŃ"))
            self.closeLabel.setText(_translate("Form", "x"))
            self.confirmLine.setPlaceholderText(_translate("Form", "POTWIERDŹ HASŁO"))

    def new_password(self):
        try:
            db = sql.connect('database.db')  # łączymy się do bazy
            c = db.cursor()  # dodajemy kursor

            # c.execute("""CREATE TABLE logged_users (
            #                 id integer,
            #                 username text UNIQUE,
            #                 coins integer,
            #                 games_played integer,
            #                 win_rate integer,
            #                 time_spent integer,
            #                 cards_used integer
            #                 )""")


            password = self.passwordLine.text()
            confirm = self.confirmLine.text()

            query = "SELECT username from logged_users where id = 5"
            c.execute(query)
            db.commit()
            username = c.fetchone()[0]

            query = "SELECT password from users where username = '" + username + "'"
            c.execute(query)
            db.commit()
            current_password = c.fetchone()[0]
        
            if password == "" or confirm == "":
                if self.language == 1:
                    self.statusLabel.setText("Please fill in all the required fields")
                elif self.language == 2:
                    self.statusLabel.setText("Wypełnij wszystkie pola")

            elif password != confirm:
                if self.language == 1:
                    self.statusLabel.setText("Passwords don't match")
                elif self.language == 2:
                    self.statusLabel.setText("Hasła nie są zgodne")

            elif password == confirm == current_password:
                if self.language == 1:
                    self.statusLabel.setText("This is your current password")
                elif self.language == 2:
                    self.statusLabel.setText("To jest Twoje obecne hasło")

            elif len(password) < 6:
                if self.language == 1:
                    self.statusLabel.setText("Password is too short")
                elif self.language == 2:
                    self.statusLabel.setText("Podane hasło jest za krótkie")

            else:

                self.statusLabel.setStyleSheet("color: rgb(51, 204, 51);")
                if self.language == 1:
                    self.statusLabel.setText("Password has changed")
                if self.language == 2:
                    self.statusLabel.setText("Hasło zostało zmienione")
                self.changeButton.setEnabled(False)

                try:
                    c.execute("UPDATE users SET password = '" + password + "' where username = '" + username + "'")
                    db.commit()

                except sql.Error as e:
                    self.statusLabel.setStyleSheet("color: rgb(255, 46, 56);")
                    self.statusLabel.setText("Error")


        except sql.Error as e:
            self.statusLabel.setStyleSheet("color: rgb(255, 46, 56);")
            self.statusLabel.setText("Error")

    def account(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = account.accountForm(self.language)
        self.ui.setupUi(self.window)
        self.window.show()