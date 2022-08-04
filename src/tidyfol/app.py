import sys
import argparse
import tomli

from tidyfol.command.tidy import tidy
from tidyfol.command.restore import restore

def main():
    data = {}
    with open("pyproject.toml", "rb") as f:
        data = tomli.load(f)

    parser = argparse.ArgumentParser(description='Tidy up your folders with simple commands.',
                                    epilog='Github: https://github.com/yimin-z/tidyfol')
    parser.add_argument('--version', action='version', version='%(prog)s {}'.format(data['project']['version']))
    # TODO: Add description
    subparsers = parser.add_subparsers(required=True)

    parser_tidy = subparsers.add_parser('tidy')
    parser_tidy.add_argument('messy_folder', nargs='?', default='.')
    parser_tidy.add_argument('dst_folder', nargs='?', default='.')
    parser_tidy.set_defaults(func=tidy)

    parser_restore = subparsers.add_parser('restore')
    parser_restore.set_defaults(func=restore)

    args = None
    try:
        args = parser.parse_args()
    except:
        if len(sys.argv) == 1:
            parser.print_help()
        elif sys.argv[1] == 'tidy':
            parser_tidy.print_help()
        elif sys.argv[1] == 'restore':
            parser_restore.print_help()
    else:
        print(args)
        args.func(args)
