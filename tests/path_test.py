import os
import re
import unittest
import shutil

from nsrlscanner import misc
from tests.database_test import write_tmp_file

class PathTests(unittest.TestCase):

    def test_good_filesystem(self):
        os.mkdir('tmp_dir')
        current_dir = os.path.abspath('./tmp_dir')
        tmp_file1 = os.path.join(current_dir,"tmp_pathfile1")
        tmp_file2 = os.path.join(current_dir,"tmp_pathfile2")
        write_tmp_file(tmp_file1,"NoContent")
        write_tmp_file(tmp_file2,"NoContent")

        known_paths = [ os.path.join(current_dir,"tmp_pathfile1")
                        , os.path.join(current_dir,"tmp_pathfile2") ]

        gen_paths = misc.generate_file_list(os.path.abspath("./tmp_dir"))
        shutil.rmtree("./tmp_dir")
        self.assertTrue(known_paths,gen_paths)

    def test_empty_filesystem(self):
        current_dir = os.path.abspath(".")
        os.mkdir('tmp_dir')
        with self.assertRaises(SystemExit):
            misc.generate_file_list(os.path.join(current_dir,"tmp_dir"))
        shutil.rmtree("./tmp_dir")


if __name__ == '__main__':
    unittest.main()
