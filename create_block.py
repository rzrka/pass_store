from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QLabel, QComboBox, QPushButton, qApp
from PyQt5.QtCore import Qt


class CreateBlock(QDialog):
    def __init__(self, database):
        super(CreateBlock, self).__init__()
        self.database = database

        self.setFixedSize(711, 475)
        self.setWindowTitle('Впишите название блока и что туда записать')
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setModal(True)

        self.name = QtWidgets.QTextEdit(self)
        self.name.setGeometry(QtCore.QRect(200, 160, 251, 30))
        self.name.setObjectName("name")

        self.text = QtWidgets.QTextEdit(self)
        self.text.setGeometry(QtCore.QRect(200, 200, 251, 71))
        self.text.setObjectName("text")

        self.button_save = QtWidgets.QPushButton('Сохранить и закрыть', self)
        self.button_save.setGeometry(QtCore.QRect(200, 300, 175, 23))
        self.button_save.setObjectName("button_save")

        self.button_exit = QtWidgets.QPushButton('Закрыть без сохранения', self)
        self.button_exit.setGeometry(QtCore.QRect(370, 300, 175, 23))
        self.button_exit.setObjectName("button_exit")

