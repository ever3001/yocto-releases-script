import unittest

import yocto_releases.__main__ as __main__

import sys

class TestSimple(unittest.TestCase):

    def test_main_code_name(self):
        sys.argv = ['yocto_releases', '-c', 'Kirkstone']
        self.assertEqual(__main__.main(), '4.0')
        sys.argv = ['yocto_releases', '-c', 'Dunfell']
        self.assertEqual(__main__.main(), '3.1')
        sys.argv = ['yocto_releases', '-c', 'Zeus']
        self.assertEqual(__main__.main(), '3.0')
    
    def test_main_version(self):
        sys.argv = ['yocto_releases', '-v', '4.0']
        self.assertEqual(__main__.main(), 'Kirkstone')
        sys.argv = ['yocto_releases', '-v', '3.1']
        self.assertEqual(__main__.main(), 'Dunfell')
        sys.argv = ['yocto_releases', '-v', '3.0']
        self.assertEqual(__main__.main(), 'Zeus')

    def test_main_no_args(self):
        sys.argv = ['yocto_releases']
        self.assertEqual(__main__.main(), -1)

if __name__ == '__main__':
    unittest.main()