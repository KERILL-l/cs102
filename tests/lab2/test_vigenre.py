import unittest
from src.lab2.vigenre import encrypt_vigenere
from src.lab2.vigenre import decrypt_vigenere


class Test(unittest.TestCase):
    def test_encryption(self):
        assert encrypt_vigenere('', keyword='ABC') == ''
        assert encrypt_vigenere('carl stole coral from clara', keyword='clarinet') == 'elrc agseg noiiy jkqx cciee'
        assert encrypt_vigenere('carL stole coral From clara', keyword='clarinet') == 'elrC agseg noiiy Jkqx cciee'
        assert encrypt_vigenere('zzz', keyword='zzz') == 'yyy'

    def test_decryption(self):
        assert decrypt_vigenere('', keyword='ABC') == ''
        assert decrypt_vigenere('elrc agseg noiiy jkqx cciee', keyword='clarinet') == 'carl stole coral from clara'
        assert decrypt_vigenere('elrc agSeg noiiy jkqx cCiee', keyword='clarinet') == 'carl stOle coral from cLara'
        assert decrypt_vigenere('zzz', keyword='zzz') == 'aaa'
