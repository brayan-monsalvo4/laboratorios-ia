from typing import Dict, List
class Grafo:
	# Constructor
	def __init__(self, aristas : Dict[int, List[int]], total : int):
		self.lista_adyacencia : Dict[int, List[int]] = dict()
		
		# recorre todas las aristas, guardando el nodo inicial y el destino en una tupla
		for (src, end) in aristas:

			# si no se encuentra el nodo inicial
			if not src in self.lista_adyacencia.keys():
				self.lista_adyacencia.update({ src : list() })

			# si no se encuentra el nodo inicial (final, ya que es un grafo no dirigido)
			if not end in self.lista_adyacencia.keys():
				self.lista_adyacencia.update( {end : list()} )

			# cada nodo (key) tiene una lista (value) de nodos adyacentes:

			# se anade a la lista de nodos adyacentes
			self.lista_adyacencia.get(src).append(end)
			self.lista_adyacencia.get(end).append(src)

		self.total_vertices = total


def BFS(grafo : Grafo, inicial : int, descubiertos : list[int]):
	# crea una lista para simular una COLA
	q = list()

	# anade el nodo inicial como descubierto
	descubiertos.append(inicial)
	
	# encola el primer nodo 
	q.append(inicial)

	# se ejecuta mientras la cola no este vacia
	while len(q) != 0:

		# saca el nodo de la cola
		nodo = q.pop(0)

		print(nodo, end='-')

		# si el nodo no tiene hijos, entonces salta hacia el siguiente ciclo, para no generar una excepcion
		if not nodo in grafo.lista_adyacencia.keys():
			continue

		# para cada arista (u, v)
		for u in grafo.lista_adyacencia.get(nodo):

			# si u no ha sido descubierto
			if not u in descubiertos:
				
				#se encola y agrega a la lista de descubiertos
				descubiertos.append(u)
				q.append(u)
		

if __name__ == '__main__':
	# aristas entre nodos
	aristas = [
		(1,2), (1,3), (2, 4), (2, 5), (3, 6), (3, 7), (5, 8)
	]

	# numero total de nodos
	n = 8

	# instancia de grafo con la lista de aristas y total de nodos
	grafo = Grafo(aristas, n)

	# realiza el algoritmo BFS para todos los nodos en n
	# range(1, n+1) para recorrer a partir de 1 y finalizar en n+1, ya que range no es inclusiva
	# en el extremo superior
	for i in range(1, n+1):
		BFS(grafo=grafo, inicial=i, descubiertos=list())
		print("\n")
		