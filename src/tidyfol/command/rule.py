import json
import os.path

from tidyfol import config


def rule(args):
    print("new rules")


def touch(sub_dir, name="*"):
    with open(config.RULES_PATH) as f:
        rules = json.load(f)

    with open(config.RULES_PATH, "w") as f:
        json.dump(rules, f)


def mkdir(sub_dir):
    with open(config.RULES_PATH) as f:
        rules = json.load(f)

    with open(config.RULES_PATH, "w") as f:
        json.dump(rules, f)


def mv(sub_dir):
    with open(config.RULES_PATH) as f:
        rules = json.load(f)

    with open(config.RULES_PATH, "w") as f:
        json.dump(rules, f)


def rm(sub_dir):
    with open(config.RULES_PATH) as f:
        rules = json.load(f)

    with open(config.RULES_PATH, "w") as f:
        json.dump(rules, f)


def default_rules(restore=False):
    # TODO: add more rules
    rules = [{
        "is_dir": True,
        "Description": "Screen Shots",
        "Screen Shots": [{
            "is_dir": False,
            "name": "Screen Shot*"
        }]
    }, {
        "is_dir": True,
        "Description": "Source Code",
        "Source Code": [{
            "is_dir": True,
            "Description": "Python Code",
            "Python": [{
                "is_dir": False,
                "name": "*.py"
            }]
        }]
    }, {
        "is_dir": True,
        "Description": "Other Files",
        "Other": [{
            "is_dir": False,
            "name": "*"
        }]
    }]

    if restore or (not os.path.exists(config.RULES_PATH)):
        with open(config.RULES_PATH, "w") as f:
            json.dump(rules, f)
