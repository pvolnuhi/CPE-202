import unittest
from bears import *

class TestAssign1(unittest.TestCase):
	def test_bear_01(self):
		self.assertTrue(bears(250)) #divisible by 5

	def test_bear_02(self):
		self.assertTrue(bears(42)) #start out with 42

	def test_bear_03(self):
		self.assertFalse(bears(53)) #not divisble by 2,3,4, or 5

	def test_bear_04(self):
		self.assertFalse(bears(41)) #less than 42, cannot get 42 if starting with less than 42

	def test_bear_05(self):
		self.assertTrue(bears(44)) #checks if divisible by 2

	def test_bear_06(self):
		self.assertTrue(bears(63)) #checks if divisible by 3
		
if __name__ == "__main__":
		unittest.main()
