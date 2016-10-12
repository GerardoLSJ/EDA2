class vertex:
	def __init__(self,v):
		self.id     = v
		self.padre  = None
		self.hizq   = None
		self.hder   = None


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
			print(act.id)
			self.imprimir(act.hder)

class main:
	t = arbol()
	t.crearArbol([8,7,6,5])
	t.imprimir(t.raiz)
