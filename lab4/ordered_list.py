
# Polina Volnuhina
# 014302388
# 4/25/2019

# lab 4
# CPE 202-13
# Practising doubly-linked list

class Node:
	'''Node for use with doubly-linked list'''
	def __init__(self, data):
		self.data = data 
		self.next = None
		self.prev = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def getPrev(self):
		return self.prev

	def setNext(self, newnext):
		self.next = newnext

	def setPrev(self, newprev):
		self.prev = newprev
				
class OrderedList:
	'''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''
	'''head is smallest items and tail is largest items '''
	def __init__(self):
		'''Use ONE dummy node as described in class'''
		'''***No other attributes***'''
		'''Do not have an attribute to keep track of size'''
		self.head = None
		self.tail = None

	def isEmpty(self):
		'''Returns back True if OrderedList is empty
		MUST have O(1) performance'''
		if self.head is None and self.tail is None:
			return True 
		return False 

	def add(self, item):
		'''Adds an item to OrderedList, in the proper location based on ordering of items
		from lowest (at head of list) to highest (at tail of list)
		If the item is already in the list, do not add it again 
		MUST have O(n) average-case performance'''
		curr = self.head
		prev = curr
		stop = False
		while curr is not None and not stop:
			if curr.getData() > item:
				stop = True
			else:
				prev = curr
				curr = curr.getNext()

		newNode = Node(item)
		if curr is None and prev is None:
			newNode.setNext(self.tail)
			newNode.setPrev(self.head)
			self.head = newNode
			self.tail = newNode

		elif stop is True:
			newNode.setNext(curr)
			newNode.setPrev(curr.getPrev())
			if curr.getPrev() is None:
				self.head = newNode
			else:
				curr.prev.setNext(newNode)
			curr.setPrev(newNode)

		else:
			newNode.setNext(curr)
			newNode.setPrev(prev)
			self.tail = newNode
			prev.setNext(newNode)

	def remove(self, item):
		'''Removes an item from OrderedList. If item is removed (was in the list) returns True
		 If item was not removed (was not in the list) returns False
		 MUST have O(n) average-case performance'''
		# if self.item in self.num_items:
		#   return True 
		# else:
		#   return False
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()

			if self.size() == 1 and current.getData() == item:
				self.head = None
				self.tail = None
			else:
				# Remove the Node (item) if it's between head and a Node
				if current.getPrev() == None:
					self.head = current.getNext()
					current.next.setPrev(self.head)
				# Remove the Node (item) if it's betweem a Node and tail
				elif current.getNext() == None:
					self.tail = current.getPrev()
					current.prev.setNext(self.tail)
				# Remove the Node (item) if it's between two Nodes
				else:
					previous_node = current.getPrev()
					next_node = current.getNext()
					previous_node.setNext(next_node)
					next_node.setPrev(previous_node)
		return found 

	def index(self, item):
		'''Returns index of an item in OrderedList (assuming head of list is index 0).
		If item is not in list, return None
		MUST have O(n) average-case performance'''
		curr = self.head
		found = False
		size = 0
		while curr is not None and not found:
			if curr.getData() == item:
				found = True
			else:
				size += 1
				curr = curr.getNext()
		return size

	def pop(self, index): #check over again
		'''Removes and returns item at index (assuming head of list is index 0).
		If index is negative or >= size of list, raises IndexError
		MUST have O(n) average-case performance'''
		if index < 0 or index >= self.size():
			raise IndexError()
		else:
			curr = self.head
			count = 0
			stop = False
			while curr != None and not stop:
				if count == index:
					found = curr.getData()
					self.remove(found )
					stop = True
				else:
					count += 1
					curr = curr.getNext()
		return found

		# if self.isEmpty():
		#   raise IndexError
		# elif index is None:
		#   while curr is not None:
		#       if curr.next is None:
		#           prev.next(None)
		#           return curr
		#       prev = curr
		#       curr = curr.next
		#   self.head = None
		#   return prev

		# elif index == 0:
		#   self.dummy = curr
		#   return prev

		# curr_index = 0
		# while curr is not None:
		#   if curr_index == index - 1:
		#           try:
		#               prev.setNext(cur.next)
		#               curr.next.setPrev(prev)
		#           except:
		#               prev.setNext(None)
		#               return curr
		#           prev = curr
		#           curr = cur.next
		#           curr_index += 1


	def search(self, item): #recursion
		'''Searches OrderedList for item, returns True if item is in list, False otherwise"
		To practice recursion, this method must call a RECURSIVE method that
		will search the list
		MUST have O(n) average-case performance'''
		curr = self.head
		found = False
		stop = False 
		while curr is not None and not found and not stop:
			if curr.getData() == item:
				found = True 
			else:
				if curr.getData() > item:
					stop = True
				else:
					curr = curr.getNext()
		return found

	def python_list(self):
		'''Return a Python list representation of OrderedList, from head to tail
		For example, list with integers 1, 2, and 3 would return [1, 2, 3]
		MUST have O(n) performance'''
		python_list = []
		curr = self.head
		while curr is not None:
			python_list.append(curr.getData())
			curr = curr.getNext()
		return python_list
				
				

	def python_list_reversed(self): #recursion
		'''Return a Python list representation of OrderedList, from tail to head, using recursion
		For example, list with integers 1, 2, and 3 would return [3, 2, 1]
		To practice recursion, this method must call a RECURSIVE method that
		will return a reversed list
		MUST have O(n) performance'''
		python_list = []
		curr = self.tail
		while curr is not None:
			python_list.append(curr.getData())
			curr = curr.getPrev()
		return python_list
				

	def size(self): #recursion
		'''Returns number of items in the OrderedList
		To practice recursion, this method must call a RECURSIVE method that
		will count and return the number of items in the list
		MUST have O(n) performance'''
		curr = self.head
		num_items = 0
		while curr is not None:
			num_items = num_items + 1
			curr = curr.getNext()
		return num_items  
