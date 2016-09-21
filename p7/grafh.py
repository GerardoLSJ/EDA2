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


class main:
	g = graph()
	g.agregarVertice(1)
	g.agregarVertice(2)
	g.agregarVertice(3)
	g.agregarVertice(4)
	g.agregarVertice(5)
	g.agregarVertice(6)
	
	g.agregarArista(1,2)
	g.agregarArista(2,4)
	g.agregarArista(2,3)
	g.agregarArista(4,3)
	g.agregarArista(4,5)
	g.agregarArista(6,5)
	g.imprimirGrafica()
	g.BFS(int(raw_input()))

	
	
	#TODO: parse list of vertex and Edged
