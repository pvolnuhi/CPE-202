#
#Polina Volnuhina
#014302388
#5/10/2019
#
#Assign5
#CPE 202-13
#Tests for Graphs and Bipartite distinction through BFS and DFS search.

import unittest
from graph import *

class TestList(unittest.TestCase):

	def test_01(self):
		g = Graph('test1.txt')
		self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
		self.assertTrue(g.is_bipartite())

	def test_02(self):
		g = Graph('test2.txt')
		self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
		self.assertFalse(g.is_bipartite())

	def test_add_vertex(self):
		g1 = Graph('test1.txt')
		g1.add_vertex("a")
		self.assertEqual(g1.get_vertices(), ['a', 'v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'])


	# def test_add_edge_01(self):
	# 	g1 = Graph('test1.txt')
	# 	g1.add_vertex("a")
	# 	g1.add_edge("a", "b")
	# 	g1.add_edge("a", "c")
	# 	g1.add_edge("a", "d")
	# 	g1.add_edge("c", "b")
	# 	self.assertEqual(g1.get_vertices(), ["a", "b", "c", "d"])
	# 	self.assertEqual(str(g1), "a connected to: ['b', 'c', 'd']\nb connected to: []\nc connected to: ['b']\nd connected to: []")

	# def test_make_complete(self):
	#     g1 = Graph()
	#     g1.add_vertex("a")
	#     g1.add_edge("a", "b")
	#     g1.add_edge("a", "c")
	#     g1.add_edge("a", "d")
	#     g1.add_edge("c", "b")
	#     g1.make_complete()
	#     self.assertEqual(g1.get_vertices(), ["a", "b", "c", "d"])
	#     self.assertEqual(str(g1), "a connected to: ['b', 'c', 'd']\nb connected to: ['a', 'c', 'd']\nc connected to: ['b', 'a', 'd']\nd connected to: ['a', 'b', 'c']")

	# def test_get_connections(self):
	#     g1 = Graph()
	#     g1.add_vertex("a")
	#     g1.add_edge("a", "b")
	#     g1.add_edge("a", "c")
	#     g1.add_edge("a", "d")
	#     self.assertEqual(g1.vert_list['a'].get_connections(), ['b', 'c', 'd'])

	# def test_id(self):
	#     g1 = Graph()
	#     g1.add_vertex("a")
	#     self.assertEqual(g1.vert_list['a'].get_id(), 'a')

	# def test_get_weight(self):
	#     g1 = Graph()
	#     g1.add_vertex("a")
	#     g1.add_edge("a", "b")
	#     self.assertEqual(g1.vert_list['a'].get_weight(g1.vert_list['b']), 0)

	# def test_get_vertex(self):
	#     g1 = Graph()
	#     g1.add_vertex("a")
	#     g1.add_vertex("b")
	#     g1.add_vertex("c")
	#     self.assertEqual(g1.get_vertex('z'), None)

	# def test_add_edge_02(self):
	#     g1 = Graph()
	#     g1.add_edge("a", "b")
	#     self.assertEqual(g1.vert_list['a'].get_connections(), ['b'])

if __name__ == '__main__':
   unittest.main()
