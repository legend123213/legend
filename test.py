from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStackedWidget, QMainWindow, QFileDialog, QCheckBox, QListWidgetItem, QPushButton,QApplication

from fun import *
from PIL import *
from lo import *
from cre import *
class Ui_loginn(object):
    def check_login(self):
            username = self.lineEdit.text()
            password = self.lineEdit_2.text()
            roll = self.checkBox.isChecked()
            bool = test(username, password, roll)
            print(bool)


            if bool == True and roll == False:
                wid.setCurrentIndex(wid.currentIndex() + 1)
                user = quary_user(username)
                Take(user)
            elif bool == True and roll == True:
                wid.setCurrentIndex(wid.currentIndex() + 2)
            else:
                sh(self,frontt,'INCORRECT PASSWORD OR USERNAME SIGNUP TO USE','ERROR')

    def go_sign(self):
        wid.setCurrentIndex(wid.currentIndex() + 3)


    def setupUi(self, frontt):

        frontt.setObjectName("MainWindow")
        frontt.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(frontt)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.gridLayout_2.addLayout(self.verticalLayout, 5, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 4, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 2, 1, 1)
        frontt.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(frontt)
        self.statusbar.setObjectName("statusbar")
        frontt.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.check_login)
        self.pushButton_2.clicked.connect(self.go_sign)

        self.retranslateUi(frontt)
        QtCore.QMetaObject.connectSlotsByName(frontt)

    def retranslateUi(self, frontt):
        _translate = QtCore.QCoreApplication.translate
        frontt.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "                  WELCOME"))
        self.label_2.setText(_translate("MainWindow", "USERNAME"))
        self.label_3.setText(_translate("MainWindow", "PASSWORD"))
        self.label_4.setText(_translate("MainWindow", "LOGIN"))
        self.pushButton.setText(_translate("MainWindow", "LOGIN"))
        self.pushButton_2.setText(_translate("MainWindow", "SIGNUP"))
        self.checkBox.setText(_translate("MainWindow", "Admin"))


