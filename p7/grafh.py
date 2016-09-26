class vertex:
	def __init__(self, i):
		self.id 		= i
		self.visitado 	= False
		self.nivel 		= -1
		self.vecinos 	= []

	def agregarVecino(self, v):
		if(v not in self.vecinos): 	#Evitar aristas repetidos
			self.vecinos.append(v)
	
class graph:
	def __init__(self,):			#Constructor
		self.vertices = {}
	def agregarVertice(self, v):
		if v not in self.vertices:
			vert = vertex(v)
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
		if( r in self.vertices):		#Comprobar existencia del 
			cola = []					#nodo objetivo 
			cola.append(r)
			self.vertices[r].visitado = True
			self.vertices[r].nivel = 0
			print(r,0) 					#Primera pareja
			while(len(cola)>0):
				act = cola[0]
				cola = cola[1:]			#cortamos la lista 
				for vec in self.vertices[act].vecinos:
					#Para cada vecino checamos que no haya sido visitado 
					if(self.vertices[vec].visitado == False):
						cola.append(vec)	#Agregamos a la cola y marcamos 
											#como visitado para evitar repetir
						self.vertices[vec].visitado = True
						self.vertices[vec].nivel = self.vertices[act].nivel +1
											#Asignamos un nivel mas que el padre.
						print(vec, self.vertices[vec].nivel ) 
		else:
			print("Vertice no existe")	


class main:
	root = 46
	nodes = [2, 46, 164, 76, 128, 36, 183, 156, 58, 70]
	vertex = [[76, 46], [46, 156], [183, 164], [70, 156], [2, 164], [2, 164], [76, 164], [76, 2], [128, 46], [58, 46], [164, 128], [46, 128], [2, 128]]

	g = graph()

	for item in nodes:
		g.agregarVertice(item)

	for pair in vertex:
		g.agregarArista(pair[0],pair[1])

	
	g.imprimirGrafica()
	g.BFS(root)

	
	
	#TODO: parse list of vertex and Edged 	
	#def borrarVecinos(self, v):

