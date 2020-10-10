import unittest
from base_convert import *
#num is 10 and base b is from 2-16
class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C") 

    def test_base14(self):
        self.assertEqual(convert(-316,16),"-316")

    def test_base17(self):
        self.assertEqual(convert(316,17),"17")

    def test_base0(self):
        self.assertEqual(convert(0,0),"0")

    def test_base1(self):
        self.assertEqual(convert(1,1),"1")

    def test_base6(self):
        self.assertEqual(convert(1,0),"1")

    def test_base3(self):
        self.assertEqual(convert(0,1),"0")

    def test_base1546(self):
        self.assertEqual(convert(18,0),"0")

    def test_base1546(self):
        self.assertEqual(convert(i, 10), stri(i))

if __name__ == "__main__":
        unittest.main()
