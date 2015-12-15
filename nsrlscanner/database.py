""" NSRLScanner Database File Library"""
import sys

def load_database(filename):
    """Verify Existence and File Header of NSRL Database

        :arg filename: name of input file

        :returns file object
    """

    #Python apparently hates multiline strings, gotta remove spaces
    db_header = "\"SHA-1\",\"MD5\",\"CRC32\",\"FileName\",\"FileSize\",\
        \"ProductCode\",\"OpSystemCode\",\"SpecialCode\"\r\n".replace(" ", "")

    try:
        with open(filename, "r") as db:
            file_header = db.readline()
            if  file_header != db_header:
                print("[-] Error: NSRL Database is formatted incorrectly")
                sys.exit(1)
            return filename
    except IOError as e:
        print("[-] File Read Error: " + str(e))
