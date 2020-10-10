import unittest
from lab1 import *

#
#Polina Volnuhina
#014302388
#4/07/2019
#
#lab 1
#CPE 202-13
#Testing recursion through finding max number, reversing numbers, and binary search. 

# A few test cases. Add more!!!
class TestLab1(unittest.TestCase):

	def test_max_list_iter(self):
		"""checks & returns the max number in a passed list (not its index)"""
		tlist = None
		with self.assertRaises(ValueError):  #used to check for exception
			max_list_iter(tlist)

		tlist1 = [2, 4, 6, 8]
		self.assertEqual(max_list_iter(tlist1), (8)) #tests normal list

		tlist2 = []
		self.assertEqual(max_list_iter(tlist2), None) #checks if list is empty 
		
		tlist3 = [2, 3, -1, 50, -10]
		self.assertEqual(max_list_iter(tlist3), 50) #tests normal list

		tlist4 = [5, 5, 5, 5, 5]
		self.assertEqual(max_list_iter(tlist4), 5) #tests all same numbers

	def test_reverse_rec(self):
		"""testing a recursion function that returns a reversed list of numbers"""
		tlist = None
		with self.assertRaises(ValueError):  #checks for exception
			reverse_rec(tlist)

		tlist1 = [1,2,3]
		self.assertEqual(reverse_rec(tlist1),[3,2,1])

		tlist2 = [0,0,-1]
		self.assertEqual(reverse_rec(tlist2), [-1,0,0])

		tlist3 = [2]
		self.assertEqual(reverse_rec(tlist3), [2])

		tlist4 = []
		self.assertEqual(reverse_rec(tlist4), None)

		tlist4 = [0]
		self.assertEqual(reverse_rec(tlist4), [0])


	def test_bin_search(self):   
		"""searches for target and returns the index of the target number if found in list"""  
		list_val =[0,1,2,3,4,7,8,9,10] #testing when target in the middle
		high = len(list_val)-1
		low = 0
		self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)

		list_val1 = [1,2,3,4,5,6] #testing upper bound
		high1 = len(list_val1)-1
		low1 = 0
		self.assertEqual(bin_search(6, 0, len(list_val1)-1, list_val1), 5)

		list_val2 = [2,3,4,5,7,8] #testing lower bound
		high2 = len(list_val2)-1
		low2 = 0
		self.assertEqual(bin_search(2, 0, len(list_val2)-1, list_val2), 0)

		list_val3 = [2,3,4,5,7,8] #testing out of bounds target num
		high3 = len(list_val3)-1
		low3 = 0
		self.assertEqual(bin_search(9, 0, len(list_val3)-1, list_val3), None) 

		low4 = 0 #testing for exception
		high4 = 0
		list_val4 = None
		with self.assertRaises(ValueError): 
			bin_search(0, 0, 0, list_val4)

		list_val5 = [2,3,4,5,7,8] #testing when high = low
		high5 = len(list_val5)-1
		low5 = 5
		self.assertEqual(bin_search(5, 5, len(list_val5)-1, list_val5), None) #checks if target isn't in list

		list_val6 = [2,3,4,5,7,8] #testing when target is none
		high6 = len(list_val6)-1
		low6 = 5
		self.assertEqual(bin_search(0, 5, len(list_val6)-1, list_val6), None)

		list_val7 = [] #testing when list is empty
		high7 = len(list_val7)-1
		low7 = 0
		self.assertEqual(bin_search(21, 0, len(list_val7)-1, list_val7), None)

		list_val8 = [2,3,3,3,3,3,4,5] #testing for multiple targets
		high8 = len(list_val8)-1
		low8 = 0
		self.assertEqual(bin_search(3, 0, len(list_val8)-1, list_val8), 3)

		list_val9 = [1.0,2.0,3.0,4.0,5.0] #testing target in decimal form
		high9 = len(list_val9)-1
		low9 = 0
		self.assertEqual(bin_search(4.0, 0, len(list_val9)-1, list_val9), 3)

		list_val10 = [1,2,3,4,5] #testing when low and high are switched
		low10 = len(list_val10)-1
		high10 = 0
		self.assertEqual(bin_search(2, len(list_val10)-1, 0, list_val10), None)

		list_val11 = [-1.0,-2.0,-3.0,-4.0,-5.0] #testing target in decimal form
		high11 = len(list_val9)-1
		low11 = 0
		self.assertEqual(bin_search(2.0, 0, len(list_val11)-1, list_val11), None)

		list_val12 = [1,2,3,4,5] #testing when low and high are switched and there's target
		low12 = len(list_val12)-1
		high12 = 0
		self.assertEqual(bin_search(5, len(list_val12)-1, 0, list_val12), 4)

        
		


		




		
		
		
		#self.assertEqual(bin_search(6, 2, len(list_val2)-1, list_val2), None) how to test if no target number?

if __name__ == "__main__":
		unittest.main()

