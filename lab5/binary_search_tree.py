# Polina Volnuhina
# 014302388
# 5/08/2019

# lab 5
# CPE 202-13
# Practising binary search tree


class TreeNode:
	def __init__(self, key, data, left=None, right=None, parent=None):
		self.key = key
		self.data = data
		self.left = left
		self.right = right
		self.parent = parent


	def insert(self,key):
		"""  Insert new node with key, assumes data not present """
		if self.key != None:
			if key < self.key:
				if self.left is None:
					self.left = TreeNode(key)
					self.left.parent = self
				else:
				   self.left.insert(key)
			elif key > self.key:
				if self.right is None:
					self.right = TreeNode(key)
					self.right.parent = self
				else:
					self.right.insert(key)
		else:
			self.key = key

	# def find_max(self): # returns a tuple with max key and data in the BST
	# 	# returns None if the tree is empty
	# 	if self.is_empty():
	# 		return None
	# 	node = self.root
	# 	while node.right is not None:
	# 		node = node.right
	# 	return node

	def inorder_list(self): # return Python list of BST keys representing in-order traversal of BST
		if self is not None:
			if self.left():
				self.left.inorder_list()
			return self.key
			if self.right():
				self.right.inorder_list()

	def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
	#not sure how to do this
		list1 = []
		if root:
			list1.append(root.data)
			list1 = list1 + self.preorder_list(root.left)
			list1 = list1 + self.preorder_list(root.right)
		return list1



	# Determines if the TreeNode has a left child
	# TreeNode -> Boolean
	def has_left_child(self):
		return self.left is not None

	# Determines if the TreeNode has a right child
	# TreeNode -> Boolean
	def has_right_child(self):
		return self.right is not None

	# Determines if the TreeNode has any children
	# TreeNode -> Boolean
	def has_any_children(self):
		return self.left is not None or self.right is not None

	# Determines if the TreeNode has both a left and right child
	# TreeNode -> Boolean
	def has_both_children(self):
		return self.left is not None and self.right is not None

	# Determines if the TreeNode has a parent
	# TreeNode -> Boolean
	def has_parent(self):
		return self.parent is not None

	# Determines if the TreeNode is the left child
	# TreeNode -> Boolean
	def is_left_child(self):
		return self.has_parent() and self.parent.left == self

	# Determines if the TreeNode is the right child
	# TreeNode -> Boolean
	def is_right_child(self):
		return self.has_parent() and self.parent.right == self

	# Determines if the TreeNode is a leaf
	# TreeNode -> Boolean
	def is_leaf(self):
		return self.left is None and self.right is None




	def find_successor(self):
		""" Finds the next successor of a TreeNode """
		if self.right == None:
			return self
		current = self.right
		while current.left != None:
			current = current.left
		return current


	def find_min(self): # returns a tuple with min key and data in the BST
		# returns None if the tree is empty
		if not self.has_left_child():
			return self
		else:
			return self.left.find_min()
		# if self.is_empty():
		# 	return None
		# node = self.root
		# while node.left is not None:
		# 	node = node.left
		# return node

	def find_max(self):
		if not self.has_right_child():
			return self
		else:
			return self.right.find_max()

	# Helper function for removing a TreeNode
	# TreeNode -> None
	def delete(self):
		if self.is_leaf():
			if self.is_left_child():
				self.parent.left = None
			else:
				self.parent.right = None
		elif self.has_any_children():
			if self.has_left_child():
				if self.is_left_child():
					self.parent.left = self.left
				else:
					self.parent.right = self.left
				self.left.parent = self.parent
			else:
				if self.is_left_child():
					self.parent.left = self.right
				else:
					self.parent.right = self.right
				self.right.parent = self.parent


class BinarySearchTree:

	def __init__(self):  # Returns empty BST
		self.root = None


	def is_empty(self):  # returns True if tree is empty, else False
		if self.root == None:
			return True
		else:
			return False

	def search(self, key):  # returns True if key is in a node of the tree, else False
		node = self.root
		while node != None:
			if key < node.key:
				node = node.left
			elif key > node.key:
				node = node.right
			else:
				return node
		return None


	def insert(self, key, data=None):  # inserts new node w/ key and data
		# If an item with the given key is already in the BST,
		# the data in the tree will be replaced with the new data
		# Example creation of node: temp = TreeNode(key, data)
		temp = TreeNode(key, data)
		if self.root == None:
			self.root = temp
			return self.root
		else:
			node = self.root
			while node is not None:
				if key < node.key:
					if node.left is None:
						node.left = temp
						temp.parent = node
						break
					else:
						node = node.left
				elif key > node.key:
					if node.right is None:
						node.right = temp
						temp.parent = node
						break
					else:
						node = node.right

	def subtree_height(self, node):
		if node is None:
			return 0
		else:
			left_depth = self.subtree_height(node.left)
			right_depth = self.subtree_height(node.right)
			# Use the larger one
			if (left_depth > right_depth):
				return left_depth + 1
			else:
				return right_depth + 1

	def tree_height(self):  # return the height of the tree
		# returns None if tree is empty
		return self.subtree_height(self.root)

	# def delete(self, key):
	# 	while node.key != key:
	# 		node = self.root
	# 		if key < node.key:
	# 			node = node.left
	# 		else:
	# 			node = node.right
	# 	self.node_delete(node)

		
	def node_delete(self, key): # deletes node containing key
		# Will need to consider all cases 
		# This is the most difficult method - save it for last, so that
		# if you cannot get it to work, you can still get credit for 
		# the other methods
		# Returns True if the item was deleted, False otherwise

		# No child case
		node = self.root
		if node.left == None and node.right == None:
			if node.key == self.root.key:
				self.root = None
			elif node.parent.left== p:
				node.parent.left = None
			else:
				node.parent.right = None
		# OneChild Case
		elif node.left == None or node.right == None:
			if node.key == self.root.key:
				if self.root.left != None:
					self.root = self.root.left
					self.root.parent= None
				else:
					self.root = self.root.right
					self.root.parent= None
			elif node.left != None:
				node.left.parent = node.parent
				if node.key < node.parent.key:
					node.parent.left = node.left
				else:
					node.parent.right = node.left
			else:
				node.right.parent = node.parent
				if node.key > node.parent.key:
					node.parent.right = node.right
				else:
					node.parent.left = node.right
		# TwoChild Case
		else:
			if node.key == self.root.key:
				temp = self.root.find_successor()
				self.delete_node(temp)
				node.key = temp.key
			else:
				temp = node.find_successor()
				self.delete_node(node.find_successor())
				goleft = node.left
				goright = node.right
				temp.parent = node.parent
				if node.parent.right == node:
					node.parent.right = temp
				else:
					node.parent.left = temp
				node = temp
				node.left = goleft
				node.right = goright


 
