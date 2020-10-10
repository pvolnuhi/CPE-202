import unittest
from binary_search_tree import *

class TestLab4(unittest.TestCase):

	# def test_simple(self):  # one's i need to use

	# 	bst = BinarySearchTree()
	# 	self.assertTrue(bst.is_empty())
	# 	bst.insert(10, 'stuff')
	# 	self.assertTrue(bst.search(10))
	# 	self.assertEqual(bst.root.find_min().key, (10, 'stuff'))
	# 	bst.insert(10, 'other')
	# 	self.assertEqual(bst.find_max(), (10, 'other'))
	# 	self.assertEqual(bst.tree_height(), 0)
	# 	self.assertEqual(bst.inorder_list(), [10])
	# 	self.assertEqual(bst.preorder_list(), [10])
	# 	self.assertTrue(bst.delete(10))
	# 	self.assertEqual(bst.tree_height(), None)

	def test_insert_0(self):
		bst = BinarySearchTree()
		bst.insert(1)
		self.assertEqual(bst.root.key, 1)

	def test_insert_a(self):
		bst = BinarySearchTree()
		bst.insert(None)
		# tree.insert(None)
		self.assertEqual(bst.root.key, None)

	# def test_insert_b(self):
	# 	tree = TreeNode(1, 2, 3)
	# 	tree.insert(1)
	# 	tree.insert(2)
	# 	tree.insert(3)
	# 	self.assertEqual(tree.root.right.key, 3)

	def test_insert_1(self):
		bst = BinarySearchTree()
		bst.insert(1)
		bst.insert(2)
		self.assertEqual(bst.root.right.key, 2)

	def test_insert_2(self):
		bst = BinarySearchTree()
		bst.insert(1)
		bst.insert(2)
		bst.insert(3)
		self.assertEqual(bst.root.right.right.key, 3)

	def test_is_child_0(self):
		bst = BinarySearchTree()
		bst.insert(2)
		bst.insert(1)
		bst.insert(3)
		self.assertTrue(bst.root.right.is_right_child())
		self.assertTrue(bst.root.left.is_left_child())

	def test_find_successor_0(self):
		bst = BinarySearchTree()
		bst.insert(5)
		bst.insert(3)
		bst.insert(7)
		bst.insert(2)
		bst.insert(1)
		bst.insert(1.5)
		bst.insert(6)
		bst.insert(10)
		bst.insert(8)
		bst.insert(9)
		bst.insert(11)
		self.assertEqual(bst.root.right.find_successor().key, 8)

	def test_tree_height(self):
		bst = BinarySearchTree()
		bst.insert(5)
		bst.insert(3)
		bst.insert(7)
		bst.insert(9)
		bst.insert(11)
		self.assertEqual(bst.tree_height(), 4)

	# def test_subtree_height(self):
	# 	bst = BinarySearchTree()
	# 	bst.insert(5)
	# 	bst.insert(3)
	# 	bst.insert(7)
	# 	bst.insert(9)
	# 	bst.insert(11)
	# 	bst.insert(12)
	# 	self.assertEqual(bst.key.subtree_height(), 4)

	# def test_find_successor_1(self):
	# 	tree = BinarySearchTree()
	# 	tree.insert(5)
	# 	tree.insert(3)
	# 	tree.insert(7)
	# 	tree.insert(2)
	# 	tree.insert(1)
	# 	tree.insert(1.5)
	# 	tree.insert(6)
	# 	tree.insert(10)
	# 	tree.insert(8)
	# 	tree.insert(11)
	# 	self.assertEqual(tree.root.right.right.left.find_successor().key, 10)

	# def test_print_tree_0(self):
	# 	tree = BinarySearchTree()
	# 	tree.insert(5)
	# 	tree.insert(3)
	# 	tree.insert(4)
	# 	tree.insert(2)
	# 	tree.insert(1)
	# 	tree.insert(1.5)
	# 	tree.print_tree()
	# 	# Should have output that looks like this "1 1.5 2 3 4 5"

	# def test_inorder_print_tree_0(self):
	# 	tree = BinarySearchTree()
	# 	tree.insert(5)
	# 	tree.insert(3)
	# 	tree.insert(4)
	# 	tree.insert(2)
	# 	tree.insert(1)
	# 	tree.insert(1.5)
	# 	tree.root.left.inorder_print_tree()
		# Should have output that looks like this "1 1.5 2 3 4 5"

	def test_print_levels_0(self):
		bst = BinarySearchTree()
		bst.insert(5)
		bst.insert(3)
		bst.insert(4)
		bst.insert(2)
		bst.insert(1)
		bst.insert(1.5)
		#print(tree.root.print_levels())

	def test_find_0(self):
		bst = BinarySearchTree()
		bst.insert(5)
		bst.insert(4)
		bst.insert(3)
		bst.insert(2)
		bst.insert(1)
		self.assertTrue(bst.search(5))
		self.assertTrue(bst.search(3))
		self.assertFalse(bst.search(7))

	def test_is_empty_0(self):
		bst = BinarySearchTree()
		self.assertTrue(bst.is_empty())

	def test_is_empty_1(self):
		bst = BinarySearchTree()
		bst.insert(1)
		self.assertFalse(bst.is_empty())

	def test_delete_0(self):
		bst = BinarySearchTree()
		bst.insert(1)
		bst.node_delete(1)
		self.assertTrue(bst.is_empty())

	# def test_delete_1(self):
	# 	tree = BinarySearchTree()
	# 	tree.insert(2)
	# 	tree.insert(3)
	# 	tree.insert(1)
	# 	tree.insert(4)
	# 	tree.insert(7)
	# 	tree.insert(6)
	# 	print("TEST DELETE")
	# 	tree.root.inorder_print_tree()
	# 	tree.delete(6)
	# 	tree.delete(3)
	# 	tree.delete(2)
	# 	#self.assertTrue(tree.size, 4)
	# 	#self.assertTrue(tree.root.right.key, 4)
	# 	#self.assertTrue(tree.root.right.right.key, 7)
	# 	self.assertTrue(tree.root.key, 1)
	# 	print("SOLUTION")
	# 	tree.root.inorder_print_tree()

	# def test_delete_2(self):
	# 	tree = BinarySearchTree()
	# 	tree.insert(1)
	# 	tree.insert(2)
	# 	tree.insert(3)
	# 	print("TEST DELETE")
	# 	tree.root.inorder_print_tree()
	# 	tree.delete(1)
	# 	print("SOLUTION")
	# 	tree.root.inorder_print_tree()

	def test_insert_3(self):
		bst = BinarySearchTree()
		bst.insert(2)
		bst.insert(1)
		bst.insert(3)
		self.assertEqual(bst.root.key, 2)
		self.assertEqual(bst.root.parent, None)
		self.assertEqual(bst.root.right.key, 3)
		self.assertEqual(bst.root.right.parent.key, 2)
		self.assertEqual(bst.root.left.key, 1)
		self.assertEqual(bst.root.left.parent.key, 2)

	def test_find_min_0(self):
		bst = BinarySearchTree()
		bst.insert(2)
		bst.insert(1)
		self.assertEqual(bst.root.find_min().key, 1)

	def test_find_max_0(self):
		bst = BinarySearchTree()
		bst.insert(1)
		bst.insert(2)
		bst.insert(3)
		bst.insert(4)
		self.assertEqual(bst.root.find_max().key, 4)		


if __name__ == '__main__': 
	unittest.main()
