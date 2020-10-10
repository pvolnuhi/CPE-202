#
#Polina Volnuhina
#014302388
#5/10/2019
#
#Assign5
#CPE 202-13
#Graphs and Bipartite distinction through BFS and DFS search.

import os  


from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search

class Vertex:
	'''Add additional helper methods if necessary.'''
	def __init__(self, key):
		self.id = key          
		self.neighbor = {}
		self.processed = False # True = checked this vertex already  
		self.color = -1 # color isn't distinguished yet. Biparte uses 0 and 1
	
	def reset(self):
		self.processed = False
		self.color = -1

	'''Checked vertex already'''
	def process(self, color = -1):
		self.processed = True
		self.color = color 


	def is_processed(self):
		return self.processed 

	def get_color(self):
		return self.color
	
	'''Add up neighboring vertices if they exist'''
	def add_neighbor(self, buddy):
		if self.neighbor.get(buddy.id, None) is None:
			self.neighbor[buddy.id] = buddy
	
	"""Returns list of connected vertices"""
	def get_neighbors(self):
		values = []
		for v in self.neighbor.values():
			values.append(v)
		return sorted(values, key=lambda x: x.id) # goes through values, sorts by ID

	'''Returns the location/ID of vertex'''
	def get_id(self):
		return self.id


class Graph:
	'''Add additional helper methods if necessary.'''

	def __init__(self, filename):
		'''reads in the specification of a graph and creates a graph using an adjacency list representation.  
		You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
		represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
		in the input file should appear on the adjacency list of each vertex of the two vertices associated 
		with the edge.'''
		self.num_vert = 0 # don't need it i think 
		self.vertices = {}
		self.load_data(filename)

	def reset(self):
		for k in self.vertices.keys():
			self.vertices[k].reset()

	def load_data(self, filename):
		try:
			graph_file = open(filename, 'r', newline = '')
		except:
			raise FileNotFoundError("filename not found")


		for line in graph_file:
			line = line.strip()
			edges = line.split() # white space as seperator 
			if len(edges) != 2: # assume pair of vertices per edge 
				raise ValueError("Wrong file format")
			self.add_vertex(edges[0])
			self.add_vertex(edges[1])
			self.add_edge(edges[0], edges[1])
		graph_file.close()

	def add_edge(self, v1, v2): # modifies adjacent_to 
		'''v1 and v2 are vertex id's. As this is an undirected graph, add an 
		edge from v1 to v2 and an edge from v2 to v1.  You can assume that
		v1 and v2 are already in the graph'''
		vert1 = self.get_vertex(v1)
		vert2 = self.get_vertex(v2)
		vert1.add_neighbor(vert2)
		vert2.add_neighbor(vert1)

	def add_vertex(self, key):
		'''Add vertex to graph, only if the vertex is not already in the graph'''
		if key not in self.vertices.keys():
			v = Vertex(key)
			self.vertices[key] = v

	def get_vertex(self, key): # check over
		'''return the Vertex object associated with the id. If id is not in the graph, then None'''
		# if key != self.vertices.keys():
		# 	return None
		return self.vertices.get(key, None)

	def size(self):
		vert_length = len(self.vertices)
		return vert_length

	def is_empty(self):
		return self.size() == 0

	def get_vertices(self):
		'''Returns a list of id's representing the vertices in the graph, in ascending order'''
		sorted_vert = sorted(self.vertices.keys())
		return sorted_vert

	def next_unprocessed(self):
		'''Return a list of id's representing the vertices in the graph, in ascending order'''
		for k in self.vertices.keys():
			if not self.vertices[k].is_processed():
				return self.vertices[k]
		return None

	def conn_components(self): 
		'''Returns a list of lists.  For example, if there are three connected components 
		then you will return a list of three lists.  Each sub list will contain the 
		vertices (in ascending order) in the connected component represented by that list.
		The overall list will also be in ascending order based on the first item of each sublist.
		This method MUST use Depth First Search logic!'''
		components = []
		count = 0
		while count < self.size():
			component = []
			stack = Stack(self.size())
			v = self.next_unprocessed()
			v.process()
			stack.push(v)
			count += 1
			while not stack.is_empty():
				v = stack.pop()
				component.append(v.id)
				neighbors = v.get_neighbors()
				for v in neighbors:
					if not v.is_processed(): # if didn't check vertex 
						v.process()
						stack.push(v)
						count += 1
			component.sort()
			components.append(component)
		#reset graph
		self.reset() # calls back to __init__ functions
		return sorted(components, key = lambda x: x[0])


	def is_bipartite(self):
		'''Returns True if the graph is bicolorable and False otherwise.
		This method MUST use Breadth First Search logic!'''
		count = 0
		while count < self.size():
			queue = Queue(self.size())
			v = self.next_unprocessed()
			queue.enqueue(v)
			count += 1
			while not queue.is_empty(): # 
				v = queue.dequeue() 
				neighbors = v.get_neighbors()
				color = self.get_color_not_in(neighbors)
				if color == None:
					return False
				else:
					v.process(color)
					count += 1
				for v in neighbors:
					if not v.is_processed():
						queue.enqueue(v)
		# reset all after processing
		self.reset()
		return True 

	def get_color_not_in(self, vertex_list):
		'''Returns suggested color for a vertex, either 0 or 1, checking it's
		neighboring color or None if color can't be assigned'''
		color = 0
		for v in vertex_list:
			if v.get_color() == color: 
				#try color = 1
				color = -1
				break
		if color == 0:
			# means color = 0 works for us 
			return color 
		# color = 0 failed, let's try color = 1
		color = 1
		for v in vertex_list:
			if v.get_color() == color:
				# not bipartite graph
				return None
		# returns color = 1
		return color 


















