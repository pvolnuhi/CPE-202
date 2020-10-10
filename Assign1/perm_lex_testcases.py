import unittest
import perm_lex

class TestAssign1(unittest.TestCase):

	def test_perm_gen_lex(self): #checks emtpy string
		self.assertEqual(perm_lex.perm_gen_lex([]),[])

	def test_perm_gen_lex1(self): #checks when len(string) is 1
		self.assertEqual(perm_lex.perm_gen_lex('a'),['a'])

	def test_perm_gen_lex2(self): #checks when len(string) is 2.   
		self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab', 'ba'])

	def test_perm_gen_lex3(self): #checks when len(string) is greater than 2.    
		self.assertEqual(perm_lex.perm_gen_lex('abc'),['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

if __name__ == "__main__":
        unittest.main()	



