# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_about(object):
    def setupUi(self, about):
        about.setObjectName("about")
        about.resize(987, 804)
        self.centralwidget = QtWidgets.QWidget(about)
        self.centralwidget.setObjectName("centralwidget")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(670, 30, 251, 231))
        self.label_6.setStyleSheet("background-color:white;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(370, 310, 61, 31))
        font = QtGui.QFont()
        font.setFamily("aakar")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: white;\n"
"\n"
"border-radius:40px;\n"
"color:black;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(450, 320, 81, 41))
        self.label_8.setStyleSheet("background-color: white;\n"
"\n"
"border-radius:40px;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(550, 320, 81, 41))
        self.label_9.setStyleSheet("background-color: white;\n"
"\n"
"border-radius:40px;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(650, 320, 81, 41))
        self.label_10.setStyleSheet("background-color: white;\n"
"\n"
"border-radius:40px;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(760, 320, 81, 41))
        self.label_11.setStyleSheet("background-color: white;\n"
"\n"
"border-radius:40px;")
        self.label_11.setObjectName("label_11")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 350, 291, 211))
        self.plainTextEdit.setStyleSheet("background-color: white;")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(880, 590, 81, 31))
        font = QtGui.QFont()
        font.setFamily("aakar")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: white;\n"
"\n"
"border-radius:40px;\n"
"color:black;")
        self.label_12.setObjectName("label_12")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(790, 660, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 331, 221))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.username = QtWidgets.QLabel(self.widget)
        self.username.setStyleSheet("background-color: white;\n"
"\n"
"border-radius:40px;")
        self.username.setObjectName("username")
        self.verticalLayout.addWidget(self.username)
        self.name = QtWidgets.QLabel(self.widget)
        self.name.setStyleSheet("background-color: white;\n"
"\n"
"border-radius:40px;")
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.roll = QtWidgets.QLabel(self.widget)
        self.roll.setStyleSheet("background-color: white;\n"
"\n"
"border-radius:40px;")
        self.roll.setObjectName("roll")
        self.verticalLayout.addWidget(self.roll)
        self.contact = QtWidgets.QLabel(self.widget)
        self.contact.setStyleSheet("background-color: white;\n"
"\n"
"border-radius:40px;")
        self.contact.setObjectName("contact")
        self.verticalLayout.addWidget(self.contact)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setStyleSheet("background-color: white;\n"
"\n"
"border-radius:40px;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        about.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(about)
        self.statusbar.setObjectName("statusbar")
        about.setStatusBar(self.statusbar)

        self.retranslateUi(about)
        QtCore.QMetaObject.connectSlotsByName(about)

    def retranslateUi(self, about):
        _translate = QtCore.QCoreApplication.translate
        about.setWindowTitle(_translate("about", "about"))
        self.label_7.setText(_translate("about", " Field :"))
        self.label_8.setText(_translate("about", "Python"))
        self.label_9.setText(_translate("about", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#161616;\">csdsx</span></p></body></html>"))
        self.label_10.setText(_translate("about", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#161616;\">csdsx</span></p></body></html>"))
        self.label_11.setText(_translate("about", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#161616;\">csdsx</span></p></body></html>"))
        self.label_12.setText(_translate("about", "Point :"))
        self.pushButton.setText(_translate("about", "Back"))
        self.username.setText(_translate("about", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#161616;\">csdsx</span></p></body></html>"))
        self.name.setText(_translate("about", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#161616;\">csdsx</span></p></body></html>"))
        self.roll.setText(_translate("about", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#161616;\">csdsx</span></p></body></html>"))
        self.contact.setText(_translate("about", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#161616;\">csdsx</span></p></body></html>"))
        self.label_5.setText(_translate("about", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#161616;\">csdsx</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    about = QtWidgets.QMainWindow()
    ui = Ui_about()
    ui.setupUi(about)
    about.show()
    sys.exit(app.exec_())
