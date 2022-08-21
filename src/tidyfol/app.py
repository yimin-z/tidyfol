import argparse
import tomli

from tidyfol.command.tidy import tidy
from tidyfol.command.restore import restore
from tidyfol.command.rule import rule, default_rules


def main():
    with open("pyproject.toml", "rb") as f:
        data = tomli.load(f)

    parser = argparse.ArgumentParser(description='Tidy up your folders with simple commands.',
                                     epilog='Github: https://github.com/yimin-z/tidyfol')
    parser.add_argument('--version', action='version',
                        version='%(prog)s {}'.format(data['project']['version']))
    # TODO: Add description
    subparsers = parser.add_subparsers(required=True)

    # tidy subcommand
    parser_tidy = subparsers.add_parser('tidy')
    parser_tidy.add_argument('messy_folder', nargs='?', default='.')
    parser_tidy.add_argument('dst_folder', nargs='?', default='.')
    parser_tidy.set_defaults(func=tidy)

    # restore subcommand
    parser_restore = subparsers.add_parser('restore')
    parser_restore.set_defaults(func=restore)

    # rule subcommand
    parser_rule = subparsers.add_parser('rule')
    parser_rule.set_defaults(func=rule)
    subparsers_rule = parser_rule.add_subparsers(required=True, dest='subcommand')

    # mkdir subcommand of rule
    parser_rule_mkdir = subparsers_rule.add_parser("mkdir")
    parser_rule_mkdir.add_argument('path')

    # add subcommand of rule
    parser_rule_add = subparsers_rule.add_parser("add")
    parser_rule_add.add_argument('path')

    # mv subcommand of rule
    parser_rule_mv = subparsers_rule.add_parser("mv")
    parser_rule_mv.add_argument('from_path')
    parser_rule_mv.add_argument('to_path')

    # rm subcommand of rule
    parser_rule_rm = subparsers_rule.add_parser("rm")
    parser_rule_rm.add_argument('path')

    try:
        args = parser.parse_args()
    except TypeError:
        parser.print_help()
    else:
        # default_rules()
        print(args)
        # args.func(args)
