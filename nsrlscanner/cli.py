""" NSRLScanner CLI"""
import argparse
import sys

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

    return parser

def main():
    """CLI Main Function and Argument Handler"""
    parser = create_parser()
    args = parser.parse_args()

if __name__ == '__main__':
    sys.exit(main())
