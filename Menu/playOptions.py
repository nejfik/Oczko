from PyQt5 import QtCore, QtGui, QtWidgets
import menu, res, playUsers, warning

class playOptionsForm(object):
    def __init__(self, language):
        self.language = language
        self.playersNumber = -1
        self.computersNumber = -1
        self.betting = 3
        self.warningType = 0

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(530, 732)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.background = QtWidgets.QLabel(Form)
        self.background.setGeometry(QtCore.QRect(0, 0, 511, 711))
        self.background.setStyleSheet("background-color: rgb(24, 47, 38);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.logoIcon = QtWidgets.QLabel(Form)
        self.logoIcon.setText("")
        self.logoIcon.setObjectName("logoIcon")
        self.backgroundDark = QtWidgets.QLabel(Form)
        self.backgroundDark.setGeometry(QtCore.QRect(20, 120, 471, 571))
        self.backgroundDark.setStyleSheet("background-color:rgba(0, 0, 0, 100);\n"
                                          "border-radius:10px;\n"
                                          "")
        self.backgroundDark.setText("")
        self.backgroundDark.setObjectName("backgroundDark")
        self.returnIcon = QtWidgets.QLabel(Form)
        self.returnIcon.setGeometry(QtCore.QRect(471, 8, 31, 31))
        self.returnIcon.setStyleSheet("border-image: url(:/images/return.png);")
        self.returnIcon.setText("")
        self.returnIcon.setObjectName("returnIcon")
        self.onePlayerButton = QtWidgets.QPushButton(Form)
        self.onePlayerButton.setGeometry(QtCore.QRect(140, 200, 71, 71))
        self.onePlayerButton.setStyleSheet("image: url(:/images/one.png);")
        self.onePlayerButton.setText("")
        self.onePlayerButton.setObjectName("onePlayerButton")
        self.playersLabel = QtWidgets.QLabel(Form)
        self.playersLabel.setText("")
        self.playersLabel.setObjectName("playersLabel")
        self.twoPlayersButton = QtWidgets.QPushButton(Form)
        self.twoPlayersButton.setGeometry(QtCore.QRect(220, 200, 71, 71))
        self.twoPlayersButton.setStyleSheet("image: url(:/images/two.png);")
        self.twoPlayersButton.setText("")
        self.twoPlayersButton.setObjectName("twoPlayersButton")
        self.zeroPlayersButton = QtWidgets.QPushButton(Form)
        self.zeroPlayersButton.setGeometry(QtCore.QRect(60, 200, 71, 71))
        self.zeroPlayersButton.setStyleSheet("image: url(:/images/zero.png);")
        self.zeroPlayersButton.setText("")
        self.zeroPlayersButton.setObjectName("zeroPlayersButton")
        self.threePlayersButton = QtWidgets.QPushButton(Form)
        self.threePlayersButton.setGeometry(QtCore.QRect(300, 200, 71, 71))
        self.threePlayersButton.setStyleSheet("image: url(:/images/three.png);")
        self.threePlayersButton.setText("")
        self.threePlayersButton.setObjectName("threePlayersButton")
        self.fourPlayersButton = QtWidgets.QPushButton(Form)
        self.fourPlayersButton.setGeometry(QtCore.QRect(380, 200, 71, 71))
        self.fourPlayersButton.setStyleSheet("image: url(:/images/four.png);")
        self.fourPlayersButton.setText("")
        self.fourPlayersButton.setObjectName("fourPlayersButton")
        self.computersLabel = QtWidgets.QLabel(Form)
        self.computersLabel.setText("")
        self.computersLabel.setObjectName("computersLabel")
        self.zeroComputersButton = QtWidgets.QPushButton(Form)
        self.zeroComputersButton.setGeometry(QtCore.QRect(60, 360, 71, 71))
        self.zeroComputersButton.setStyleSheet("image: url(:/images/zero.png);")
        self.zeroComputersButton.setText("")
        self.zeroComputersButton.setObjectName("zeroComputersButton")
        self.oneComputerButton = QtWidgets.QPushButton(Form)
        self.oneComputerButton.setGeometry(QtCore.QRect(140, 360, 71, 71))
        self.oneComputerButton.setStyleSheet("image: url(:/images/one.png);")
        self.oneComputerButton.setText("")
        self.oneComputerButton.setObjectName("oneComputerButton")
        self.fourComputersButton = QtWidgets.QPushButton(Form)
        self.fourComputersButton.setGeometry(QtCore.QRect(380, 360, 71, 71))
        self.fourComputersButton.setStyleSheet("image: url(:/images/four.png);")
        self.fourComputersButton.setText("")
        self.fourComputersButton.setObjectName("fourComputersButton")
        self.threeComputersButton = QtWidgets.QPushButton(Form)
        self.threeComputersButton.setGeometry(QtCore.QRect(300, 360, 71, 71))
        self.threeComputersButton.setStyleSheet("image: url(:/images/three.png);")
        self.threeComputersButton.setText("")
        self.threeComputersButton.setObjectName("threeComputersButton")
        self.twoComputersButton = QtWidgets.QPushButton(Form)
        self.twoComputersButton.setGeometry(QtCore.QRect(220, 360, 71, 71))
        self.twoComputersButton.setStyleSheet("image: url(:/images/two.png);")
        self.twoComputersButton.setText("")
        self.twoComputersButton.setObjectName("twoComputersButton")
        self.betsLabel = QtWidgets.QLabel(Form)
        self.betsLabel.setText("")
        self.betsLabel.setObjectName("betsLabel")
        self.noBetsLabel = QtWidgets.QLabel(Form)
        self.noBetsLabel.setText("")
        self.noBetsLabel.setObjectName("noBetsLabel")
        self.nextIcon = QtWidgets.QLabel(Form)
        self.nextIcon.setGeometry(QtCore.QRect(130, 570, 251, 111))
        self.nextIcon.setStyleSheet("image: url(:/images/nextInactive.png);")
        self.nextIcon.setText("")
        self.nextIcon.setObjectName("nextIcon")
        self.chipsIcon = QtWidgets.QLabel(Form)
        self.chipsIcon.setGeometry(QtCore.QRect(130, 497, 91, 81))
        self.chipsIcon.setStyleSheet("image: url(:/images/chips.png);")
        self.chipsIcon.setText("")
        self.chipsIcon.setObjectName("chipsIcon")
        self.noChipsIcon = QtWidgets.QLabel(Form)
        self.noChipsIcon.setGeometry(QtCore.QRect(290, 497, 91, 81))
        self.noChipsIcon.setStyleSheet("image: url(:/images/noChips.png);")
        self.noChipsIcon.setText("")
        self.noChipsIcon.setObjectName("noChipsIcon")
        self.betsButton = QtWidgets.QPushButton(Form)
        self.betsButton.setGeometry(QtCore.QRect(140, 500, 71, 71))
        self.betsButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.betsButton.setText("")
        self.betsButton.setObjectName("betsButton")
        self.noBetsButton = QtWidgets.QPushButton(Form)
        self.noBetsButton.setGeometry(QtCore.QRect(300, 500, 71, 71))
        self.noBetsButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.noBetsButton.setText("")
        self.noBetsButton.setObjectName("noBetsButton")
        self.nextButton = QtWidgets.QPushButton(Form)
        self.nextButton.setGeometry(QtCore.QRect(210, 600, 91, 51))
        self.nextButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.nextButton.setText("")
        self.nextButton.setObjectName("nextButton")
        self.returnButton = QtWidgets.QPushButton(Form)
        self.returnButton.setGeometry(QtCore.QRect(470, 10, 31, 31))
        self.returnButton.setStyleSheet("QPushButton { background-color: transparent; border: 0px };")
        self.returnButton.setText("")
        self.returnButton.setObjectName("returnButton")
        self.background.raise_()
        self.logoIcon.raise_()
        self.returnIcon.raise_()
        self.backgroundDark.raise_()
        self.playersLabel.raise_()
        self.zeroPlayersButton.raise_()
        self.onePlayerButton.raise_()
        self.fourPlayersButton.raise_()
        self.threePlayersButton.raise_()
        self.twoPlayersButton.raise_()
        self.computersLabel.raise_()
        self.zeroComputersButton.raise_()
        self.oneComputerButton.raise_()
        self.fourComputersButton.raise_()
        self.threeComputersButton.raise_()
        self.twoComputersButton.raise_()
        self.betsLabel.raise_()
        self.noBetsLabel.raise_()
        self.nextIcon.raise_()
        self.chipsIcon.raise_()
        self.noChipsIcon.raise_()
        self.betsButton.raise_()
        self.noBetsButton.raise_()
        self.nextButton.raise_()
        self.returnButton.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Obsługa języków
        if self.language == 1:
            self.logoIcon.setGeometry(QtCore.QRect(63, 33, 391, 81))
            self.logoIcon.setStyleSheet("border-image: url(:/images/logo.png);")
            self.computersLabel.setStyleSheet("image: url(:/images/computers.png);")
            self.computersLabel.setGeometry(QtCore.QRect(140, 310, 231, 41))
            self.playersLabel.setStyleSheet("image: url(:/images/players.png);")
            self.playersLabel.setGeometry(QtCore.QRect(160, 150, 191, 41))
            self.betsLabel.setGeometry(QtCore.QRect(146, 470, 61, 21))
            self.betsLabel.setStyleSheet("image: url(:/images/bets.png);")
            self.noBetsLabel.setGeometry(QtCore.QRect(298, 466, 81, 21))
            self.noBetsLabel.setStyleSheet("image: url(:/images/noBets.png);")
        elif self.language == 2:
            self.logoIcon.setGeometry(QtCore.QRect(130, 30, 281, 81))
            self.logoIcon.setStyleSheet("border-image: url(:/images/logoPL.png);")
            self.computersLabel.setStyleSheet("image: url(:/images/computersPL.png);")
            self.computersLabel.setGeometry(QtCore.QRect(140, 310, 235, 41))
            self.playersLabel.setStyleSheet("image: url(:/images/playersPL.png);")
            self.playersLabel.setGeometry(QtCore.QRect(172, 150, 171, 31))
            self.betsLabel.setStyleSheet("image: url(:/images/betsPL.png);")
            self.betsLabel.setGeometry(QtCore.QRect(130, 465, 81, 21))
            self.noBetsLabel.setGeometry(QtCore.QRect(270, 460, 131, 31))
            self.noBetsLabel.setStyleSheet("image: url(:/images/noBetsPL.png);")


        # Obsługa przycisków
        self.zeroPlayersButton.clicked.connect(self.zeroPlayers)
        self.onePlayerButton.clicked.connect(self.onePlayer)
        self.twoPlayersButton.clicked.connect(self.twoPlayers)
        self.threePlayersButton.clicked.connect(self.threePlayers)
        self.fourPlayersButton.clicked.connect(self.fourPlayers)
        self.zeroComputersButton.clicked.connect(self.zeroComputers)
        self.oneComputerButton.clicked.connect(self.oneComputer)
        self.twoComputersButton.clicked.connect(self.twoComputers)
        self.threeComputersButton.clicked.connect(self.threeComputers)
        self.fourComputersButton.clicked.connect(self.fourComputers)
        self.returnButton.clicked.connect(self.returnToMenu)
        self.returnButton.clicked.connect(Form.close)
        self.betsButton.clicked.connect(self.bets)
        self.noBetsButton.clicked.connect(self.noBets)

        # self.zeroPlayersButton.clicked.connect(self.optionsSettings)
        # self.onePlayerButton.clicked.connect(self.optionsSettings)
        # self.twoPlayersButton.clicked.connect(self.optionsSettings)
        # self.threePlayersButton.clicked.connect(self.optionsSettings)
        # self.fourPlayersButton.clicked.connect(self.optionsSettings)
        # self.zeroComputersButton.clicked.connect(self.optionsSettings)
        # self.oneComputerButton.clicked.connect(self.optionsSettings)
        # self.twoComputersButton.clicked.connect(self.optionsSettings)
        # self.threeComputersButton.clicked.connect(self.optionsSettings)
        # self.fourComputersButton.clicked.connect(self.optionsSettings)
        # self.betsButton.clicked.connect(self.optionsSettings)
        # self.noBetsButton.clicked.connect(self.optionsSettings)

        # self.zeroPlayersButton.clicked.connect(self.betsVisibility)
        # self.onePlayerButton.clicked.connect(self.betsVisibility)
        # self.twoPlayersButton.clicked.connect(self.betsVisibility)
        # self.threePlayersButton.clicked.connect(self.betsVisibility)
        # self.fourPlayersButton.clicked.connect(self.betsVisibility)
        # self.zeroComputersButton.clicked.connect(self.betsVisibility)
        # self.oneComputerButton.clicked.connect(self.betsVisibility)
        # self.twoComputersButton.clicked.connect(self.betsVisibility)
        # self.threeComputersButton.clicked.connect(self.betsVisibility)
        # self.fourComputersButton.clicked.connect(self.betsVisibility)



        # self.nextButton.setVisible(False)
        self.nextButton.clicked.connect(self.proceed)
        self.nextButton.clicked.connect(Form.close)

        self.nextButton.setEnabled(False)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Game setup"))


    def returnToMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = menu.menuForm(self.language)
        self.ui.setupUi(self.window)
        self.window.show()

    # Paraolimpiada estetyczna - wygaszanie nieużytych opcji

    def zeroPlayers(self):
        self.playersNumber = 0

        self.zeroPlayersButton.setStyleSheet("image: url(:/images/zero.png);")
        self.onePlayerButton.setStyleSheet("image: url(:/images/oneInactive.png);")
        self.twoPlayersButton.setStyleSheet("image: url(:/images/twoInactive.png);")
        self.threePlayersButton.setStyleSheet("image: url(:/images/threeInactive.png);")
        self.fourPlayersButton.setStyleSheet("image: url(:/images/fourInactive.png);")
        self.optionsSettings()


    def onePlayer(self):
        self.playersNumber = 1
        self.onePlayerButton.setStyleSheet("image: url(:/images/one.png);")
        self.zeroPlayersButton.setStyleSheet("image: url(:/images/zeroInactive.png);")
        self.twoPlayersButton.setStyleSheet("image: url(:/images/twoInactive.png);")
        self.threePlayersButton.setStyleSheet("image: url(:/images/threeInactive.png);")
        self.fourPlayersButton.setStyleSheet("image: url(:/images/fourInactive.png);")
        self.optionsSettings()

    def twoPlayers(self):
        self.playersNumber = 2
        self.chipsIcon.setStyleSheet("image: url(:/images/chips.png);")
        self.noChipsIcon.setStyleSheet("image: url(:/images/noChips.png);")
        self.twoPlayersButton.setStyleSheet("image: url(:/images/two.png);")
        self.zeroPlayersButton.setStyleSheet("image: url(:/images/zeroInactive.png);")
        self.onePlayerButton.setStyleSheet("image: url(:/images/oneInactive.png);")
        self.threePlayersButton.setStyleSheet("image: url(:/images/threeInactive.png);")
        self.fourPlayersButton.setStyleSheet("image: url(:/images/fourInactive.png);")
        self.optionsSettings()

    def threePlayers(self):
        self.playersNumber = 3
        self.threePlayersButton.setStyleSheet("image: url(:/images/three.png);")
        self.zeroPlayersButton.setStyleSheet("image: url(:/images/zeroInactive.png);")
        self.onePlayerButton.setStyleSheet("image: url(:/images/oneInactive.png);")
        self.twoPlayersButton.setStyleSheet("image: url(:/images/twoInactive.png);")
        self.fourPlayersButton.setStyleSheet("image: url(:/images/fourInactive.png);")
        self.optionsSettings()

    def fourPlayers(self):
        self.playersNumber = 4
        self.fourPlayersButton.setStyleSheet("image: url(:/images/four.png);")
        self.zeroPlayersButton.setStyleSheet("image: url(:/images/zeroInactive.png);")
        self.onePlayerButton.setStyleSheet("image: url(:/images/oneInactive.png);")
        self.twoPlayersButton.setStyleSheet("image: url(:/images/twoInactive.png);")
        self.threePlayersButton.setStyleSheet("image: url(:/images/threeInactive.png);")
        self.optionsSettings()

    def zeroComputers(self):
        self.computersNumber = 0
        self.zeroComputersButton.setStyleSheet("image: url(:/images/zero.png);")
        self.oneComputerButton.setStyleSheet("image: url(:/images/oneInactive.png);")
        self.twoComputersButton.setStyleSheet("image: url(:/images/twoInactive.png);")
        self.threeComputersButton.setStyleSheet("image: url(:/images/threeInactive.png);")
        self.fourComputersButton.setStyleSheet("image: url(:/images/fourInactive.png);")
        self.optionsSettings()

    def oneComputer(self):
        self.computersNumber = 1
        self.oneComputerButton.setStyleSheet("image: url(:/images/one.png);")
        self.zeroComputersButton.setStyleSheet("image: url(:/images/zeroInactive.png);")
        self.twoComputersButton.setStyleSheet("image: url(:/images/twoInactive.png);")
        self.threeComputersButton.setStyleSheet("image: url(:/images/threeInactive.png);")
        self.fourComputersButton.setStyleSheet("image: url(:/images/fourInactive.png);")
        self.optionsSettings()

    def twoComputers(self):
        self.computersNumber = 2
        self.twoComputersButton.setStyleSheet("image: url(:/images/two.png);")
        self.zeroComputersButton.setStyleSheet("image: url(:/images/zeroInactive.png);")
        self.oneComputerButton.setStyleSheet("image: url(:/images/oneInactive.png);")
        self.threeComputersButton.setStyleSheet("image: url(:/images/threeInactive.png);")
        self.fourComputersButton.setStyleSheet("image: url(:/images/fourInactive.png);")
        self.optionsSettings()

    def threeComputers(self):
        self.computersNumber = 3
        self.threeComputersButton.setStyleSheet("image: url(:/images/three.png);")
        self.zeroComputersButton.setStyleSheet("image: url(:/images/zeroInactive.png);")
        self.oneComputerButton.setStyleSheet("image: url(:/images/oneInactive.png);")
        self.twoComputersButton.setStyleSheet("image: url(:/images/twoInactive.png);")
        self.fourComputersButton.setStyleSheet("image: url(:/images/fourInactive.png);")
        self.optionsSettings()

    def fourComputers(self):
        self.computersNumber = 4
        self.fourComputersButton.setStyleSheet("image: url(:/images/four.png);")
        self.zeroComputersButton.setStyleSheet("image: url(:/images/zeroInactive.png);")
        self.oneComputerButton.setStyleSheet("image: url(:/images/oneInactive.png);")
        self.twoComputersButton.setStyleSheet("image: url(:/images/twoInactive.png);")
        self.threeComputersButton.setStyleSheet("image: url(:/images/threeInactive.png);")
        self.optionsSettings()


    def bets(self):
        self.betting = 1
        self.chipsIcon.setStyleSheet("image: url(:/images/chips.png);")
        self.noChipsIcon.setStyleSheet("image: url(:/images/noChipsInactive.png);")
        self.optionsSettings()


    def noBets(self):
        self.betting = 0
        self.chipsIcon.setStyleSheet("image: url(:/images/chipsInactive.png);")
        self.noChipsIcon.setStyleSheet("image: url(:/images/noChips.png);")
        self.optionsSettings()

    # Funkcja wyłączająca opcję betowania dla komputerów oraz komputera vs gracza
    def betsVisibility(self):

        if self.computersNumber == 0:
            self.betsButton.setEnabled(True)
            self.noBetsButton.setEnabled(True)
            if self.betting == 1:
                self.chipsIcon.setStyleSheet("image: url(:/images/chips.png);")
                self.noChipsIcon.setStyleSheet("image: url(:/images/noChipsInactive.png);")
            elif self.betting == 0:
                self.chipsIcon.setStyleSheet("image: url(:/images/chipsInactive.png);")
                self.noChipsIcon.setStyleSheet("image: url(:/images/noChips.png);")
            else:
                self.noChipsIcon.setStyleSheet("image: url(:/images/noChips.png);")
                self.chipsIcon.setStyleSheet("image: url(:/images/chips.png);")

        elif self.computersNumber >= 1:
            self.betting = 0
            self.chipsIcon.setStyleSheet("image: url(:/images/chipsInactive.png);")
            self.betsButton.setEnabled(False)
            self.noChipsIcon.setStyleSheet("image: url(:/images/noChipsInactive.png);")
            self.noBetsButton.setEnabled(False)

    # Popup z warningiem
    def warning(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = warning.warningForm(self.language, self.warningType)
        self.ui.setupUi(self.window)
        self.window.show()
        QtCore.QTimer.singleShot(3000, self.window.close)

    # Kontrola zastosowanych opcji - wyświetla warningi i uniemożliwia przejście dalej
    def optionsSettings(self):

        self.betsVisibility()
        if self.playersNumber + self.computersNumber > 4:
            self.warningType = 1
            self.nextIcon.setStyleSheet("image: url(:/images/nextInactive.png);")
            self.nextButton.setVisible(False)
            self.nextButton.setEnabled(False)
            self.warning()

        elif self.playersNumber + self.computersNumber < 2:
            self.nextIcon.setStyleSheet("image: url(:/images/nextInactive.png);")
            self.nextButton.setVisible(False)
            self.nextButton.setEnabled(False)


        elif self.computersNumber == 0 and (self.betting != 0 and self.betting != 1):
            self.nextIcon.setStyleSheet("image: url(:/images/nextInactive.png);")
            self.nextButton.setVisible(False)
            self.nextButton.setEnabled(False)


        elif self.computersNumber == -1 or self.playersNumber == -1:
            self.nextIcon.setStyleSheet("image: url(:/images/nextInactive.png);")
            self.nextButton.setVisible(False)
            self.nextButton.setEnabled(False)


        else:
            self.nextIcon.setStyleSheet("image: url(:/images/next.png);")
            self.nextButton.setVisible(True)
            self.nextButton.setEnabled(True)



    def proceed(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = playUsers.usersForm(self.language, self.playersNumber, self.computersNumber, self.betting)
        self.ui.setupUi(self.window)
        self.window.show()
