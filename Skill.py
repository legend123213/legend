# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Skill1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(984, 577)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 421, 81))
        font = QtGui.QFont()
        font.setFamily("Norasi")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(0, 80, 431, 491))
        self.listWidget.setStyleSheet("background-color:white;\n"
"color: rgb(0, 0, 0);")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(570, 0, 421, 141))
        self.textEdit.setStyleSheet("background-color:white;\n"
"color:black;")
        self.textEdit.setObjectName("textEdit")
        self.working_2 = QtWidgets.QTextEdit(Form)
        self.working_2.setGeometry(QtCore.QRect(570, 310, 411, 141))
        self.working_2.setStyleSheet("background-color:white;\n"
"color:black;")
        self.working_2.setObjectName("working_2")
        self.add_list = QtWidgets.QPushButton(Form)
        self.add_list.setGeometry(QtCore.QRect(280, 40, 88, 34))
        self.add_list.setObjectName("add_list")
        self.working = QtWidgets.QPushButton(Form)
        self.working.setGeometry(QtCore.QRect(880, 460, 101, 41))
        self.working.setObjectName("working")
        self.add_more = QtWidgets.QPushButton(Form)
        self.add_more.setGeometry(QtCore.QRect(870, 160, 111, 41))
        self.add_more.setObjectName("add_more")
        self.remove = QtWidgets.QPushButton(Form)
        self.remove.setGeometry(QtCore.QRect(380, 40, 88, 34))
        self.remove.setObjectName("remove")
        self.working_3 = QtWidgets.QPushButton(Form)
        self.working_3.setGeometry(QtCore.QRect(880, 530, 101, 41))
        self.working_3.setObjectName("working_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Skill_Form"))
        self.label.setText(_translate("Form", " select  Language "))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "Python"))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "C++"))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "C"))
        item = self.listWidget.item(3)
        item.setText(_translate("Form", "Java"))
        item = self.listWidget.item(4)
        item.setText(_translate("Form", "JavaScript"))
        item = self.listWidget.item(5)
        item.setText(_translate("Form", "Html"))
        item = self.listWidget.item(6)
        item.setText(_translate("Form", "CSS"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">for additional skill separate by&quot;/&quot;</p></body></html>"))
        self.working_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Working on </p></body></html>"))
        self.add_list.setText(_translate("Form", "Add"))
        self.working.setText(_translate("Form", "add working..."))
        self.add_more.setText(_translate("Form", "add for more"))
        self.remove.setText(_translate("Form", "remove"))
        self.working_3.setText(_translate("Form", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
