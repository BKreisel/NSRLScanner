import os
import re
import unittest

from nsrlscanner import hash
from tests.database_test import write_tmp_file

class HashTests(unittest.TestCase):

    def test_good_file(self):
        write_tmp_file("tmp_hashfile","Scrabdoodle\n")
        md5 = hash.hash_file("tmp_hashfile")
        known_md5 = "0371d05a44bf116ac0c58f59bb3532fd"
        self.assertEqual(md5,known_md5)
        os.remove("tmp_hashfile")

    def test_bad_file(self):
        md5 = hash.hash_file("thisisntarealfileIpromise")
        self.assertFalse(md5)

    def test_no_file(self):
        md5 = hash.hash_file("")
        self.assertFalse(md5)

    def test_perms(self):
        md5 = hash.hash_file("/etc/sudoers")
        self.assertFalse(md5)
if __name__ == '__main__':
    unittest.main()
