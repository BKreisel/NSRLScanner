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

if __name__ == '__main__':
    unittest.main()
