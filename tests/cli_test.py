import os
import unittest

from nsrlscanner import cli

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
        args = self.parser.parse_args(['sample.txt'])
        self.assertIsNotNone(args.nsrl_db)

if __name__ == '__main__':
    unittest.main()
