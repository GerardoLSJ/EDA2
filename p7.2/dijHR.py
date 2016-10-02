import sys
path = []
costo = -1

class vertex:
    def __init__(self, i):
        self.id 	= i
        self.visitado 	= False
        self.nivel 	= -1
        self.vecinos 	= []
        self.costo	= float('inf') #Decimal('Infinity')
        self.padre = False

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
            print("Vertices: ", self.vertices[v].id, "PADRE: ",self.vertices[v].padre, "COSTO: ",self.vertices[v].costo  )
            #print("Aristas: ", self.vertices[v].vecinos)		

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
        #print (lista)
        while(len(lista)>0):
            m = self.minimo(lista)
            for vec in self.vertices[m].vecinos:
                if (self.vertices[m].costo + vec[1]) < (self.vertices[vec[0]].costo): 
                    self.vertices[vec[0]].costo = self.vertices[m].costo + vec[1]
                    self.vertices[vec[0]].padre = self.vertices[m].id
                    #print("Hijo: ",self.vertices[vec[0]].id )
                    #print("padre: ",self.vertices[vec[0]].padre )
                    #print(self.vertices[vec[0]].costo)
                
                if(self.vertices[vec[0]].visitado ==False):
                    #print("before",lista)
                    lista.append(vec[0])
                    #print("after",lista)
            lista.remove(m)
            self.vertices[m].visitado =True		
            
            
    def shortPath(self,source, target):
        global path
        global costo
        
        path.append(target)
        if( self.vertices[target].padre != False):
            #print(self.vertices[target].padre)
            path.append(self.vertices[target].padre)
            self._shortPath(source, self.vertices[target].padre)
            
        else:
            path.append(self.vertices[source].id)
            costo = self.vertices[path[0]].costo 
            

    def _shortPath(self,source, target):
        global path
        global costo
        if( self.vertices[target].padre != False):
            path.append(self.vertices[target].padre)
            #print(self.vertices[target].padre)
            self._shortPath(source, self.vertices[target].padre)
            
        else:
            path.append(self.vertices[source].id)
            costo = self.vertices[path[0]].costo 


class main:

    arr = []
    for line in sys.stdin:
        arr.append(line)
                
                
    nodes   = arr[0].replace("[","").replace("]","")
    vertex  = arr[1]
    root    = arr[2].replace("(","").replace(")","")
    # extracting useful data (could be more efficient)
    root    = root.split(',')
    root   = list(map(int, root))
    nodes   = nodes.split(',')
    nodes   = list(map(int, nodes))
    
    first   = vertex.index('[')
    last    = vertex.rindex(']')
 
    
    vertex = vertex[first+2:]
    vertex = vertex[:last-3]
    vertex = vertex.split('], [')
    #print(vertex)
    g = graph()

    for item in nodes:
        #print(item)
        g.agregarVertice(item)

    for pair in vertex:
        
        pair = pair.split(',')
        pair = list(map(int,pair))
        
        g.agregarArista(pair[0],pair[1],pair[2])


    g.dijkstra(root[0],5)
    g.shortPath(root[0],root[1])
    if costo >= float('inf'):
        print("No existe camino")
    else:
        rev = path[::-1] 
        print (rev) 
        print (costo)






