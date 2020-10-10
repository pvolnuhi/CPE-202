#
#Polina Volnuhina
#014302388
#5/13/2019
#
#Assign3a 
#CPE 202-13
#Test cases for HuffmanNode contruction and traversal.

import unittest
import filecmp
import subprocess
from huffman import *

class TestList(unittest.TestCase): #how to test with spaces in one file with other words?
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


if __name__ == '__main__': 
   unittest.main()
