import os
import re
import unittest

from nsrlscanner import database

class FileTestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_header = "\"SHA-1\",\"MD5\",\"CRC32\",\"FileName\", \
            \"FileSize\",\"ProductCode\",\"OpSystemCode\",\"SpecialCode\" \
            \r\n".replace(" ", "")
        cls.tmpfile = "tmpfile"

class FileTests(FileTestClass):

    def test_bad_file(self):
        write_tmp_file(self.tmpfile,"Scrabdoodle\n")
        with self.assertRaises(SystemExit):
            f = database.load_database(self.tmpfile)
        os.remove(self.tmpfile)

    def test_good_file(self,):
        write_tmp_file(self.tmpfile, self.file_header)
        f = database.load_database(self.tmpfile)
        self.assertTrue(hasattr(f,'read'))
        os.remove(self.tmpfile)

if __name__ == '__main__':
    unittest.main()

#Helper Functions
def write_tmp_file(filename,contents):
    #Write a file to current directory
    with open(filename,'w') as f:
        f.write(contents)
