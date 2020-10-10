#
#Polina Volnuhina
#014302388
#4/16/2019
#
#lab 2
#CPE 202-13
#Practising how to stack using arrays.  

class Stack:
	'''Implements an efficient last-in first-out Abstract Data Type using a Python List'''

	def __init__(self, capacity):
		'''Creates and empty stack with a capacity'''
		self.capacity = capacity
		self.items = [None]*capacity
		self.num_items = 0 

	def is_empty(self):
		'''Returns True if the stack is empty, and False otherwise
		   MUST have O(1) performance'''
		if self.num_items == 0:
			return True
		else:
			return False

	def is_full(self):
		'''Returns True if the stack is full, and False otherwise  
		   MUST have O(1) performance'''
		if self.num_items == self.capacity:
			return True
		else:
			return False

	def push(self, item):
		'''If stack is not full, pushes item on stack. 
		   If stack is full when push is attempted, raises IndexError
		   MUST have O(1) performance'''
		if self.num_items == self.capacity: #stack is full
			raise IndexError
		self.items[self.num_items] = item #pushes item to stack 
		self.num_items += 1

	def pop(self): 
		'''If stack is not empty, pops item from stack and returns item.
		   If stack is empty when pop is attempted, raises IndexError
		   MUST have O(1) performance'''
		if self.num_items == 0:
			raise IndexError
		pops = self.items[self.num_items - 1]
		self.num_items -= 1
		return pops


	def peek(self):
		'''If stack is not empty, returns next item to be popped (but does not pop the item)
		   If stack is empty, raises IndexError
		   MUST have O(1) performance'''
		if self.is_empty():
			raise IndexError
		return self.items[self.num_items - 1]

	def size(self):
		'''Returns the number of elements currently in the stack, not the capacity
		   MUST have O(1) performance'''
		return self.num_items

 

 
