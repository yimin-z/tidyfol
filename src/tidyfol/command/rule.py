import json
import os.path

from tidyfol import config


def rule(args):
    print("new rules")


def default_rules(restore=False):
    # TODO: add more rules
    rules = [{
        "Screen Shots": {
            "name": "Screen Shot*"
        }
    }, {
        "Other": {
            "name": "*"
        }
    }]

    if restore or (not os.path.exists(config.RULES_PATH)):
        with open(config.RULES_PATH, "w") as f:
            json.dump(rules, f)
