class vertex:
	def __init__(self,v):
		self.id     = v
		self.padre  = None
		self.hizq   = None
		self.hder   = None


class arbol:

	def __init__(self):
		self.raiz = None


	def agregar(self, ver):
		if act.id < ver.id:
			if act.hder != None:
				agregar(act.hder, ver)
			else:
				act.hder = ver
		else:
			if act.hizq != None:
				agregar(act.hizq,ver)
			else:
				act.hizq = ver


	def agregarVertice(self,v):
		ver = vertex(v)
		if(self.raiz == None):
			self.raiz = ver
		else:
			agregar(self.raiz, ver)


	def crearArbol(self,lv):
		for i in range(len(lv)):
			agregarVertice(i)

class main:
	t = arbol()
	t.crearArbol([7,6,5])
