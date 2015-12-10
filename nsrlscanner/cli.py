""" NSRLScanner CLI"""
import argparse
import sys

import database as db

def create_parser():
    """ Create Parser Object

        :returns: parser object
    """
    parser = argparse.ArgumentParser(
        description='Check a directory against NIST NSRL Database'
    )

    parser.add_argument(
        'nsrl_db', help='TXT file containing NSRL Database'
    )
    parser.add_argument(
        'path', help='file or directory to scan'
    )
    return parser

def main():
    """CLI Main Function and Argument Handler"""
    parser = create_parser()
    args = parser.parse_args()

    db_file = db.load_database(args.nsrl_db)

if __name__ == '__main__':
    sys.exit(main())
