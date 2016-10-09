import sys
arr = []
for line in sys.stdin:
    arr.append(line)

arb = arr[0].replace("[","").replace("]","").replace("\n","").split(",")
inser = arr[1].replace("[","").replace("]","").replace("\n","").split(",")
remove = arr[2].replace("[","").replace("]","")
#Normalizar la cadena de texto

arb = list(map(int,arb))
inser = list(map(int,inser))
#cast a los elementos

def insertar(v,p): #valor(o nodo), posicion
	if p == len(arb): #Si va al final de la lista
		arb.append(v) #se inserta y ya
		
	elif p < len(arb):
		if hijos(p) == 1 or hijos(p) ==3:
			#tiene hijos izq o ambos
			aux = arb[p] #elemento que se dezplazara
			arb[p] = v	 #elemento insertado
			insertar(aux, 2*p)
			#ahora se inseerta el elemento dezplazado
			#de manera recursiva hasta que quede en una 
			#hoja un nodo dezplazado y solo entre al primer IF
			# o el ultimo ELIF
		elif(hijos(p) == 2):
			#solo tiene hijo derecho
			arb[2*p] = arb[p] #Ahora tiene hijo izquierdo :)
			arb[p] = v		  # y no tuvimos que dezplazar nada
		elif hijos(p) == 0:
			crecer(2*p)			#Para evitar salirnos de rango
			arb[2*p] = arb[p]	#pasa al lugar de un hijo izquierdo
			arb[p] = v			#y el insertado a ser el padre.
			



def hijos(p):
	if ( p <= len(arb)-1 ):	#no existe, fuera de rango
		
		if len(arb)-1 >= (2*p+1): #puede que tenga ambos hijos
			if arb[2*p] != None:  #si tiene hijo izuqierdo
				if arb[2*p+1] != None: #si tiene ambos hijos
					return 3
				return 1 #solo tiene hijo izquierdo
			elif arb[2*p +1] != None: #Solo tiene hijo derecho
				return 2
		elif len(arb)-1 >= 2*p:	#solo hijo izquierdo
			if arb[2*p] != None:
				#tiene hijo derecho
				return 1
		else:
			#no tiene hijos
			return 0
	else:
		#no existe
		return -1


	
def crecer(i):			#i = 2*p, seria hijo izquierdo
	j = i - len(arb)+1	#Solo incrementamos la casillas necesarias 
	for l in range(j):	#para que len(arb) == 2*p y así
		arb.append(None)	#tener lugar para el hijo izquierdo


def decrecer():
	global arb
	while(arb[len(arb) -1] == None):
		arb = arb[:len(arb)-1]
#Recorremos el arreglo de derecha a izquierda
#eliminando los "None" hasta llegaar a un valor
#de esa manera no tenemos NONE de más


def eliminar(p):
	if (hijos(p) !=-1 ):
		if(hijos(p) == 0):	#Si no hay hijos solo lo eliminamos sin más
			arb[p] = None 
		elif(hijos(p) == 1  or hijos(p) ==3 ):
			#Si tiene hijo izq o ambos
			arb[p] = arb[2*p] #izquiero pasa a ser padre
			eliminar(2*p)	  #eliminamos a ese izquierdo
		
		elif(hijos(p) == 2 ):
			#Si solo hay hijo derecho
			arb[p] = arb[2*p+1] #Ese hijo pasa a ser padre
			eliminar(2*p+1)		#y lo eliminamos 
			
	decrecer()	#cuando termine la reasignacion debe limpiar los None




insertar(inser[0],inser[1])
eliminar(int(remove))
print(arb)


"""
Sample Output

[0, 20, 1, 88, 46, 114, None, 40, None, None, 6]
[0, 20, 1, 88, 46, 114, None, 40, None, None, 6]


"""