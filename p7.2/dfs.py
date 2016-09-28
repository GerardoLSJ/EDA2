
class vertex:
	def __init__(self, i):
		self.id 	= i
		self.visitado 	= False
		self.nivel 	= -1
		self.vecinos 	= []
		self.costo	= float("inf") #Decimal('Infinity')

	def agregarVecino(self, v):
		if(v[0] not in self.vecinos): 	#Evitar aristas repetidos
			self.vecinos.append(v)
	
class graph:
	def __init__(self,):			#Constructor
		self.vertices = {}
	def agregarVertice(self, v):
		if v not in self.vertices:
			vert = vertex(v)
			self.vertices[v] = vert
		
	def agregarArista(self,a,b,p):
		if (a in self.vertices and b in self.vertices):
			self.vertices[a].agregarVecino([b,p])
			#YA ES DIRIGIDA: self.vertices[b].agregarVecino(a) 

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


	def DFS(self,r,n):
		if r in self.vertices:
			self.vertices[r].visitado = True
			self.vertices[r].nivel = n
			print (r,n)
			for v in self.vertices[r].vecinos:
				if self.vertices[v[0]].visitado == False:			
					self.DFS(v[0],n+1)

	def topoSort(self):
		n = len(self.vertices)  #casa
		for v in self.vertices:
			if self.vertices[v].visitado == False:
				self.DFS(v,0)

				


class main:

	g = graph()
	g.agregarVertice(1)
	g.agregarVertice(2)
	g.agregarVertice(3)
	g.agregarVertice(4)
	g.agregarVertice(5)
	g.agregarVertice(6)
	g.agregarVertice(7)
	
	g.agregarArista(1,2,1)
	g.agregarArista(2,4,1)
	g.agregarArista(2,3,1)
	g.agregarArista(4,3,1)
	g.agregarArista(4,5,1)
	g.agregarArista(6,5,1)
	g.agregarArista(7,6,1)
	g.agregarArista(1,7,1)

	root = 2
	nodes = [2, 46, 164, 76, 128, 36, 183, 156, 58, 70]
	vertex = [[76, 46], [46, 156], [183, 164], [70, 156], [2, 164], [2, 164], [76, 164], [76, 2], [128, 46], [58, 46], [164, 128], [46, 128], [2, 128]]
	"""
	g = graph()

	for item in nodes:
		g.agregarVertice(item)

	for pair in vertex:
		g.agregarArista(pair[0],pair[1], 1)

	"""
	g.imprimirGrafica()
	#g.DFS(root,0)
	g.topoSort()
	#g.BFS(root)
	

	
	
	#TODO: parse list of vertex and Edged 	
	#def borrarVecinos(self, v):

