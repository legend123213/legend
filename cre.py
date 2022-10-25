

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStackedWidget, QMainWindow, QFileDialog, QCheckBox, QListWidgetItem, QPushButton,QApplication

from fun import *
from PIL import *
from lo import *
from test import *
from home import *
from admin_home import *
from signup import *
from show import *
from PyQt5.QtGui import QImage, QPixmap


from PyQt5 import QtCore, QtGui, QtWidgets
class Take():

    name =None
    username = None
    roll = None
    img = None
    contact = None
    year = None
    group = None
    dept = None
    password = None
    language = list(get_lang('Username'))
    working = None
    message = None
    acceptance = None
    def __init__(self,user):
        self.name = user.name
        self.username = user.username
        self.roll = user.roll
        self.contact = user.contact
        self.year =user.year
        self.group = user.group
        self.dept  = user.dept
        self.password = user.password
        self.language = list(get_lang(user.username))
        print(self.name)
        print("DONE")






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
        self.back = QtWidgets.QPushButton(self.frame_2)
        self.back.setObjectName("back")
        self.verticalLayout_3.addWidget(self.working)
        self.verticalLayout_3.addWidget(self.back)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 1, 1, 1, 1)
        self.get_nitem()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.listWidget.itemDoubleClicked.connect(self.get_item)
        self.add_list.clicked.connect(self.add_li)
        self.add_more.clicked.connect(self.add_more_lang)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def add_more_lang(self):
        skill = self.textEdit.toPlainText().split("/")
        for i in skill:
            if i!='':
                language.append(i)
        print(skill)
        print(language)

    def add_li(self):
        add_lang('Username',language)
        wid.setCurrentIndex(wid.currentIndex())
        self.get_nitem()
    def get_item(self, lsa):
        sel_items = self.listWidget.selectedItems()
        if lsa.text() not in language and 'selected' not in lsa.text():
            language.append(lsa.text())
            if language != None and 'selected' not in lsa.text():
                for item in sel_items:
                    item.setText(item.text() + ' selected')

        else:
            h = lsa.text().split(' selected')
            for item in sel_items:
                item.setText(h[0])
            print(str(h[0]))
            language.remove(h[0])
        print(language)

    def get_nitem(self):
        listWidgetItem = QListWidgetItem('')
        self.listWidget.addItem(listWidgetItem)
        listWidgetItem = QListWidgetItem('')
        self.listWidget.addItem(listWidgetItem)
        listWidgetItem = QListWidgetItem('YOU HAVE ')
        self.listWidget.addItem(listWidgetItem)
        for i in language:
            listWidgetItem = QListWidgetItem(i)
            self.listWidget.addItem(listWidgetItem)


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
        self.back.setText(_translate("Form", "back to main page"))

