#
#Polina Volnuhina
#014302388
#4/16/2019
#
#lab 3
#CPE 202-13
#Practising how to stack first-in first-out queues using python lists. 

class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.items=[None]*capacity
        self.capacity = capacity  
        self.num_items = 0 #queue
        self.front = 0
        self.end = 0

    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        if self.num_items == 0:
            return True
        else:
            return False

    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        if self.num_items == self.capacity:  #is full.    #CHECK THIS
            return True
        else:
            return False

    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError'''
        if self.num_items == self.capacity: #is full
            raise IndexError
        else:  #is not full
            self.items[self.end] = item #changed from self.front
            self.end = (self.end+1)%self.capacity  #??????
            self.num_items +=1

    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if self.num_items == 0:
            raise IndexError
        else:
            temp = self.items[self.front]
            self.front = (self.front+1)%self.capacity
            self.num_items -=1
            return temp

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.num_items

