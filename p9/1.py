import sys
arr = []

for line in sys.stdin:
    arr = line.replace('[','').replace(']', '').split(",")
    arr = list(map(int,arr))


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
            print(act.id,act.altura)
            self.imprimir(act.hder)

    def imprimirDesv(self,act, arr=[]):
        if act != None:
            self.imprimirDesv(act.hizq, arr)
            if(act.hizq != None and act.hder != None and abs(act.hizq.altura - act.hder.altura ) > 1 ):
                #print( act.id)
                arr.append(act.id)
            elif(act.hizq == None and act.hder != None and  act.hder.altura  > 0 ):
                #print(act.id)
                arr.append(act.id)
            elif (act.hizq != None and act.hder == None and  act.hizq.altura > 0 ):
                #print(act.id)
                arr.append(act.id)
            #print(act.id,act.altura)
            self.imprimirDesv(act.hder, arr)
            return arr

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
        if self.raiz == act:
            self.raiz = nr


class main:
    t = arbol()
    t.crearArbol(arr)
    t.altura(t.raiz)
    r = t.imprimirDesv(t.raiz)
    print (r)

    # NOTE: Encontrar al nodo desvalanceado, el 6 la diferencia de sus hijos es mayor de 2.
    # NOTE: Es el nodo mas profundo nuestro target
    # NOTE: TAREA, --elimine vertices--,---preservar BST, rotacion a la izqueirda
    # NOTE: TAREA, obtener los vertices desvalanceadoS!