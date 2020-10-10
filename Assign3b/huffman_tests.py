#
#Polina Volnuhina
#014302388
#5/19/2019
#
#Assign3b 
#CPE 202-13
#Test cases for HuffmanNode contruction and traversal plus decoding.

import unittest 
import filecmp
import subprocess
from huffman import *

class TestList(unittest.TestCase): 
	def test_cnt_freq0(self):
		freqlist = cnt_freq("file2.txt")
		anslist = [2, 4, 8, 16, 0, 2, 0] 
		self.assertListEqual(freqlist[97:104], anslist)

	def test_cnt_freq1(self):
		freqlist = cnt_freq("file1.txt")
		anslist = [2, 4, 3, 2, 1]
		list2 = [freqlist[32]]
		self.assertEqual(list2 + freqlist[97:101], anslist)

	def test_cnt_freq2(self): #with spaces
		freqlist = cnt_freq("file3.txt")
		anslist = [5, 9]
		self.assertEqual(freqlist[32:34], anslist)

	def test_create_huff_tree(self):
		freqlist = cnt_freq("file2.txt")
		hufftree = create_huff_tree(freqlist)
		self.assertEqual(hufftree.freq, 32)
		self.assertEqual(hufftree.char, 97)
		left = hufftree.left
		self.assertEqual(left.freq, 16)
		self.assertEqual(left.char, 97)
		right = hufftree.right
		self.assertEqual(right.freq, 16)
		self.assertEqual(right.char, 100)
	
	def test_create_header(self): 
		freqlist = cnt_freq("file2.txt")
		self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

	def test_parse_header(self): 
		freqlist = cnt_freq("file4.txt")
		header_string = create_header(freqlist)
		string_to_list = parse_header(header_string)
		self.assertEqual(string_to_list[97:100], [3, 4, 2])

	def test_create_code(self):
		freqlist = cnt_freq("file2.txt")
		hufftree = create_huff_tree(freqlist)
		codes = create_code(hufftree)
		self.assertEqual(codes[ord('d')], '1')
		self.assertEqual(codes[ord('a')], '0000')
		self.assertEqual(codes[ord('f')], '0001')

	def test_01_textfile(self): 
		huffman_encode("multiline.txt", "multiline_out.txt")
		# capture errors by running 'diff' on your encoded file with a *known* solution file
		err = subprocess.call("diff -wb multiline_out.txt multiline_soln.txt", shell = True)
		self.assertEqual(err, 0)

	def test_02_textfile(self): 
		huffman_encode("declaration.txt", "declaration_out.txt")
		# capture errors by running 'diff' on your encoded file with a *known* solution file
		err = subprocess.call("diff -wb declaration_out.txt declaration_soln.txt", shell = True)
		self.assertEqual(err, 0)

	def test_03_textfile(self): 
		huffman_decode( "multiline_out.txt", "multiline_decoded.txt")
		# capture errors by running 'diff' on your decoded file with a *known* solution file
		err = subprocess.call("diff -wb multiline.txt multiline_decoded.txt", shell = True)
		self.assertEqual(err, 0)

	def test_04_textfile(self): 
		huffman_decode( "declaration_out.txt", "declaration_decoded.txt")
		# capture errors by running 'diff' on your decoded file with a *known* solution file
		err = subprocess.call("diff -wb declaration.txt declaration_decoded.txt", shell = True)
		self.assertEqual(err, 0)

if __name__ == '__main__': 
   unittest.main()
