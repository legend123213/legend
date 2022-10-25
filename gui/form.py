# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Skill.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1117, 605)
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Norasi")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(self.frame)
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
        self.verticalLayout_2.addWidget(self.listWidget)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.add_list = QtWidgets.QPushButton(self.frame)
        self.add_list.setObjectName("add_list")
        self.verticalLayout.addWidget(self.add_list)
        self.remove = QtWidgets.QPushButton(self.frame)
        self.remove.setObjectName("remove")
        self.verticalLayout.addWidget(self.remove)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 0, 0, 2, 1)
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textEdit = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit.setStyleSheet("background-color:white;\n"
"color:black;")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_4.addWidget(self.textEdit)
        self.add_more = QtWidgets.QPushButton(self.frame_3)
        self.add_more.setObjectName("add_more")
        self.verticalLayout_4.addWidget(self.add_more)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_3, 0, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.working_2 = QtWidgets.QTextEdit(self.frame_2)
        self.working_2.setStyleSheet("background-color:white;\n"
"color:black;")
        self.working_2.setObjectName("working_2")
        self.verticalLayout_3.addWidget(self.working_2)
        self.working = QtWidgets.QPushButton(self.frame_2)
        self.working.setObjectName("working")
        self.verticalLayout_3.addWidget(self.working)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Skill_Form"))
        self.label.setText(_translate("Form", " Select Language "))
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
        self.add_list.setText(_translate("Form", "Add"))
        self.remove.setText(_translate("Form", "remove"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">for additional skill separate by&quot;/&quot;</p></body></html>"))
        self.add_more.setText(_translate("Form", "add for more"))
        self.working_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Working on </p></body></html>"))
        self.working.setText(_translate("Form", "add working..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
