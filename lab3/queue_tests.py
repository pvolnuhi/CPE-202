import unittest
from queue_array import Queue
from queue_linked import LinkedQueue

class TestLab1(unittest.TestCase):
	def test_queue_array(self):
		'''Trivial test to ensure method names and parameters are correct'''
		q = Queue(4)
		self.assertTrue(q.is_empty())
		with self.assertRaises(IndexError): #Checks if raises IndexError when dequeuing a Queue
			q.dequeue()
		q.enqueue(1)
		self.assertEqual(q.dequeue(),1) #Checks dequeue 
		q.enqueue(1)
		self.assertEqual(q.size(),1) #Checks the number of items in Queue
		self.assertEqual(q.items,[1,1,None,None]) #Checks if enqueue worked #CHECK
		self.assertFalse(q.is_empty())
		self.assertFalse(q.is_full()) #not full yet 
		
		q.enqueue(2)
		self.assertEqual(q.end, 3) #Checks the end #,3
		self.assertEqual(q.size(),2) #Checks the number of items in Queue
		q.enqueue(3)
		q.enqueue(4)
		with self.assertRaises(IndexError): #Checks if raises IndexError when enqueuing a full Queue
			q.enqueue(5)
		self.assertTrue(q.is_full()) #Checks is_full method on a Queue when all slots are occupied by elements
		self.assertEqual(q.size(),4) #Checks the number of items in Queue
		q.dequeue()
		self.assertEqual(q.front, 2) #Checks front on Queue after dequeue called
		self.assertEqual(q.size(),3) #Checks the number of items in Queue after calling dequeue
		
	def test_queue_linked(self):
		'''Trivial test to ensure method names and parameters are correct'''
		q = LinkedQueue(4)
		self.assertTrue(q.is_empty())
		with self.assertRaises(IndexError): #Checks if raises IndexError when dequeuing a Queue
			q.dequeue()
		q.enqueue(1)
		self.assertEqual(q.dequeue(),1) #Checks dequeue 
		q.enqueue(1)
		self.assertEqual(q.size(),1) #Checks the number of items in Queue
		self.assertFalse(q.is_empty())
		self.assertFalse(q.is_full()) #not full yet 
		
		q.enqueue(2)
		self.assertEqual(q.end.data, 2) #Checks the end #,3. .data
		self.assertEqual(q.size(),2) #Checks the number of items in Queue
		q.enqueue(3)
		q.enqueue(4)
		with self.assertRaises(IndexError): #Checks if raises IndexError when enqueuing a full Queue
			q.enqueue(5)
		self.assertTrue(q.is_full()) #Checks is_full method on a Queue when all slots are occupied by elements
		self.assertEqual(q.size(),4) #Checks the number of items in Queue
		q.dequeue()
		self.assertEqual(q.front.data, 2) #Checks front on Queue after dequeue called
		self.assertEqual(q.size(),3) #Checks the number of items in Queue after calling dequeue



		#new test cases
		

if __name__ == '__main__': 
	unittest.main()
