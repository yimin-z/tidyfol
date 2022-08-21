import json
import os
import os.path

from tidyfol import config


def rule(args):
    if args.subcommand == 'mkdir':
        mkdir(args.path)
    elif args.subcommand == 'add':
        # TODO: add params
        add(args.path)
    elif args.subcommand == 'mv':
        mv(args.from_path, args.to_path)
    elif args.subcommand == 'rm':
        rm(args.path)


def find_file(directory, path, file_type):
    if path == '':
        return directory

    curr_dir = directory
    dirs = os.path.normpath(path).split(os.sep)

    for dir in dirs:
        for i in range(len(curr_dir["contents"])):
            if curr_dir["contents"][i]["name"] == dir and curr_dir["contents"][i]["type"] == file_type:
                curr_dir = curr_dir["contents"][i]
                break
            if i == len(curr_dir["contents"]) - 1:
                return {}

    return curr_dir


def mkdir(path):
    with open(config.RULES_PATH) as f:
        rules = json.load(f)

    head, tail = os.path.split(os.path.normpath(path))
    file = find_file(rules[0], head, 'directory')
    if file:
        file['contents'].append(
            {"type": "directory", "name": tail, "contents": []})
        rules[1]["directories"] += 1
    else:
        print("{}: No such file or directory".format(head))
        return

    with open(config.RULES_PATH, "w") as f:
        json.dump(rules, f)


def add(path, pattern=''):
    with open(config.RULES_PATH) as f:
        rules = json.load(f)

    head, tail = os.path.split(path)
    if tail == '':
        print("{}: is a directory".format(head))
        return

    file = find_file(rules[0], head, 'directory')
    if not file:
        print("{}: No such file or directory".format(head))
        return

    if pattern == '':
        pattern = input(
            "Enter filename pattern (e.g., *.txt) or leave empty: ").strip()
        if pattern == '':
            pattern = '*'

    file['contents'].append({"type": "file", "name": tail, "pattern": pattern})
    rules[1]['files'] += 1

    with open(config.RULES_PATH, "w") as f:
        json.dump(rules, f)


def mv(from_path, to_path):
    with open(config.RULES_PATH) as f:
        rules = json.load(f)

    from_head, from_tail = os.path.split(from_path)
    if from_tail == '':
        from_head, from_tail = os.path.split(os.path.normpath(from_path))
    from_file = find_file(rules[0], from_head, 'directory')
    if not from_file:
        print("{}: No such file or directory".format(from_head))
        return

    to_file = find_file(rules[0], to_path, 'directory')
    if not to_file:
        print("{}: No such file or directory".format(to_path))
        return

    for i in range(len(from_file['contents'])):
        if from_file["contents"][i]["name"] == from_tail:
            target_file = from_file["contents"].pop(i)
            break
        if i == range(len(from_file['contents'])) - 1:
            print("{}: No such file or directory".format(from_path))
            return

    to_file['contents'].append(target_file)

    with open(config.RULES_PATH, "w") as f:
        json.dump(rules, f)


def rm(path):
    with open(config.RULES_PATH) as f:
        rules = json.load(f)

    head, tail = os.path.split(os.path.normpath(path))
    file = find_file(rules[0], head, 'directory')
    if not file:
        print("{}: No such file or directory".format(head))
        return

    for i in range(len(file['contents'])):
        if file["contents"][i]["name"] == tail:
            file["contents"].pop(i)
            rules[1]['files'] -= 1
            break
        if i == range(len(file['contents'])) - 1:
            print("{}: No such file or directory".format(path))
            return

    with open(config.RULES_PATH, "w") as f:
        json.dump(rules, f)


def default_rules(restore=False):
    if (not restore) and os.path.exists(config.RULES_PATH):
        return

    rules = [{"type": "directory", "contents": []},
             {"type": "report", "directories": 0, "files": 0}]
    with open(config.RULES_PATH, "w") as f:
        json.dump(rules, f)

    # TODO: add more rules
    mkdir('Screen Shots')
    add('Screen Shots/screen_shot', 'Screen Shot*')

    mkdir('Source Code')
    mkdir('Python')
    add('Source Code/Python/python', '*.py')
