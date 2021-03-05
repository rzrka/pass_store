from Cryptodome.Cipher import AES
from database import PassStorage
from main_window import UserMainWindow
from write_pass import write_content
from read_pass import read_content
import configparser
import os
from PyQt5.QtWidgets import QApplication, QMessageBox
import sys
import multiprocessing

def padding_text(text):
    pad_len = (16 - len(text) % 16) % 16
    return text + b' ' * pad_len

def _decrypt(text, key):
    cipher = AES.new(key, AES.MODE_CBC, iv=text[:16])
    msg = cipher.decrypt(text[16:])
    return msg

def config_load():
    config = configparser.ConfigParser()
    dir_path = os.getcwd()
    config.read(f'{dir_path}/{"client.ini"}')
    if 'SETTINGS' in config:
        return config
    else:
        config.add_section('SETTINGS')
        config.set('SETTINGS', 'Database_path', '')
        config.set('SETTINGS', 'Database_file', 'client_database.db3')
        return config

def autorize(user_data, database):
    database.user_login(user_data['USER_LOGIN'], user_data['USER_PASS'])

my_login = b'rzrka'
my_pass = b'1234'
my_secret = padding_text(my_login + my_pass)
my_message = b'Hello!'

"""temporary"""

block_id = 1

user_data = {
    'USER_LOGIN': my_login,
    'USER_PASS': my_pass,
    'USER_SECRET': my_secret,
    'USER_MESSAGE': my_message,
}
'''---------------'''
config = config_load()
database = PassStorage(os.path.join(config['SETTINGS']['Database_path'],
                                        config['SETTINGS']['Database_file']))
autorize(user_data, database)



APP = QApplication(sys.argv)
main_window = UserMainWindow(user_data, database)
APP.exec_()







#write_content(user_data, block_id, database)
#print(read_content(user_data, database))


