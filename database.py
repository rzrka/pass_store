from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime, Text
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import default_comparator
import datetime

BASE = declarative_base()

class PassStorage:

    class AllUsers(BASE):

        __tablename__ = 'Users'
        id = Column(Integer, primary_key=True)
        login = Column(String, unique=True)
        password = Column(String)

        def __init__(self, login, password):
            self.id = None
            self.login = login
            self.password = password

        def __repr__(self):
            return f'<UserContent({self.id}, {self.login}, {self.password})>'


    class UserBlock(BASE):

        __tablename__ = 'UserBlock'
        id = Column(Integer, primary_key=True)
        user_id = Column(ForeignKey('Users.id'))
        text_pos = Column(String)
        button_pos = Column(String)

        def __init__(self, user_id, text_pos, button_pos):
            self.id = None
            self.user_id = user_id
            self.text_pos = text_pos
            self.button_pos = button_pos

        def __repr__(self):
            return f'<UserBlock({self.id}, {self.user_id}, {self.text_pos}, {self.button_pos})>'


    class UserContent(BASE):

        __tablename__ = 'UserContent'
        id = Column(Integer, primary_key=True)
        user_id = Column(ForeignKey('Users.id'))
        block_id = Column(ForeignKey('UserBlock.id'))
        name = Column(Text)
        content = Column(Text)
        date = Column(DateTime)

        def __init__(self, user_id, block_id, name, content):
            self.id = None
            self.user_id = user_id
            self.block_id = block_id
            self.name = name
            self.content = content
            self.date = datetime.datetime.now()

        def __repr__(self):
            return f'<UserContent({self.id}, {self.user_id}, {self.block_id}, {self.name}, {self.content}, {self.date})>'

    def __init__(self, path):
        self.database_engine = create_engine(f'sqlite:///{path}', echo=False, pool_recycle=7200, connect_args={'check_same_thread': False})
        BASE.metadata.create_all(self.database_engine)

        session = sessionmaker(bind=self.database_engine)
        self.session = session()

        self.session.commit()

    def user_login(self, login, password):
        rez = self.session.query(self.AllUsers).filter_by(login=login)

        if rez.count():
            pass
        else:
            user = self.AllUsers(login, password)
            self.session.add(user)
            self.session.commit()

    def get_user_id(self, login):
        user_id = self.session.query(self.AllUsers).filter_by(login=login)
        return user_id.all()[0].id

    def get_content(self, login, block_id):
        user_id = self.get_user_id(login)
        query = self.session.query(self.UserContent).filter_by(user_id=user_id, block_id=block_id)
        return query.all()[0].content

    def write_content(self, user_id, block_id, name, content):
        rez = self.session.query(self.UserContent).filter_by(user_id=user_id, block_id=block_id)
        if rez.count():
            new_content = rez.first()
            new_content.content = content
        else:
            write = self.UserContent(user_id, block_id, name, content)
            self.session.add(write)
        self.session.commit()

    def add_block_db(self, login, text_pos, button_pos):
        user_id = self.get_user_id(login)
        text_pos = ' '.join(list(map(lambda x: str(x), text_pos)))
        button_pos = ' '.join(list(map(lambda x: str(x), button_pos)))
        block = self.UserBlock(user_id, text_pos, button_pos)
        self.session.add(block)
        self.session.commit()