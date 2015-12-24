""" NSRLScanner CLI"""
import argparse
import os
import sys

import database as db
import hash as hashylib
import misc

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

def validate_path(path):
    """ Ensures Path is Real File or Directory

        :arg path: String containing path

        :returns: Boolean for file validity
    """
    path = os.path.expandvars(path)
    if os.path.exists(path):
        return True
    return False


def main():
    """CLI Main Function and Argument Handler"""
    parser = create_parser()
    args = parser.parse_args()

    if not validate_path(args.path):
        print("[-] Error: Path \"" + args.path + "\" does not exist")
        sys.exit(1)

    filename = db.load_database(args.nsrl_db)

    print("\n[+]  -- Hashing Files --\n")
    scan_list = misc.generate_file_list(args.path)

    hashes = []

    for item in scan_list:
        hashes.append(hashylib.HashedPath(item))


if __name__ == '__main__':
    sys.exit(main())
