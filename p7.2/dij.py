
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

	def minimo(self,l):
		m = self.vertices[l[0]].costo
		v = l[0]
		for e in l:
			if(m > self.vertices[e].costo):
				m = self.vertices[e].costo
				v = e
		return v

			

	def dijkstra(self,a,b):
		#verificar que a y b existad y shalala
		lista=[]
		self.vertices[a].costo = 0
		for v in self.vertices[a].vecinos:
			self.vertices[v[0]].costo = v[1]
			lista.append(v[0])
		print (lista)
		while(len(lista)>0):
			m = self.minimo(lista)
			for vec in self.vertices[m].vecinos:
				if (self.vertices[m].costo + vec[1]) < (self.vertices[vec[0]].costo): 
					self.vertices[vec[0]].costo = self.vertices[m].costo + vec[1]
					print(self.vertices[vec[0]].costo)
				
				if(vec[0] not in lista):
					print("before",lista)
					lista.append(vec[0])
					print("after",lista)
			lista.remove(m)		
			
			

				


class main:

	g = graph()
	g.agregarVertice(1)
	g.agregarVertice(2)
	g.agregarVertice(3)
	g.agregarVertice(4)
	g.agregarVertice(5)
	g.agregarVertice(6)
	g.agregarVertice(7)
	
	g.agregarArista(1,2,2)
	g.agregarArista(2,4,1)
	g.agregarArista(2,3,5)
	g.agregarArista(4,3,2)
	g.agregarArista(4,5,4)
	g.agregarArista(6,5,3)
	g.agregarArista(7,6,1)
	g.agregarArista(1,7,4)

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
	g.dijkstra(1,3)
	#g.DFS(root,0)
	#g.topoSort()
	#g.BFS(root)
	

	
	
	#TODO: parse list of vertex and Edged 	
	#def borrarVecinos(self, v):

