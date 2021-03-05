# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import qApp
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, qApp, QMainWindow, QWidget, QFormLayout, QScrollArea, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout



class Ui_ContentWindow(object):
    def setupUi(self, MainClientWindow):
        MainClientWindow.setObjectName("MainClientWindow")
        MainClientWindow.resize(1920, 1080)
        MainClientWindow.setMinimumSize(QtCore.QSize(756, 534))
        _translate = QtCore.QCoreApplication.translate
        self.centralwidget = QtWidgets.QWidget(MainClientWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(180, 140, 651, 371))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        '''
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName("textEdit")

        self.textEdit_2 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_2.setObjectName("textEdit_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")

        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")

        self.textEdit_3 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_3.setObjectName("textEdit_3")

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.pushButton_4, 1, 3, 1, 1)
        self.gridLayout.addWidget(self.pushButton_5, 1, 4, 1, 1)
        self.gridLayout.addWidget(self.pushButton_6, 1, 5, 1, 1)
        self.gridLayout.addWidget(self.pushButton_7, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.pushButton_8, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.pushButton_9, 3, 2, 1, 1)
        self.gridLayout.addWidget(self.textEdit_3, 2, 0, 1, 3)
        self.gridLayout.addWidget(self.textEdit_2, 0, 3, 1, 3)
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 3)
        '''
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(460, 450, 131, 31))
        self.btn_add.setObjectName("btn_add")

        MainClientWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainClientWindow)

        QtCore.QMetaObject.connectSlotsByName(MainClientWindow)

    def retranslateUi(self, MainClientWindow):
        _translate = QtCore.QCoreApplication.translate
        MainClientWindow.setWindowTitle(_translate("MainClientWindow", "Pass Store alpha release"))
        self.btn_add.setText(_translate("MainClientWindow", "Добавить окно"))
