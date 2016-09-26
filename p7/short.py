import sys

class vertex:
	def __init__(self, i):
		self.id 	= i
		self.visitado 	= False
		self.nivel 	= -1
		self.vecinos 	= []

	def agregarVecino(self, v):
		if(v not in self.vecinos): #NOT
			self.vecinos.append(v)
	
	#def borrarVecinos(self, v):

	
class graph:
	def __init__(self,):
		self.vertices = {}
	def agregarVertice(self, v):
		if v not in self.vertices:
			vert 		 = vertex(v)
			self.vertices[v] = vert
		

	def agregarArista(self,a,b):
		if (a in self.vertices and b in self.vertices):
			self.vertices[a].agregarVecino(b)
			self.vertices[b].agregarVecino(a) 

	def imprimirGrafica(self):
		print("Grafica: ")
		for v in self.vertices:
			print("Vertices: ", self.vertices[v].id)
			print("Aristas: ", self.vertices[v].vecinos)		

	def BFS(self, r):
		if( r in self.vertices):
			cola = []
			cola.append(r)
			self.vertices[r].visitado = True
			self.vertices[r].nivel = 0
			print(r,0) #primera linea bonita
			while(len(cola)>0):
				act = cola[0]
				cola = cola[1:]
				for vec in self.vertices[act].vecinos:
					if(self.vertices[vec].visitado == False):
						
						cola.append(vec)
						self.vertices[vec].visitado = True
						self.vertices[vec].nivel = self.vertices[act].nivel +1
						print(vec, self.vertices[vec].nivel ) 
		else:
			print("Vertice no existe")	

	
	def _BFS(self,root,target):
		
		self.BFS(target)
		if self.vertices[root].nivel == -1:
			print("No existe camino")
		else:

			actual = root
			l = []
			l.append(actual)
			#print(actual)

			while actual != target:
				for vec in self.vertices[actual].vecinos:
					if self.vertices[vec].nivel == self.vertices[actual].nivel -1:
						l.append(vec)
						#print(vec)
						actual = vec
			
			for i in reversed(l):
				print i


class main:
	#root = [100, 133]
	root =[45, 155]
	nodes = [45, 84, 169, 64, 21, 155, 83, 52, 22, 162, 27, 110, 60, 154, 128, 181, 114]
	vertex = [[84, 128], [60, 169], [169, 60], [27, 52], [154, 155], [162, 84], [128, 60], [162, 181], [154, 155], [60, 114], [21, 181], [27, 52], [52, 155], [155, 52], [110, 60], [110, 114], [64, 84], [114, 22], [45, 22], [114, 162], [169, 22], [83, 110], [181, 60], [154, 181], [169, 110], [110, 169]]
	g = graph()

	for item in nodes:
		g.agregarVertice(item)

	for pair in vertex:
		g.agregarArista(pair[0],pair[1])

	
	#g.imprimirGrafica()
	g._BFS(root[1],root[0])

	
	
	#TODO: parse list of vertex and Edged
