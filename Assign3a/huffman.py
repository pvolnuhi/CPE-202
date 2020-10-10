#
#Polina Volnuhina
#014302388
#5/13/2019
#
#Assign3a 
#CPE 202-13
#Test cases for HuffmanNode contruction and traversal.

class HuffmanNode:
	def __init__(self, char, freq, left, right):
		# stored as an integer - the ASCII character code value
		self.char = ord(char)
		self.freq = freq   # the freqency associated with the node
		self.left = left   # Huffman tree (node) to the left
		self.right = right  # Huffman tree (node) to the right

	def set_left(self, node):
		self.left = node

	def set_right(self, node):
		self.right = node

	def is_leaf(self):
		""" leaf node """
		return self.left == None and self.right == None

def comes_before(a, b):
	"""Returns True if tree rooted at node a comes before tree rooted at node b, False otherwise"""
	if a.freq == b.freq:
		return a.char < b.char
	elif a.freq < b.freq:
		return True
	else:
		return False


def combine(a, b):
	"""Creates and returns a new Huffman node with children a and b, with the "lesser node" on the left
	The new node's frequency value will be the sum of the a and b frequencies
	The new node's char value will be the lesser of the a and b char ASCII values"""
	new_node_char = None
	if a.char < b.char:
		new_node_char = chr(a.char)
	else:
		new_node_char = chr(b.char)
	if comes_before(a,b):
		left = a
		right = b
	else:
		left = b
		right = a
	node_freq = a.freq + b.freq
	new_node = HuffmanNode(new_node_char, node_freq, left, right)
	return new_node


def cnt_freq(filename):  # works!
	"""Opens a text file with a given file name (passed as a string) and counts the
	frequency of occurrences of all the characters within that file"""
	freq_counter = [0] * 256  # size 256 all the zeros until freq of letter is added to index using ascii values

	try:
		# opens and reads file dont need to split because space is included
		txtfile = open(filename, 'r')
	except:
		raise FileNotFoundError('filename not found')

	for line in txtfile:
		for charachter in line:
			freq_counter[ord(charachter)] += 1
	txtfile.close()  # close file
	return freq_counter  # returns list of frequencies

def sort_list(huffman_nodes_list):
	""" Takes in huffman nodes, and sorts based on comes_before call """
	huffman_nodes_list.sort(key=lambda node: (node.freq, node.char), reverse=False)
	return huffman_nodes_list

def create_huff_tree(char_freq):
	"""Create a Huffman tree for characters with non-zero frequency
	Returns the root node of the Huffman tree"""
	leaf_nodes = []
	for i in range(len(char_freq)):
		if char_freq[i] != 0:
			leaf_nodes.append(HuffmanNode(chr(i), char_freq[i], None, None))
	sorted_nodes = sort_list(leaf_nodes)

	while len(sorted_nodes) > 1:
		min1 = sorted_nodes.pop(0)
		min2 = sorted_nodes.pop(0)
		huffman_tree = combine(min1, min2)
		sorted_nodes.append(huffman_tree)
		# goes through again with different sorted list
		sorted_nodes = sort_list(sorted_nodes)
		# sorted_nodes.append(new_leaf_node)  #add new node to sorted list
	return sorted_nodes[0]


def create_code(root_node):  # passes in Huffmantree
	"""Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation
	as the index into the arrary, with the resulting Huffman code for that character stored at that location"""
	code = ''
	list_of_strings = [''] * 256
	traverse_huffman_tree(root_node.left, code + '0', list_of_strings)
	traverse_huffman_tree(root_node.right, code + '1', list_of_strings)
	return list_of_strings


def traverse_huffman_tree(node, code, list_of_strings):
	if node.is_leaf():
		list_of_strings[node.char] = code
	else:
		traverse_huffman_tree(node.left, code + '0', list_of_strings)
		traverse_huffman_tree(node.right, code + '1', list_of_strings)


def create_header(list_of_freqs):  # HELP
	"""Input is the list of frequencies. Creates and returns a header for the output file
	Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” """
	header = ''  # returns a string
	for i in range(len(list_of_freqs)):
		if list_of_freqs[i] != 0:
			if len(header) > 0:
				header += " "
			header += str(i) + " " + str(list_of_freqs[i])
	return header


def huffman_encode(in_file, out_file):  # HELP
	"""Takes inout file name and output file name as parameters
	Uses the Huffman coding process on the text from the input file and writes encoded text to output file
	Take note of special cases - empty file and file with only one unique character"""
	#does txtfile exist 
	try:
		txtfile = open(in_file, 'r')
	except:
		raise FileNotFoundError("filename not found")
	# Checks if file empty
	if txtfile.readline() == '':
		output = open(out_file, 'w')
		output.close()
	else:
		# Checks for one character in txtfile
		txtfile.close()
		freq_in_file = cnt_freq(in_file)
		count = 0
		index = None
		freq = None
		for i in range(len(freq_in_file)):
			if freq_in_file[i] != 0:
				index = i
				freq = freq_in_file[i]
				count += 1
		if count == 1:
			output_file = open(out_file, 'w', newline = '')
			output_file.write(str(index) + ' ' + str(freq))
			output_file.close()
		else:
			huff_tree_root = create_huff_tree(freq_in_file) # With multiple characters and file is not empty build huffman code
			code_list = create_code(huff_tree_root)
			infile = open(in_file, 'r', newline = '')
			outfile = open(out_file, 'w', newline = '')
			# Write header
			outfile.write(create_header(freq_in_file) + "\n")
			# Write encoded body
			for line in infile:
				for character in line:
					outfile.write(code_list[ord(character)])
			infile.close()
			outfile.close()
