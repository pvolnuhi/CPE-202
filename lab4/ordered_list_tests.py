import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        #self.assertEqual(t_list.index(10), 10) #check
        self.assertTrue(t_list.search(10))

        #self.assertFalse(t_list.isEmpty())
        #self.assertTrue(t_list.isEmpty()) #is_empty head and tail are none

        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_search(self):
        t_list = OrderedList()
        t_list.add(1)
        t_list.add(2)
        self.assertTrue(t_list.search(2))

    def test_search_0(self):
        t_list = OrderedList()
        t_list.add(1)
        t_list.add(2)
        self.assertFalse(t_list.search(3))

    def test_search_1(self):
        t_list = OrderedList()
        t_list.add(2)
        t_list.add(5)
        self.assertTrue(t_list.search(5))


    def test_is_empty(self):
        t_list = OrderedList()
        t_lis = OrderedList()
        t_lis.add(10)
        self.assertTrue(t_list.isEmpty())
        self.assertFalse(t_lis.isEmpty())

    def test_remove(self):
        t_list = OrderedList()
        t_list.add(1)
        t_list.add(4)
        t_list.add(2)
        self.assertTrue(t_list.remove(1))
        self.assertEqual(t_list.tail.getData(), 4)
        self.assertEqual(t_list.head.getData(), 2)

    def test_remove_0(self):
        t_list = OrderedList()
        t_list.add(1)
        t_list.add(4)
        t_list.add(2)
        self.assertTrue(t_list.remove(2))
        self.assertEqual(t_list.tail.getData(), 4)
        self.assertEqual(t_list.head.getData(), 1)

    # def test_remove_1(self):
    #     t_list = OrderedList()
    #     t_list.add(1)
    #     t_list.add(2)
    #     t_list.add(3)
    #     t_list.add(4)
    #     self.assertTrue(t_list.remove(4))
    #     self.assertEqual(t_list.tail.getData(), 3)
    #     self.assertEqual(t_list.head.getData(), 1)

    def test_index(self):
        t_list = OrderedList()
        t_list.add(1)
        self.assertEqual(t_list.index(1), 0)

    def test_index_0(self):
        t_list = OrderedList()
        t_list.add(2)
        t_list.add(5)
        t_list.add(3)
        self.assertEqual(t_list.index(5), 2)


    def test_add(self):
        t_list = OrderedList()
        t_list.add(1)
        t_list.add(3)
        t_list.add(2)
        self.assertEqual(t_list.size(), 3)
        self.assertEqual(t_list.tail.getData(), 3)

    def test_add_0(self):
        t_list = OrderedList()
        t_list.add(5)
        t_list.add(7)
        t_list.add(10)
        t_list.add(12)
        t_list.add(2)
        t_list.add(4)
        t_list.add(0)
        self.assertEqual(t_list.size(), 7)
        self.assertEqual(t_list.tail.getData(), 12)
        self.assertEqual(t_list.head.getData(), 0)

    def test_pop(self):
        t_list = OrderedList()
        t_list.add(1)
        t_list.add(5)
        t_list.add(3)
        t_list.add(0)
        self.assertEqual(t_list.pop(2), 3)
        self.assertEqual(t_list.tail.getData(), 5)
        self.assertEqual(t_list.head.getData(), 0)

    # def test_pop_0(self):
    #     t_list = OrderedList()
    #     t_list.add(1)
    #     t_list.add(5)
    #     t_list.add(3)
    #     t_list.add(0)
    #     self.assertEqual(t_list.pop(2), 3)
    #     self.assertEqual(t_list.tail.getData(), 5)
    #     self.assertEqual(t_list.head.getData(), 0)

    def test_pop_0(self):
        t_list = OrderedList()
        t_list.add(1)
        t_list.add(5)
        t_list.add(3)
        t_list.add(0)
        self.assertEqual(t_list.pop(0), 0)
        self.assertEqual(t_list.tail.getData(), 5)
        self.assertEqual(t_list.head.getData(), 1)




if __name__ == '__main__': 
    unittest.main()
