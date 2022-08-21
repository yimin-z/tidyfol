import os.path
from platformdirs import *

APP_NAME = "tidyfol"
APP_AUTHOR = "Eminz"

RULES_PATH = os.path.join(user_config_dir(APP_NAME, APP_AUTHOR), "rules.json")
DB_PATH = os.path.join(user_data_dir(APP_NAME, APP_AUTHOR), "tidyfol.db")
