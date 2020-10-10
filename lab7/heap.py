
class MaxHeap:  #bottom-up

	def __init__(self, capacity=50):
		"""Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
		self.heap_list = [0]
		self.capacity = capacity
		self.size = 0


	def enqueue(self, item):
		"""inserts "item" into the heap, returns true if successful, false if there is no room in the heap"""
		if self.size == self.capacity:
			return False
		else:
			self.size += 1
			self.heap_list.append(item)
			self.perc_up(self.size)
			return True

	def peek(self):
		"""returns max without changing the heap, returns None if the heap is empty"""
		if self.heap_list != []:
			return max(self.heap_list)
		else:
			return None 

	def dequeue(self):
		"""returns max and removes it from the heap and restores the heap property
		   returns None if the heap is empty"""
		if self.heap_list != []:
			max = self.heap_list[1]
			self.heap_list[1] = self.heap_list[self.size]
			self.heap_list.pop()
			self.size -= 1
			self.perc_down(1)
			return max
		else:
			return None


	def contents(self):
		"""returns a list of contents of the heap in the order it is stored internal to the heap.
		(This may be useful for in testing your implementation.)"""
		contents = []
		for element in range(1, len(self.heap_list)):
			contents.append(self.heap_list[element])
		return contents

	def build_heap(self, alist): # Look over this!
		"""Builds a heap from the items in alist and builds a heap using the bottom up method.  
		If the capacity of the current heap is less than the number of 
		items in alist, the capacity of the heap will be increased"""
		if self.capacity < len(alist):
			self.capacity = len(alist)
		i = len(alist) // 2
		self.size = len(alist)
		self.heap_list = [0] + alist
		while i > 0:
			self.perc_down(i)
			i -= 1
		return True

	def is_empty(self):
		"""returns True if the heap is empty, false otherwise"""
		if self.size == 0:
			return True
		else:
			return False 

	def is_full(self):
		"""returns True if the heap is full, false otherwise"""
		if self.size == self.capacity:
			return True 
		else:
			return False 
   
	def get_capacity(self):
		"""this is the maximum number of a entries the heap can hold
		1 less than the number of entries that the array allocated to hold the heap can hold"""
		return self.capacity
	
	def get_size(self):
		"""the actual number of elements in the heap, not the capacity"""
		return self.size

		
	def perc_down(self, i):
		"""where the parameter i is an index in the heap and perc_down moves the element stored
		at that location to its proper place in the heap rearranging elements as it goes."""
		while i * 2 <= self.size:
			child_index = self.child(i)
			if self.heap_list[i] < self.heap_list[child_index]:
				swap = self.heap_list[i] # swap them 
				self.heap_list[i] = self.heap_list[child_index] # swap them 
				self.heap_list[child_index] = swap
			i = child_index

	def child(self, node):  # helper for perc_down
		"""looks for the maximum child for every node (with one or two children present) """
		if node * 2 + 1 > self.size:
			return node * 2
		else:
			if self.heap_list[node * 2 + 1] > self.heap_list[node * 2]:
				return node * 2 + 1
			else:
				return node * 2

		
	def perc_up(self, i):
		"""where the parameter i is an index in the heap and perc_up moves the element stored
		at that location to its proper place in the heap rearranging elements as it goes."""
		while i // 2 > 0:
			if self.heap_list[i] > self.heap_list[i//2]: #floor division 
				swap = self.heap_list[i//2]
				self.heap_list[i//2] = self.heap_list[i]
				self.heap_list[i] = swap
			i = i // 2


	def heap_sort_ascending(self, alist):
		"""perform heap sort on input alist in ascending order
		This method will discard the current contents of the heap, build a new heap using
		the ihs in alist, then mutate alist to put the items in ascending order"""
		self.build_heap(alist)
		while self.size > 0:
			swap = self.heap_list[1]
			self.heap_list[1] = self.heap_list[self.size]
			self.heap_list[self.size] = swap
			self.size -= 1
			self.perc_down(1)
		return self.contents()



