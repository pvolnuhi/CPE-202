from hash_quad import HashTable
import string

class Concordance:

	def __init__(self, stop_table = 191, concordance_table = 191):
		self.stop_table = HashTable(stop_table)               # hash table for stop words
		self.concordance_table = HashTable(concordance_table) # hash table for concordance

	def load_stop_table(self, filename):
		""" Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
		Starting size of hash table should be 191: self.stop_table = HashTable(191)
		If file does not exist, raise FileNotFoundError"""
		try:
			stop_words_file = open(filename, 'r', newline = '')
		except:
			raise FileNotFoundError("filename not found")
		for line in stop_words_file:
			line = line.strip()
			self.stop_table.insert(line.lower(), 0) # file2.txt makes them lower case 
		stop_words_file.close()


	def load_concordance_table(self, filename):
		""" Read words from input text file (filename) and insert them into the concordance hash table 
		(after processing for punctuation, numbers and filtering out words that are in the stop words hash table).
		Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
		Starting size of hash table should be 191: self.concordance_table = HashTable(191)
		If file does not exist, raise FileNotFoundError"""
		try:
			stop_words_file = open(filename, 'r', newline = '')
		except:
			raise FileNotFoundError("filename not found")

		line_number = 0 # what is count in this case????
		for line in stop_words_file:
			line_number += 1
			line = self.concordance_string(line) #functions that take cares of removes any punctuation, hyphens, numbers, and stop words
			line = line.split()
			for word in line:
				self.concordance_table.insert(word, line_number)
		stop_words_file.close()

	def write_concordance(self, filename): # HELP
		""" Write the concordance entries to the output file(filename)
		See sample output files for format."""

		key_list = self.concordance_table.get_all_keys() 
		key_list.sort() # sorts in alphabetical order 
		output_file = open(filename, 'w', newline = '')
		for key in key_list:
			values = self.concordance_table.get_value(key)
			values.sort()
			for i in range(len(values)):
				values[i] = str(values[i])
			values = ' '.join(values)
			output_file.write(key + ': ' + values + '\n')
		output_file.close()

	def remove_punct(self, line):
		""" Removes punctuation in one line """
		# for char in line:
		#     if char in string.punctuation:
		remove = set(string.punctuation)
		line = ''.join(x for x in line if x not in remove) # apostrophe included
		return line

	def remove_hyphens(self, string): # included in import string module, but need to replace with white space 
		"""Replace all hyphens in a line with spaces."""
		new_string = string.replace('-', ' ')
		return new_string 

	def remove_digits(self, string):
		"""Return string without any numbers."""
		no_digits = []
		for char in string:
			if not char.isdigit():
				no_digits.append(char)
		return ''.join(no_digits)

	def remove_stop_words(self, string): # HELP 
	    #not sure if works correctly... directly goes from quad_hash method call in_table...
		"""Remove all stop words from a string in current line."""
		string = string.split()
		new_string = []
		for word in string:
			if self.stop_table.in_table(word) != True: # if word is not in the stop_word table (true), then return it in a new string
				new_string.append(word)
		return ' '.join(new_string)

	def concordance_string(self, line):
		"""Clean up a line so that it only includes VALID words for concordance."""
		new_line = line.strip()
		new_line = new_line.lower()
		new_line = self.remove_hyphens(new_line)
		new_line = self.remove_punct(new_line)
		new_line = self.remove_digits(new_line)
		new_line = self.remove_stop_words(new_line)
		return new_line










