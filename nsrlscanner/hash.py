""" NSRLScanner Hashing Library"""
import hashlib
import sys

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

