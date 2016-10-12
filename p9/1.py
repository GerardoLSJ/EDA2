class vertex:
	def __init__(self,v):
		self.id     = v
		self.padre  = None
		self.hizq   = None
		self.hder   = None
		self.altura = -1


class arbol:

	def __init__(self):
		self.raiz = None


	def agregar(self,act, ver):
		if act.id < ver.id:
			if act.hder != None:
				self.agregar(act.hder, ver)
			else:
				act.hder = ver
		else:
			if act.hizq != None:
				self.agregar(act.hizq,ver)
			else:
				act.hizq 	= ver
				ver.padre 	= act


	def agregarVertice(self,v):
		ver = vertex(v)
		if(self.raiz == None):
			self.raiz = ver
		else:
			self.agregar(self.raiz, ver)


	def crearArbol(self,lv):
		for i in range(len(lv)):
			self.agregarVertice(lv[i])

	def imprimir(self,act):
		if act != None:
			self.imprimir(act.hizq)
			print(act.id , act.altura)
			self.imprimir(act.hder)

	def altura(self, act):
		if(act != None):
			a1 = self.altura(act.hizq)
			a2 = self.altura(act.hder)
			act.altura = max([a1,a2]) +1
			return act.altura
		else:
			return -1


	def RR(self, act):
		nr 			= act.hizq
		act.hizq 	= nr.hder
		nr.hder 	= act
		nr.padre 	= act.padre
		act.padre 	= nr
		if act.hizq != None:
			act.hizq.padre = act
		if nr.padre != None:
			nr.padre.hizq = nr


class main:
	t = arbol()
	#t.crearArbol([8,7,6,5])
	#t.crearArbol([8,6,5,10,7,4,3])
	t.crearArbol([8,6,10,5,4])
	t.altura(t.raiz)
	t.imprimir(t.raiz)
	t.RR(t.raiz.hizq)
	t.altura(t.raiz)
	print("------")
	t.imprimir(t.raiz)

	# NOTE: Encontrar al nodo desvalanceado, el 6 la diferencia de sus hijos es mayor de 2.
	# NOTE: Es el nodo mas profundo nuestro target
