from PyQt5 import QtCore, QtGui, QtWidgets

import menu
import replayBoard
import sqlite3 as sql
import re

class historyForm(object):
    def __init__(self, language):
        self.language = language
        self.playersdb = []
        self.movesdb = []

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 601)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.backgroundLabel = QtWidgets.QLabel(Form)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 901, 601))
        self.backgroundLabel.setText("")
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.gamesComboBox = QtWidgets.QComboBox(Form)
        self.gamesComboBox.setGeometry(QtCore.QRect(290, 320, 311, 31))
        self.gamesComboBox.setStyleSheet("color: rgb(255, 170, 0);\n"
"selection-background-color: rgb(62, 121, 84);\n"
"background-color: rgb(48, 94, 66);")
        self.gamesComboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.gamesComboBox.setObjectName("gamesComboBox")
        self.gamesComboBox.addItem("")
        self.gamesComboBox.addItem("")
        self.gamesComboBox.addItem("")
        self.gamesComboBox.addItem("")
        self.gamesComboBox.addItem("")
        self.gamesComboBox.addItem("")
        self.gamesComboBox.addItem("")
        self.gamesComboBox.addItem("")
        self.gamesComboBox.addItem("")
        self.gamesComboBox.addItem("")

        self.playButton = QtWidgets.QPushButton(Form)
        self.playButton.setGeometry(QtCore.QRect(390, 400, 131, 131))
        self.playButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.playButton.setText("")
        self.playButton.setObjectName("playButton")
        self.closeButton = QtWidgets.QPushButton(Form)
        self.closeButton.setGeometry(QtCore.QRect(880, 0, 18, 24))
        self.closeButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        # Obsługa przycisków
        self.closeButton.clicked.connect(Form.close)
        self.closeButton.clicked.connect(self.returnToMenu)

        self.playButton.clicked.connect(Form.close)
        self.playButton.clicked.connect(self.check_data)
        self.playButton.clicked.connect(self.show_replay)

        for i in range(0,10):
            self.get_replay(i)

        # Obsługa języków
        if self.language == 1:
            self.backgroundLabel.setStyleSheet("image: url(:/images/historyBackground.png);")
        if self.language == 2:
            self.backgroundLabel.setStyleSheet("image: url(:/images/historyBackgroundPL.png);")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Games history"))

    def returnToMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = menu.menuForm(self.language)
        self.ui.setupUi(self.window)
        self.window.show()

    def show_replay(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = replayBoard.replayBoardForm(self.language, True, self.playersdb, self.movesdb)
        self.ui.setupUi(self.window)
        self.window.show()

    def check_data(self):
        for i in range(0,10):
            if self.gamesComboBox.currentIndex() == i:
                self.get_replay(i)

    def get_replay(self, id):
        try:
            db = sql.connect('database.db')  # łączymy się do bazy
            c = db.cursor()  # dodajemy kursor

            c.execute("SELECT id, players, moves FROM replays order by id DESC limit 10")

            db.commit()

            result = c.fetchall()
            a = result[id][2]

            b = re.split('[^A-Z0-9]\S', a)
            self.movesdb = list(filter(lambda a: a != '', b))


            a = result[id][1]


            b = re.split('[^A-Za-z0-9\s]', a)
            self.playersdb = list(filter(lambda a: a != '' and a != ' ', b))


            self.gamesComboBox.setItemText(id, "game=" + str(id) + " " + str(self.playersdb))


        except sql.Error as e:
            print("sth wrong with update")
