import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()


class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = os.getenv('DB_URL')
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        sessiona_make = sessionmaker(bind=self.__engine)
        self.session = sessiona_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
