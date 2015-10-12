import argparse

def create_parser():
    parser = argparse.ArgumentParser(
        description='Check a directory against NIST NSRL Database'
    )

    parser.add_argument(
        'nsrl_db',help='TXT file containing NSRL Database'
    )

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

if __name__ == '__main__':
    main()
