""" NSRLScanner CLI"""
import argparse
import os
import sys
import time

from tqdm import tqdm

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
    start_time = time.time()

    parser = create_parser()
    args = parser.parse_args()

    if not validate_path(args.path):
        print("[-] Error: Path \"" + args.path + "\" does not exist")
        sys.exit(1)

    filename = db.load_database(args.nsrl_db)

    print("\n[+]  -- Hashing Files --\n")
    scan_list = misc.generate_file_list(args.path)

    hashes = []

    for item in tqdm(scan_list):
        hashes.append(hashylib.HashedPath(item))

    print("\n[+]  -- Scanning Database --\n")

    unmatched_list = sorted(hashylib.scan_database(hashes, filename),
                            key=lambda x: x.get_path())

    print("[+] Files Not in Database: \n")
    for item in unmatched_list:
        print(item.get_path())

    run_time = time.time() - start_time
    no_access= len(filter(lambda x: x.get_hash() == None, hashes))
    actually_scanned = len(scan_list) - no_access
    verified = actually_scanned - len(unmatched_list)
    print("\n[+] -- Statistics --\n")
    print("Execution Time: " + "{0:.1f}".format(run_time) + " seconds")
    print("Targeted Files: " + str(len(scan_list)) + "\n")
    print("Scanned Files: " + str(actually_scanned))
    print("Inaccessable Files: " + str(no_access) + "\n")
    print("Verified Files: " + str(verified))
    print("Unverified Files: " + str(len(unmatched_list)))
if __name__ == '__main__':
    sys.exit(main())
