#
#Polina Volnuhina
#014302388
#4/16/2019
#
#lab 3
#CPE 202-13
#Practising how to stack first-in first-out queues using linking. 

class Node:
	def __init__(self,item):
		self.data = item
		self.next = None

class LinkedQueue:
	'''Implements an link-based ,efficient first-in first-out Abstract Data Type'''

	def __init__(self, capacity):
		'''Creates an empty Queue with a capacity'''
		self.capacity = capacity
		self.front = None
		self.end = None
		self.num_items = 0


	def is_empty(self):
		'''Returns True if the Queue is empty, and False otherwise'''
		return self.num_items == 0


	def is_full(self):
		'''Returns True if the Queue is full, and False otherwise'''
		return self.num_items == self.capacity


	def enqueue(self, item):
		'''If Queue is not full, enqueues (adds) item to Queue 
		   If Queue is full when enqueue is attempted, raises IndexError'''
		if self.is_full():
			raise IndexError
		node = Node(item)
		if self.is_empty():
			self.front = node
			self.end = node
		else:
			self.end.next = node
			self.end = node
		self.num_items +=1           


	def dequeue(self):
		'''If Queue is not empty, dequeues (removes) item from Queue and returns item.
		   If Queue is empty when dequeue is attempted, raises IndexError'''
		if self.is_empty():
			raise IndexError
		ret_value = self.front
		self.front = self.front.next
		self.num_items -=1
		return ret_value.data


	def size(self):
		'''Returns the number of elements currently in the Queue, not the capacity'''
		return self.num_items
