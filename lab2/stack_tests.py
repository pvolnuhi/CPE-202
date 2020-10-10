#
#Polina Volnuhina
#014302388
#4/16/2019
#
#lab 2
#CPE 202-13
#Testing both the stacked array and stacked linked.  

import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
from stack_array import Stack
# from stack_linked import Stack

class TestLab2(unittest.TestCase):
	def test_stack_array(self):
		stack = Stack(5)
		stack.push(0) #pushes nothing 
		self.assertFalse(stack.is_empty()) #not empty
		self.assertFalse(stack.is_full()) #not full
		self.assertEqual(stack.size(),1) #size refers to len() of list

	def test1_stack_array(self):
		stack = Stack(5)
		self.assertTrue(stack.is_empty()) #Test empty stack
		stack.push(1) 
		self.assertFalse(stack.is_empty()) #Test empty stack with element inside stack
		self.assertFalse(stack.is_full()) #Test if stack is full
		self.assertEqual(stack.size(),1)
		
	def test2_stack_array(self):
		stack = Stack(5)
		self.assertTrue(stack.is_empty()) #Test empty stack
		stack.push(1) 
		self.assertFalse(stack.is_empty()) #Test empty stack with element inside stack
		self.assertFalse(stack.is_full()) #Test if stack is full
		stack.push(2)
		self.assertEqual(stack.size(),2) #Test the number of items
		stack.push(3)
		stack.push(4)
		stack.push(5)
		with self.assertRaises(IndexError): #Test if error is raised when going passed capacity
			stack.push(6) 
		self.assertEqual(stack.size(),5) 
		self.assertTrue(stack.is_full()) #Test when stack is full will confirm
		self.assertEqual(stack.pop(), 5) #Test return of top of stack and redirects top
		self.assertEqual(stack.size(),4) #Test to check the new size of stack
		self.assertEqual(stack.peek(),4) #Test new top of stack
	
	def test4_stack_array(self):
		stack = Stack(0)
		with self.assertRaises(IndexError): #Test if error is raised when stack is empty 
			stack.peek() 
		
	def test3_stack_array(self):
		stack = Stack(3)
		with self.assertRaises(IndexError):
			stack.pop() #Test to pop an empty stack
		self.assertEqual(stack.size(),0) #Test to return size of empty stack
		stack = Stack(3)
		with self.assertRaises(IndexError):
			stack.pop() #Test to pop an empty stack
		self.assertEqual(stack.size(),0) #Test to return size of empty stack

	def test_stack_linked(self):
		stack_node = Stack(3) #Create Stacked Linked List
		with self.assertRaises(IndexError): #Tests Error, cannot pop an empty stack
			stack_node.pop()
		self.assertTrue(stack_node.is_empty()) #Tests if the stack is empty
		self.assertEqual(stack_node.size(), 0) #Tests if the size of the stack is 0
		stack_node.push(12) #Push first value to the stack
		self.assertFalse(stack_node.is_empty()) #Tests when something is pushed if the stack is empty
		self.assertEqual(stack_node.size(), 1)#Tests size function
		self.assertEqual(stack_node.peek(), 12)#Tests peek function
		self.assertEqual(stack_node.pop(), 12) #Tests pop function

		self.assertFalse(stack_node.is_full()) #Tests if the Stack is full
		stack_node.push(15)
		stack_node.push(17)
		self.assertEqual(stack_node.size(), 2) #Tests the size after pushing 2 items
		self.assertEqual(stack_node.peek(),17) #Tests peek function
		self.assertEqual(stack_node.pop(),17) #Tests pop function 
		self.assertEqual(stack_node.peek(),15)#Tests peek to see if once the top is redirected if it returns the new top
		stack_node.push(12)
		stack_node.push(21)
		self.assertEqual(stack_node.size(), 3) 
		self.assertTrue(stack_node.is_full())#Tests when the Stack is full 
		with self.assertRaises(IndexError): #Tests pushing additional item after it is full
			stack_node.push(12)	

	def test_stack_linked1(self):
		stack_node = Stack(0)
		with self.assertRaises(IndexError):
			stack_node.peek()



if __name__ == '__main__': 
	unittest.main()
