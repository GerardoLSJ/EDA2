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
				act.hizq = ver


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
			print max([a1,a2])
			act.altura = max([a1,a2]) +1
			return act.altura
		else:
			return -1




class main:
	t = arbol()
	#t.crearArbol([8,7,6,5])
	t.crearArbol([8,5,10,6,7])
	t.altura(t.raiz)
	t.imprimir(t.raiz)
