import unittest
from location import *

class TestLab1(unittest.TestCase):
	#checks if given location is exactly the same as other location
	def test_repr(self):
		loc = Location("SLO", 35.3, -120.7)
		self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

		loc = Location("Paris", 48.9, 2.4)
		self.assertEqual(repr(loc),"Location('Paris', 48.9, 2.4)")

		loc = Location("SLO", 35.3, -120.7)
		self.assertNotEqual(repr(loc),"Location('Paris', 48.9, 2.4)")

		loc = Location("Paris", 48, 2)
		self.assertNotEqual(repr(loc),"Location('Paris', 48.9, 2.4)")

		oc = Location("SLO", 35, -120)
		self.assertNotEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
	
	# Add more tests!
	# checks if given location is exactly the same as other location with booleans 
	def test_eq(self):
		loc = Location("SLO", 35.3, -120.7)
		other = Location("SLO", 35.3, -120.7)
		self.assertEqual(loc==other, True) #takes exactly two arguments

		loc1 = Location("Paris", 48.9, 2.4)
		other1 = Location("Paris", 48.9, 2.4)
		self.assertEqual(loc1==other1, True)

		loc2 = Location("Paris", 48.9, 2.4)
		other2 = Location("SLO", 35.3, -120.7)
		self.assertEqual(loc2==other2, False)

if __name__ == "__main__":
		unittest.main()














