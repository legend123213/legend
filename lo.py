import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


def sh(self, fro, message, title):
    dialog = QtWidgets.QMessageBox(fro)
    dialog.setText(message)
    dialog.setWindowTitle(title)
    dialog.setIcon(QtWidgets.QMessageBox.Critical)
    dialog.setStandardButtons(QMessageBox.Retry |QMessageBox.Cancel )


    dialog.exec_()


