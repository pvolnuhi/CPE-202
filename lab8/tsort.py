#
#Polina Volnuhina
#014302388
#5/05/2019
#
#lab 8
#CPE 202-13
#Practising tsort algorithm.


from sys import argv
from stack_array import *


class Vertex:
	
	def __init__(self, key, order, in_degree = 0):
		self.id = key
		self.order = order
		self.in_degree = in_degree           
		self.neighbor = {}
	
	def add_nearby(self, buddy):
		"""Add nearby vertices """
		if self.neighbor.get(buddy.id, None) is None:
			self.neighbor[buddy.id] = buddy
			buddy.increment_in_degree()

	def get_connections(self):
		"""Returns list of connected vertices """
		values = []
		for v in self.neighbor.values():
			values.append(v)
		return sorted(values, key=lambda x: x.order)

	# def get_id(self):
	# 	"""Returns the location/ID of vertex"""
	# 	return self.id

	def get_in_degree(self):
		"""Returns the in degree of the vertex - number incoming edges"""
		return self.in_degree
	
	def increment_in_degree(self):
		self.in_degree += 1
	
	def decrement_in_degree (self):
		self.in_degree -= 1

	def decrement_all (self):
		for n in self.neighbor.values():
			n.decrement_in_degree()

	# def get_order(self):
	# 	return self.order

def get_zero_in_sorted(graph_map):
		to_be_sorted = []
		for v in graph_map.values():
			if v.get_in_degree() == 0:
				to_be_sorted.append(v)
		
		for x in to_be_sorted:
			del graph_map[x.id] # graph_map[x.id] = None 

		if to_be_sorted != []:
			return sorted(to_be_sorted, key=lambda x: x.order)
		else:
			return []

def tsort(vertices):
	'''
	* Performs a topological sort of the specified directed acyclic graph.  The
	* graph is given as a list of vertices where each pair of vertices represents
	* an edge in the graph.  The resulting string return value will be formatted
	* identically to the Unix utility {@code tsort}.  That is, one vertex per
	* line in topologically sorted order.
	*
	* Raises a ValueError if:
	*   - vertices is emtpy with the message "input contains no edges"
	*   - vertices has an odd number of vertices (incomplete pair) with the
	*     message "input contains an odd number of tokens"
	*   - the graph contains a cycle (isn't acyclic) with the message 
	*     "input contains a cycle"'''
	
	sorted_list = [] # our sorted topologically sorted list of vertices
	stack = Stack(len(vertices)) # stack where we keep verices with 0 in degrees
	graph_map = {} # key - vertice id, value - vertice itself

	if vertices == []:
		raise ValueError("input contains no edges")
	if len(vertices) % 2 != 0:
		raise ValueError("input contains an odd number of tokens")

	order = 0
	for i in range (0, len(vertices) -1, 2):
		# vertices[i] and vertices[i+1]
		v1 = graph_map.get(vertices[i], None)
		v2 = graph_map.get(vertices[i+1], None)
		if v1 is None:
			v1 = Vertex(vertices[i], order)
			order +=1
		if v2 is None:
			v2 = Vertex(vertices[i+1], order)
			order +=1
		v1.add_nearby(v2)
		# put them back into graph_map
		graph_map[v1.id] = v1
		graph_map[v2.id] = v2
	
	llist = get_zero_in_sorted(graph_map)
	if llist == []:
		raise ValueError("input contains a cycle")
	stack.push_all(llist)

	while not stack.is_empty():
		v = stack.pop()
		# decrement in degrees of all outgoing connections
		v.decrement_all()
		outs = v.get_connections()
		sorted_list.append(v.id)
		# check if direct connection vertices has 0 in degree
		for e in outs:
			if e.in_degree == 0:
				del graph_map[e.id]
				stack.push(e)
	if len(graph_map) > 0:
		raise ValueError("input contains a cycle")
	else:
		return "\n".join(sorted_list)

# def main():
#     '''Entry point for the tsort utility allowing the user to specify
#        a file containing the edge of the DAG'''
#     if len(argv) != 2:
#         print("Usage: python3 tsort.py <filename>")
#         exit()
#     try:
#         f = open(argv[1], 'r')
#     except FileNotFoundError as e:
#         print(argv[1], 'could not be found or opened')
#         exit()
	
#     vertices = []
#     for line in f:
#         vertices += line.split()
	   
#     try:
#         result = tsort(vertices)
#         print(result)
#     except Exception as e:
#         print(e)
	
# if __name__ == '__main__': 
#     main()
