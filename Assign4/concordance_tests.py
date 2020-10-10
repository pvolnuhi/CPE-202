#
#Polina Volnuhina
#014302388
#5/30/2019
#
#Assign4
#CPE 202-13
#Hashing data strcuture and concordance of text.

import unittest
import filecmp
from concordance import *

class TestList(unittest.TestCase):

	def test_01(self):
			conc = Concordance()
			conc.load_stop_table("stop_words.txt")
			conc.load_concordance_table("file1.txt")
			conc.write_concordance("file1_con.txt")
			self.assertTrue(filecmp.cmp("file1_con.txt", "file1_sol.txt"))

	def test_02(self):
			conc = Concordance()
			conc.load_stop_table("stop_words.txt")
			conc.load_concordance_table("file2.txt")
			conc.write_concordance("file2_con.txt")
			self.assertTrue(filecmp.cmp("file2_con.txt", "file2_sol.txt"))

	def test_03(self):
			conc = Concordance()
			conc.load_stop_table("stop_words.txt")
			conc.load_concordance_table("declaration.txt")
			conc.write_concordance("declaration_con.txt")
			self.assertTrue(filecmp.cmp("declaration_con.txt", "declaration_sol.txt"))

	# def test_04(self):
	# 		conc = Concordance()
	# 		conc.load_stop_table("stop_words.txt")
	# 		conc.load_concordance_table("War_And_Peace.txt")
	# 		conc.write_concordance("War_And_Peace_con.txt")
			# self.assertTrue(filecmp.cmp("War_And_Peace.txt", "dictionary_a-c_sol.txt"))

if __name__ == '__main__':
	 unittest.main()
