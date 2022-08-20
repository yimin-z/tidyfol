import sqlite3
from platformdirs import *

from tidyfol import config


def connect_db():
    con = sqlite3.connect(config.DB_PATH)


def store_meta(path):
    pass


def get_meta(path):
    pass
