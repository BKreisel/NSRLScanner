import os
import unittest

from nsrlscanner import cli
from tests.database_test import write_tmp_file

class CLITestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        parser = cli.create_parser()
        cls.parser = parser

class ArgTests(CLITestClass):

    def test_no_args(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args([])

    def test_one_arg(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['sample.txt'])

    def test_all_args(self):
        args = self.parser.parse_args(['sample.txt','path'])
        self.assertIsNotNone(args.nsrl_db)
        self.assertIsNotNone(args.path)


class PathTests(unittest.TestCase):

    def test_bad_file(self):
        self.assertFalse(cli.validate_path('/filethatdoesntexist'))
    def test_good_file(self):
        write_tmp_file("test_file","")
        self.assertTrue(cli.validate_path('test_file'))
        os.remove("test_file")
    def test_bad_dir(self):
        self.assertFalse(cli.validate_path('/dirthatdoesntexist/'))
    def test_good_dir(self):
        os.makedirs('test_dir')
        self.assertTrue(cli.validate_path('test_dir'))
        os.rmdir('test_dir')

if __name__ == '__main__':
    unittest.main()
