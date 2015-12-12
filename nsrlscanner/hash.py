""" NSRLScanner Hashing Library"""
import hashlib

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
