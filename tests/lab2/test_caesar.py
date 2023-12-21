import unittest
import sys
sys.path.insert(0, '/home/kirill/cs102/src')
from lab2.caesar import *

class Test(unittest.TestCase):
        def test_one(self):
                self.assertEqual(encrypt_caesar('PYTHON'), 'SBWKRQ')
        def test_decrypt(self):
                self.assertEqual(decrypt_caesar('SBWKRQ'), 'PYTHON')

if __name__ == '__main__':
         unittest.main()
