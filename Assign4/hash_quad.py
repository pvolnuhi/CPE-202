#
#Polina Volnuhina
#014302388
#5/30/2019
#
#Assign4
#CPE 202-13
#Hashing data strcuture and concordance of text.


class HashTable:

	def __init__(self, table_size = 191):   # can add additional attributes
		self.table_size = table_size        # initial table size = 191
		self.hash_table = [None]*self.table_size # hash table
		self.num_items = 0                  # empty hash table

	def insert(self, key, value):
		""" Inserts an entry into the hash table (using Horner hash function to determine index, 
		and quadratic probing to resolve collisions).
		The key is a string (a word) to be entered, and value is the line number that the word appears on. 
		If the key is not already in the table, then the key is inserted, and the value is used as the first 
		line number in the list of line numbers. If the key is in the table, then the value is appended to that 
		key’s list of line numbers. If value is not used for a particular hash table (e.g. the stop words hash table),
		can use the default of 0 for value and just call the insert function with the key.
		If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""

		success = False
		start_index = self.horner_hash(key)
		for i in range(self.table_size):
			index = (start_index + i * i) % self.table_size
			if self.hash_table[index] == None:
				self.hash_table[index] = (key, [value])
				self.num_items += 1
				if self.get_load_factor() < 0.5:
					return
				else:
					success = True
					break
			elif self.hash_table[index][0] == key: 
				if value not in self.hash_table[index][1]:
					self.hash_table[index][1].append(value)
					self.num_items += 1
					if self.get_load_factor() < 0.5:
						return
					else:
						success = True
						break
				else:
					success = True
					break
		# After insertion is complete:
		if self.get_load_factor() > 0.5:
			self.rehash()
		if success == False:
			# try one more time into rehashed table
			return self.insert(key, value)

	def horner_hash(self, string):  
		""" Compute and return an integer from 0 to the (size of the hash table) - 1
		Compute the hash value by using Horner’s rule, as described in project specification."""
		# if len(string) < 8:
		# 	x = len(string)
		# else:
		# 	x = 8 
		hash_val = 0
		x = len(string)
		for i in range(0, x):
			hash_val = ord(string[i]) + 31 * hash_val #**(x- 1- i)
		return hash_val % self.table_size 

	def rehash(self): 
		""" Rehash once no more space is available using Quadratic Probing """
		old_hash = self.hash_table
		self.table_size = (self.table_size * 2 + 1)
		self.hash_table = [None] * self.table_size
		self.num_items = 0
		for item in old_hash:
			if item is not None:
				for index in item[1]:
					self.insert(item[0], index)

	def in_table(self, key): # could be the error here, iterating through the hash table rather than using the hash function to find the keys, or removing duplicates 
		""" Returns True if key is in an entry of the hash table, False otherwise."""
		start_index = self.horner_hash(key)
		for i in range(self.table_size):
			index = (start_index + i*i) % self.table_size
			if self.hash_table[index] is None:
				return False
			elif self.hash_table[index][0] == key:
				return True
		return False 

	def get_index(self, key): 
		""" Returns the index of the hash table entry containing the provided key. 
		If there is not an entry with the provided key, returns None."""
		start_index = self.horner_hash(key)
		for i in range(self.table_size):
			index = (start_index + i*i) % self.table_size
			if self.hash_table[index] is None:
				return None
			elif self.hash_table[index][0] == key:
				return index
		return None 


	def get_all_keys(self):
		""" Returns a Python list of all keys in the hash table."""
		list_of_keys = []
		for val in self.hash_table:
			if val is not None:
				list_of_keys.append(val[0])
		return list_of_keys

	def get_value(self, key):
		""" Returns the value (list of line numbers) associated with the key. 
		If key is not in hash table, returns None."""
		list_line_nums = self.get_index(key)
		if list_line_nums is None:
			return None
		else:
			return self.hash_table[list_line_nums][1]

	def get_num_items(self):
		""" Returns the number of entries (words) in the table."""
		return self.num_items

	def get_table_size(self):
		""" Returns the size of the hash table."""
		return self.table_size

	def get_load_factor(self):
		""" Returns the load factor of the hash table (entries / table_size)."""
		load_factor =  self.num_items / self.table_size 
		return load_factor 

	# def dump(self):
	# 	out = open("dump_table.txt", "w")
	# 	for e in self.hash_table:
	# 		if e is not None:
	# 			out.write(str(e)+"\n")
	# 	out.close()
