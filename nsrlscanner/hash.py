""" NSRLScanner Hashing Library"""
import hashlib
import sys

from tqdm import tqdm

def hash_file(path):
    """MD5 Hash a File

        :arg filename: name of input file

        :returns String containing md5 hash
    """
    md5 = hashlib.md5()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                md5.update(chunk)
            return md5.hexdigest()
    except IOError as e:
        if e.errno == 13:
            print("[!] Warning: Insufficient Permissions to hash file: " + path)
        else:
            print(("[!] Warning: IOError: " + e.strerror))
            return False

class HashedPath(tuple):
    """
        Class to Store Path and Hash Data
    """
    __slots__ = ()

    _fields = ('path', 'hash')

    def __new__(cls, p):
        return tuple.__new__(cls, (p, hash_file(p)))

    def get_hash(self): #pylint: disable=C0111
        return self[1]

    def get_path(self): #pylint: disable=C0111
        return self[0]

def scan_database(hash_list, database):
    """Scan NSRL Database and Print out Results

        :arg hash_list: Array of HashedPath Objects
        :arg database: NSRLDatabase Filename

    """

    #Filter out permission and hashing issues (reported earlier)
    unmatched = filter(lambda x: x.get_hash() != None, hash_list)

    try:
        with open(database, 'r') as db:
            db.readline() # Strip out the header

            for line in tqdm(db):
                items = line.lower().split(",")
                #pylint: disable=W0612
                sha1, md5 = items[0].strip('"'), items[1].strip('"')

                for item in unmatched:
                    if item.get_hash() == md5:
                        unmatched.remove(item)

    except IOError as e:
        print("[-] File Read Error: " + str(e))
        sys.exit(1)

    return unmatched
