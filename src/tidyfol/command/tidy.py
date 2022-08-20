import json

from tidyfol import config


def tidy(args):
    with open(config.RULES_PATH) as f:
        rules = json.load(f)
