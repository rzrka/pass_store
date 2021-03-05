import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, qApp, QMainWindow, QWidget, QFormLayout, QScrollArea, QVBoxLayout, QHBoxLayout, QPushButton
from main_window_conv import Ui_ContentWindow
from write_pass import write_content
from create_block import CreateBlock
from Cryptodome.Cipher import AES
import ast


def _decrypt(text, key):
    cipher = AES.new(key, AES.MODE_CBC, iv=text[:16])
    msg = cipher.decrypt(text[16:])
    return msg

def padding_text(text):
    text = bytes(text, 'utf-8')
    pad_len = (16 - len(text) % 16) % 16
    return text + b' ' * pad_len

def _encrypt(text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.iv + cipher.encrypt(text)
    return ciphertext


class UserMainWindow(QMainWindow):
    def __init__(self, user_data, database):
        super().__init__()
        self.user_data = user_data
        self.database = database
        self.user_id = self.database.get_user_id(user_data['USER_LOGIN'])
        self.current_block = None
        self.rez = self.database.session.query(self.database.UserBlock).filter_by(user_id=self.user_id)
        self.block_id = self.rez.count()

        self.ui = Ui_ContentWindow()
        self.ui.setupUi(self)
        self.grid = self.ui.gridLayout
        self.get_user_window()




        self.ui.btn_add.clicked.connect(self.add_block)
        self.show()

    def get_user_window(self):
        self.names = {
            'None': '',
            'save': 'Сохранить',
            'edit': 'Редактировать',
            'delete': 'Удалить',
        }
        if self.rez.count():
            for el in zip(self.rez.all()):
                self.text_pos = list(map(int, el[0].text_pos.split()))
                self.button_pos = list(map(int, el[0].button_pos.split()))
                self.draw_blocks()
        else:
            pass

    def draw_blocks(self, content=''):

        text = QtWidgets.QTextEdit(self.names['None'])
        self.btn_save = QtWidgets.QPushButton(self.names['save'])
        self.btn_edit = QtWidgets.QPushButton(self.names['edit'])
        self.btn_delete = QtWidgets.QPushButton(self.names['delete'])

        self.btn_edit.clicked.connect(lambda: self.btn_edit_action(self.block_id))

        self.grid.addWidget(text, *self.text_pos)
        text.setText(content)
        self.grid.addWidget(self.btn_save, *self.button_pos)
        self.button_pos[1] = self.button_pos[1] + 1
        self.grid.addWidget(self.btn_edit, *self.button_pos)
        self.button_pos[1] = self.button_pos[1] + 1
        self.grid.addWidget(self.btn_delete, *self.button_pos)
        self.button_pos[1] = self.button_pos[1] + 1
        self.text_pos[1] = self.text_pos[1] + 3

    def btn_edit_action(self, id_block):
        pass

    def add_block(self):
        global create_block
        create_block = CreateBlock(self.database)
        create_block.button_exit.clicked.connect(qApp.quit)
        create_block.button_save.clicked.connect(lambda: self.add_block_action(create_block))
        create_block.show()

    def add_block_action(self, item):
        name = item.name.toPlainText()
        text = item.text.toPlainText()
        if self.rez.count():
            self.text_pos = list(map(int, self.rez.all()[-1].text_pos.split()))
            self.button_pos = list(map(int, self.rez.all()[-1].button_pos.split()))
            if self.rez.count() % 3 != 0:
                self.button_pos[1] = self.button_pos[1] + 3
                self.text_pos[1] = self.text_pos[1] + 3
            else:
                self.text_pos[1] = 0
                self.text_pos[0] = self.text_pos[0] + 2
                self.button_pos[1] = 0
                self.button_pos[0] = self.button_pos[0] + 2
            self.database.add_block_db(self.user_data['USER_LOGIN'], self.text_pos, self.button_pos)
            self.draw_blocks()
        else:
            self.text_pos = [0, 0, 1, 3]
            self.button_pos = [1, 0, 1, 1]
            self.database.add_block_db(self.user_data['USER_LOGIN'], self.text_pos, self.button_pos)
            self.write_content(name, text)
            self.draw_blocks(text)

        create_block.close()

    def write_content(self, name, text):
        if text:
            text = padding_text(text)
            text = _encrypt(text, self.user_data['USER_SECRET'])
            self.database.write_content(self.user_id, self.block_id + 1, name, text)
        else:
            self.database.write_content(self.user_id, self.block_id + 1, name, text)

    def get_content(self):
        try:
            record = self.database.get_content(self.user_data['USER_LOGIN'], self.block_id)
            text = str(_decrypt(record, self.user_data['USER_SECRET']).strip(), 'utf-8')
            return text
        except:
            return 'ERROR'

