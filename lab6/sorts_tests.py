import unittest
from sorts import *

class TestLab6(unittest.TestCase):

	def test_selection_sort(self):
	   nums = [23, 10, 2]
	   comps = selection_sort(nums)
	   self.assertEqual(comps, 3)
	   self.assertEqual(nums, [2, 10, 23]) #nums

	def test_selection_sort1(self):
	   nums = [23, 10, 2]
	   comps = selection_sort(nums)
	   self.assertEqual(comps, 3)
	   self.assertEqual(nums, [2, 10, 23]) #nums

	def test_selection_sort2(self):
	   nums = [23, 10, 2, 0]
	   comps = selection_sort(nums)
	   self.assertEqual(comps, 6)
	   self.assertEqual(nums, [0, 2, 10, 23]) #nums

	def test_selection_sort3(self):
	   nums = []
	   comps = selection_sort(nums)
	   self.assertEqual(comps, 0)
	   self.assertEqual(nums, []) #nums

	# def test_selection_sort4(self):
	#    nums = [3,2,5,1,6,4]
	#    comps = selection_sort(nums)
	#    self.assertEqual(comps, 15)
	#    self.assertEqual(nums, [1, 2, 3, 4, 5, 6]) #nums

	def test_insertion_sort(self):
		nums = [23, 10]
		comps = insertion_sort(nums)
		self.assertEqual(comps, 1)
		self.assertEqual(nums, [10, 23])


	def test_insertion_sort1(self):  # need to ask because comaprison should be less i think 
		nums = [23, 10, 2, 0]
		comps = insertion_sort(nums)
		self.assertEqual(comps, 6)
		self.assertEqual(nums, [0, 2, 10, 23])

	def test_insertion_sort2(self):
		nums = [23, 0]
		comps = insertion_sort(nums)
		self.assertEqual(comps, 1)
		self.assertEqual(nums, [0, 23])

	def test_insertion_sort3(self):
		nums = [1, 4, 0, 7]
		comps = insertion_sort(nums)
		self.assertEqual(comps, 4)
		self.assertEqual(nums, [0, 1, 4, 7])

	# def test_insertion_sort4(self):
	# 	nums = [3,2,5,1,6,4]
	# 	comps = insertion_sort(nums)
	# 	self.assertEqual(comps, 9)
	# 	self.assertEqual(nums, [1,2,3,4,5,6])

	



if __name__ == '__main__': 
   unittest.main()