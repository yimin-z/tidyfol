import argparse
import tomli

def main():
    data = {}
    with open("pyproject.toml", "rb") as f:
        data = tomli.load(f)

    parser = argparse.ArgumentParser(description='Tidy up your folders with simple commands.',
                                    epilog='Github: https://github.com/yimin-z/tidyfol')
    parser.add_argument('--version', action='version', version='%(prog)s {}'.format(data['project']['version']))

    subparsers = parser.add_subparsers()

    parser_tidy = subparsers.add_parser('tidy')

    parser_restore = subparsers.add_parser('restore')

    args = parser.parse_args()
