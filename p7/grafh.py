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


class main:
	g = graph()
	g.agregarVertice(1)
	g.agregarVertice(2)
	g.agregarVertice(3)
	g.agregarVertice(4)
	g.agregarVertice(5)
	g.agregarArista(1,2)
	g.agregarArista(2,4)
	g.agregarArista(2,3)
	g.agregarArista(4,3)
	g.agregarArista(4,5)

	g.imprimirGrafica()
	
	#TODO: parse list of vertex and Edged
