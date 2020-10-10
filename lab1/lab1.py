#
#Polina Volnuhina
#014302388
#4/07/2019
#
#lab 1
#CPE 202-13
#Practising recursion through finding max number, reversing numbers, and binary search.  

def max_list_iter(int_list):  # must use iteration not recursion
	"""finds the max of a list of numbers and returns the value (not the index)
	If int_list is empty, returns None. If list is None, raises ValueError"""
	if (int_list == []):
		return None
	elif (int_list is None):
			raise ValueError
	else:
		curr_max_num = 0
		for num in int_list:
			if num > curr_max_num:
				curr_max_num = num
		return (curr_max_num) 

def reverse_rec(int_list):   # must use recursion 
	"""recursively reverses a list of numbers and returns the reversed list
	If list is None, raises ValueError"""
	if (int_list == []):
		return None
	elif (int_list is None):
		raise ValueError
	else:
		if len(int_list) == 1:
			return int_list 
		else:
			return (reverse_rec(int_list[1:]) + [int_list[0]])


def bin_search(target, low, high, int_list):  # must use recursion           
	"""searches for target in int_list[low..high] and returns index if found
	If target is not found returns None. If list is None, raises ValueError """
	if (int_list == []):
		return None

	elif (int_list is None): #base case 
		raise ValueError

	elif ((high - low) <= 1):   #checks when one element is left
		if int_list[low] == target:
			return low
		else:
			return None  

	elif high >= 1:  #checks if greater than len(1)
		mid = (low+high)//2  #int(1 + (high)/2)
		if int_list[mid] == target: #if target is directly in the middle
			return mid

		elif int_list[mid] > target: #if target is less than middle check lower bound
			return bin_search(target, low, mid-1, int_list)

		else:
			return bin_search(target, mid+1, high, int_list) #if target is larger than middle check upper bound

	# else:
	# 		return None #target is not present in list





		# if high<= low and list_val[high]!=target:
		# 	return None

		# elif int_list[mid] == target: #switch around the order 
		# 	return mid

		# elif target > int_list[mid]:
		# 	return bin_search(target,mid+1,high,int_list)

		# else:
		# 	if target < int_list[mid]:
		# 		return bin_search(target,low,mid-1,int_list)
