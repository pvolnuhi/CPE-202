#
#Polina Volnuhina
#014302388
#5/30/2019
#
#Assign4
#CPE 202-13
#Hashing data structure and concordance of text


from hash_quad import *
import string

class Concordance:

	def __init__(self, stop_table = 191, concordance_table = 1910000):
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
			stop_words_file.close()

		for line in stop_words_file:
			line = line.strip()
			lower_line = line.lower()
			self.stop_table.insert(lower_line, 0) # file2_sol.txt lower case 
		stop_words_file.close()


	def load_concordance_table(self, filename):
		""" Read words from input text file (filename) and insert them into the concordance hash table 
		(after processing for punctuation, numbers and filtering out words that are in the stop words hash table).
		Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
		Starting size of hash table should be 191: self.concordance_table = HashTable(191)
		If file does not exist, raise FileNotFoundError"""
		try:
			input_file = open(filename, 'r', newline = '')
		except:
			raise FileNotFoundError("filename not found")
			input_file.close()

		line_entry = 0 
		for per_line in input_file:
			line_entry += 1
			per_line = self.concordance_string(per_line) #function that take cares of removes any punctuation, hyphens, numbers, and stop words
			per_line = per_line.split() # seperate by cat, dog, mousse, ...
			for words in per_line:
				self.concordance_table.insert(words, line_entry)
		input_file.close()

	def write_concordance(self, filename): 
		""" Write the concordance entries to the output file(filename)
		See sample output files for format."""
		list_of_keys = self.concordance_table.get_all_keys() 
		list_of_keys.sort() # sorts in ascending order
		output_file = open(filename, 'w', newline = '')
		for k in range(len(list_of_keys)):
			key = list_of_keys[k]
			values = self.concordance_table.get_value(key)
			values.sort()
			for i in range(len(values)):
				values[i] = str(values[i])
			values = ' '.join(values)
			if k < len(list_of_keys) - 1:
				output_file.write(key + ': ' + values + '\n')
			else:
				output_file.write(key + ': ' + values)
				# output_file.close()

		output_file.close()

	def remove_punct(self, txt):
		""" Removes all punctuation in text """
		remove = set(string.punctuation)
		txt = ''.join(x for x in txt if x not in remove) # apostrophe included
		return txt

	def remove_hyphens(self, string): # included in import string module, but need to replace with white space 
		"""Replace all hyphens in a line with spaces."""
		new_string = string.replace('-', ' ')
		return new_string 

	# def remove_apost(self, string): # included in import string module, but need to replace with white space 
	# 	"""Replace all hyphens in a line with spaces."""
	# 	new_string = string.remove("'")
	# 	return new_string

	def remove_digits(self, string):
		"""Return string without any numbers """
		no_digits = []
		for char in string:
			if not char.isdigit():
				no_digits.append(char)
		return ''.join(no_digits) # returns string with just words

	def remove_stop_words(self, string): #
		"""Remove stop words """
		string = string.split()
		new_string = []
		for word in string:
			if self.stop_table.in_table(word) == False: # if word is not in the stop_word table (False), then return it in a new string
				new_string.append(word)
		return ' '.join(new_string)

	def concordance_string(self, string):
		"""Removes stop words, punctuation, and numbers."""
		valid_words = string.lower() # drops to lower case letters

		# valid_word = self.remove_hyphens(valid_words).remove_digits(valid_words).remove_punct(valid_words).remove_stop_words(valid_words)
		valid_words = self.remove_hyphens(valid_words) 
		valid_words = self.remove_punct(valid_words)
		valid_words = self.remove_digits(valid_words)
		valid_words = self.remove_stop_words(valid_words)
		return valid_words










