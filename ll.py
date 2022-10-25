# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'll.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginn(object):
    def setupUi(self, loginn):
        loginn.setObjectName("loginn")
        loginn.resize(997, 708)
        self.centralwidget = QtWidgets.QWidget(loginn)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 160, 341, 331))
        self.label.setStyleSheet("background-color: white;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.log_in = QtWidgets.QPushButton(self.centralwidget)
        self.log_in.setGeometry(QtCore.QRect(430, 400, 88, 34))
        self.log_in.setObjectName("log_in")
        self.namee = QtWidgets.QLineEdit(self.centralwidget)
        self.namee.setGeometry(QtCore.QRect(310, 250, 341, 31))
        self.namee.setObjectName("namee")
        self.passwordd = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordd.setGeometry(QtCore.QRect(310, 300, 341, 31))
        self.passwordd.setObjectName("passwordd")
        self.log_name = QtWidgets.QLabel(self.centralwidget)
        self.log_name.setGeometry(QtCore.QRect(440, 200, 131, 21))
        self.log_name.setStyleSheet("color: black;")
        self.log_name.setObjectName("log_name")
        loginn.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(loginn)
        self.statusbar.setObjectName("statusbar")
        loginn.setStatusBar(self.statusbar)

        self.retranslateUi(loginn)
        QtCore.QMetaObject.connectSlotsByName(loginn)

    def retranslateUi(self, loginn):
        _translate = QtCore.QCoreApplication.translate
        loginn.setWindowTitle(_translate("loginn", "LOG IN"))
        self.log_in.setText(_translate("loginn", "login"))
        self.namee.setText(_translate("loginn", "username"))
        self.passwordd.setText(_translate("loginn", "password"))
        self.log_name.setText(_translate("loginn", "LOG IN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginn = QtWidgets.QMainWindow()
    ui = Ui_loginn()
    ui.setupUi(loginn)
    loginn.show()
    sys.exit(app.exec_())
