import sys
arr = []
'''
for line in sys.stdin:
    arr = line.replace('[','').replace(']', '').split(",")
    arr = list(map(int,arr))
'''
node = -1

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
        print("En RR:")
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

    def LR(self, act):
        nr 			= act.hder
        act.hder 	= nr.hizq
        nr.hizq 	= act
        nr.padre 	= act.padre
        act.padre 	= nr
        if act.hizq != None:
            act.hizq.padre = act
        if nr.padre != None:
            nr.padre.hder = nr
        if self.raiz == act:
            self.raiz = nr


    def busq(self, act, query):
        global node
        if act != None:
            if( act.id == query):
                print("FOUND")
                #self.RR(act)
                return act
            elif( act.id < query):
                self.busq(act.hder, query)
            elif( act.id > query):
                self.busq(act.hizq, query) 
        else:
            print("Fin")

class main:
    t = arbol()
    #t.crearArbol([12,10,13,11,9,7])
    t.crearArbol([8, 14, 27, 30, 4, 9])
    t.altura(t.raiz)
    t.imprimir(t.raiz)
    
    print("_________")
    t.altura(t.raiz)
    node = t.busq(t.raiz, 8)
    print(node)
    t.LR(node)  #VE ESTO lol
    t.altura(t.raiz)
    t.imprimir(t.raiz)

    # NOTE: Encontrar al nodo desvalanceado, el 6 la diferencia de sus hijos es mayor de 2.
    # NOTE: Es el nodo mas profundo nuestro target
    # NOTE: TAREA, --elimine vertices--,---preservar BST, rotacion a la izqueirda
    # NOTE: TAREA, obtener los vertices desvalanceadoS!