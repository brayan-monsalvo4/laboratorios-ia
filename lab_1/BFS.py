from collections import deque
from typing import Dict, List, Tuple

# A class to represent a graph object
class Graph:
	# Constructor
	def __init__(self, edges : Dict[int, List[int]], numero_total_vertices : int):

		self.lista_adyacencia : Dict[int, List[int]] = dict()

		# A list of lists to represent an adjacency list as a dict
		for (src, end) in edges:
			if not src in self.lista_adyacencia.keys():
				self.lista_adyacencia.update({ src : list() })
			
			if not end in self.lista_adyacencia.keys():
				self.lista_adyacencia.update( {end : list()} )

			self.lista_adyacencia.get(src).append(end)
			self.lista_adyacencia.get(end).append(src)

		self.total_vertices = numero_total_vertices

# Perform BFS on the graph starting from vertex `v`
def BFS(graph : Graph, inicial : int, descubiertos : list[int]):

	# create a queue for doing BFS
	q = deque()

	# mark the source vertex as discovered
	discovered.append(inicial)
	
	# enqueue source vertex
	q.append(inicial)

	# loop till queue is empty
	while len(q) != 0:

		# dequeue front node and print it
		nodo = q.popleft()

		print(nodo, end='-')

		if not nodo in graph.lista_adyacencia.keys():
			continue

		# do for every edge (v, u)
		for u in graph.lista_adyacencia.get(nodo):
			if not u in discovered:
				# mark it as discovered and enqueue it
				discovered.append(u)
				q.append(u)


if __name__ == '__main__':

	#dddd
	edges = [
		(1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4), (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
	]

	# total number of nodes in the graph (labelled from 0 to 14)
	n = 15

	# build a graph from the given edges
	graph = Graph(edges, n)

	print(graph.lista_adyacencia)

	# to keep track of whether a vertex is discovered or not
	discovered = list()

	# Perform BFS traversal from all undiscovered nodes to
	# cover all connected components of a graph
	#for i in range(n):
	BFS(graph=graph, inicial=1, descubiertos=discovered)
		#print("\n")