class Ui_adHome(object):
    def setupUi(self, adHome):
        adHome.setObjectName("adHome")
        adHome.resize(924, 618)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        adHome.setFont(font)
        self.centralwidget = QtWidgets.QWidget(adHome)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_14.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_13.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btn_home = QtWidgets.QPushButton(self.frame_3)
        self.btn_home.setObjectName("btn_home")
        self.verticalLayout.addWidget(self.btn_home)
        self.btn_event = QtWidgets.QPushButton(self.frame_3)
        self.btn_event.setObjectName("btn_event")
        self.verticalLayout.addWidget(self.btn_event)
        self.btn_note = QtWidgets.QPushButton(self.frame_3)
        self.btn_note.setObjectName("btn_note")
        self.verticalLayout.addWidget(self.btn_note)
        self.btn_chat = QtWidgets.QPushButton(self.frame_3)
        self.btn_chat.setObjectName("btn_chat")
        self.verticalLayout.addWidget(self.btn_chat)
        self.btn_tem = QtWidgets.QPushButton(self.frame_3)
        self.btn_tem.setObjectName("btn_tem")
        self.verticalLayout.addWidget(self.btn_tem)
        self.btn_mypro = QtWidgets.QPushButton(self.frame_3)
        self.btn_mypro.setObjectName("btn_mypro")
        self.verticalLayout.addWidget(self.btn_mypro)
        self.btn_attend = QtWidgets.QPushButton(self.frame_3)
        self.btn_attend.setObjectName("btn_attend")
        self.verticalLayout.addWidget(self.btn_attend)
        self.btn_edit = QtWidgets.QPushButton(self.frame_3)
        self.btn_edit.setObjectName("btn_edit")
        self.verticalLayout.addWidget(self.btn_edit)
        self.btn_exit = QtWidgets.QPushButton(self.frame_3)
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout.addWidget(self.btn_exit)
        self.gridLayout_11.addWidget(self.frame_3, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.gridLayout_8.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.gridLayout_5.addWidget(self.listWidget, 0, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 368, 471))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.treeWidget = QtWidgets.QTreeWidget(self.scrollAreaWidgetContents)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.gridLayout_6.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_5.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 2, 2)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 741, 467))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.scrollAreaWidgetContents_2)
        self.treeWidget_2.setObjectName("treeWidget_2")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        self.horizontalLayout_2.addWidget(self.treeWidget_2)
        self.listWidget_2 = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.horizontalLayout_2.addWidget(self.listWidget_2)
        self.gridLayout_7.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_10.addWidget(self.scrollArea_2, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 1, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_10, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_11.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_11, 0, 1, 1, 1)
        self.gridLayout_14.addWidget(self.frame, 1, 0, 1, 1)
        adHome.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(adHome)
        self.statusbar.setObjectName("statusbar")
        adHome.setStatusBar(self.statusbar)
        print(self.treeWidget.selectedItems())
        self.go()



        self.retranslateUi(adHome)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(adHome)

    def go(self):

        listicpc = listi()
        listdiv = listd()
        for i in listicpc:
            item = QtWidgets.QTreeWidgetItem(i)
            self.treeWidget.addTopLevelItem(item)
        for j in listdiv:
            itemd = QtWidgets.QTreeWidgetItem(j)
            self.treeWidget_2.addTopLevelItem(itemd)


    def retranslateUi(self, adHome):
        _translate = QtCore.QCoreApplication.translate
        adHome.setWindowTitle(_translate("Home", "Home"))
        self.btn_home.setText(_translate("Home", "Home"))
        self.btn_event.setText(_translate("Home", "Events"))
        self.btn_note.setText(_translate("Home", "Notification"))
        self.btn_chat.setText(_translate("Home", "Chat"))
        self.btn_tem.setText(_translate("Home", "Teams"))
        self.btn_mypro.setText(_translate("Home", "My Profile  "))
        self.btn_attend.setText(_translate("Home", "Attendance"))
        self.btn_edit.setText(_translate("Home", "Edit member"))
        self.btn_exit.setText(_translate("Home", "exit"))
        self.label.setText(_translate("Home", "ICPC Members"))
        self.label_3.setText(_translate("Home", "Found areas"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Home", "Python"))
        item = self.listWidget.item(1)
        item.setText(_translate("Home", "C++"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.treeWidget.headerItem().setText(0, _translate("Home", "NO."))
        self.treeWidget.headerItem().setText(1, _translate("Home", "Name"))
        self.treeWidget.headerItem().setText(2, _translate("Home", "Year"))
        self.treeWidget.headerItem().setText(3, _translate("Home", "Department"))
        self.treeWidget.headerItem().setText(4, _translate("Home", "Score"))
        self.treeWidget.headerItem().setText(5, _translate("Home", "working on"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)

        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Home", "Tab 1"))
        self.treeWidget_2.headerItem().setText(0, _translate("Home", "NO."))
        self.treeWidget_2.headerItem().setText(1, _translate("Home", "Name"))
        self.treeWidget_2.headerItem().setText(2, _translate("Home", "Year"))
        self.treeWidget_2.headerItem().setText(3, _translate("Home", "Department"))
        self.treeWidget_2.headerItem().setText(4, _translate("Home", "Rating"))
        self.treeWidget_2.headerItem().setText(5, _translate("Home", "working on"))
        __sortingEnabled = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)

        self.treeWidget_2.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("Home", "Python"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Home", "Development Members             "))
        self.label_4.setText(_translate("Home", "Language"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Home", "Tab 2"))



class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(924, 618)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        Home.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Home)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_14.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_13.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btn_home = QtWidgets.QPushButton(self.frame_3)
        self.btn_home.setObjectName("btn_home")
        self.verticalLayout.addWidget(self.btn_home)
        self.btn_event = QtWidgets.QPushButton(self.frame_3)
        self.btn_event.setObjectName("btn_event")
        self.verticalLayout.addWidget(self.btn_event)
        self.btn_note = QtWidgets.QPushButton(self.frame_3)
        self.btn_note.setObjectName("btn_note")
        self.verticalLayout.addWidget(self.btn_note)
        self.btn_chat = QtWidgets.QPushButton(self.frame_3)
        self.btn_chat.setObjectName("btn_chat")
        self.verticalLayout.addWidget(self.btn_chat)
        self.btn_tem = QtWidgets.QPushButton(self.frame_3)
        self.btn_tem.setObjectName("btn_tem")
        self.verticalLayout.addWidget(self.btn_tem)
        self.btn_mypro = QtWidgets.QPushButton(self.frame_3)
        self.btn_mypro.setObjectName("btn_mypro")
        self.verticalLayout.addWidget(self.btn_mypro)
        self.btn_exit = QtWidgets.QPushButton(self.frame_3)
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout.addWidget(self.btn_exit)
        self.gridLayout_11.addWidget(self.frame_3, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.gridLayout_8.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.gridLayout_5.addWidget(self.listWidget, 0, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 371, 471))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.treeWidget = QtWidgets.QTreeWidget(self.scrollAreaWidgetContents)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.gridLayout_6.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_5.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 2, 2)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 748, 467))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.scrollAreaWidgetContents_2)
        self.treeWidget_2.setObjectName("treeWidget_2")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        self.horizontalLayout_2.addWidget(self.treeWidget_2)
        self.listWidget_2 = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.horizontalLayout_2.addWidget(self.listWidget_2)
        self.gridLayout_7.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_10.addWidget(self.scrollArea_2, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 1, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_10, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_11.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_11, 0, 1, 1, 1)
        self.gridLayout_14.addWidget(self.frame, 1, 0, 1, 1)
        Home.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Home)
        self.statusbar.setObjectName("statusbar")
        Home.setStatusBar(self.statusbar)

        self.retranslateUi(Home)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Home)
        self.go()

    def go(self):
        listicpc = listi()
        listdiv = listd()
        for i in listicpc:
            item = QtWidgets.QTreeWidgetItem(i)
            self.treeWidget.addTopLevelItem(item)
        for i in listdiv:
            itemd = QtWidgets.QTreeWidgetItem(i)
            self.treeWidget_2.addTopLevelItem(itemd)
    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "Home"))
        self.btn_home.setText(_translate("Home", "Home"))
        self.btn_event.setText(_translate("Home", "Events"))
        self.btn_note.setText(_translate("Home", "Notification"))
        self.btn_chat.setText(_translate("Home", "Chat"))
        self.btn_tem.setText(_translate("Home", "Team"))
        self.btn_mypro.setText(_translate("Home", "My Profile  "))
        self.btn_exit.setText(_translate("Home", "exit"))
        self.label.setText(_translate("Home", "ICPC Members"))
        self.label_3.setText(_translate("Home", "Found areas"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Home", "Python"))
        item = self.listWidget.item(1)
        item.setText(_translate("Home", "C++"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.treeWidget.headerItem().setText(0, _translate("Home", "Name"))
        self.treeWidget.headerItem().setText(1, _translate("Home", "Year"))
        self.treeWidget.headerItem().setText(2, _translate("Home", "Department"))
        self.treeWidget.headerItem().setText(3, _translate("Home", "Score"))
        self.treeWidget.headerItem().setText(4, _translate("Home", "working on"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Home", "nahom"))
        self.treeWidget.topLevelItem(0).setText(1, _translate("Home", "3"))
        self.treeWidget.topLevelItem(0).setText(2, _translate("Home", "cse"))
        self.treeWidget.topLevelItem(0).setText(3, _translate("Home", "322"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Home", "Tab 1"))
        self.treeWidget_2.headerItem().setText(0, _translate("Home", "Name"))
        self.treeWidget_2.headerItem().setText(1, _translate("Home", "Year"))
        self.treeWidget_2.headerItem().setText(2, _translate("Home", "Department"))
        self.treeWidget_2.headerItem().setText(3, _translate("Home", "Rating"))
        __sortingEnabled = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        self.treeWidget_2.topLevelItem(0).setText(0, _translate("Home", "Abel        w"))
        self.treeWidget_2.topLevelItem(0).setText(1, _translate("Home", "3"))
        self.treeWidget_2.topLevelItem(0).setText(2, _translate("Home", "software"))
        self.treeWidget_2.topLevelItem(0).setText(3, _translate("Home", "9"))
        self.treeWidget_2.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("Home", "Python"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Home", "Development Members             "))
        self.label_4.setText(_translate("Home", "Language"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Home", "Tab 2"))



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    Create = QtWidgets.QMainWindow()
    frontt = QtWidgets.QMainWindow()
    signup = QtWidgets.QMainWindow()
    Home = QtWidgets.QMainWindow()
    adHome = QtWidgets.QMainWindow()
    about = QtWidgets.QMainWindow()
    Form = QtWidgets.QWidget()
    wid = QStackedWidget()
    # call windows method
    signupp = Ui_signup()
    signupp.setupUi(signup)
    adhome = Ui_adHome()
    adhome.setupUi(adHome)
    home = Ui_Home()
    home.setupUi(Home)
    ui_form = Ui_Form()
    ui_form.setupUi(Form)
    #ui = Ui_Create()
   # ui.setupUi(Create)
    logg = Ui_loginn()
    logg.setupUi(frontt)
    abu = Ui_about()
    abu.setupUi(about)
    # add widgets to stack
    wid.addWidget(about)
    wid.addWidget(Form)
    wid.addWidget(frontt)
    wid.addWidget(Home)
    wid.addWidget(adHome)
    wid.addWidget(signup)
    wid.addWidget(Create)



    wid.setFixedWidth(1000)
    wid.setFixedHeight(1000)
    wid.show()
    sys.exit(app.exec_())
