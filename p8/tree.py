
#arb = [0,1,6,3,7,9,4,8,19]


def insertar(v,p): #valor(o nodo), posicion
	if p == len(arb):
		arb.append(v)
		
	elif p < len(arb):
		if hijos(p) == 1 or hijos(p) ==3:
			#tien izq o ambos
			aux = arb[p]
			arb[p] = v
			insertar(aux, 2*p)
			
		elif(hijos(p) == 2):
			#solo tiene hijo derecho
			arb[2*p] = arb[p]
			arb[p] = v
			#insertar(aux,2*p+1)
		elif hijos(p) == 0:
			crecer(2*p)
			arb[2*p] = arb[p]
			arb[p] = v
			



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


	
def crecer(i):
	j = i - len(arb)+1
	for l in range(j):
		arb.append(None)


def decrecer():
	global arb
	while(arb[len(arb) -1] == None):
		arb = arb[:len(arb)-1]



def eliminar(p):
	if (hijos(p) !=-1 ):
		if(hijos(p) == 0):
			arb[p] = None 
		elif(hijos(p) == 1  or hijos(p) ==3 ):
			arb[p] = arb[2*p]
			eliminar(2*p)
		
		elif(hijos(p) == 2 ):
			arb[p] = arb[2*p+1]
			eliminar(2*p+1)
			
	decrecer()




arb = [0, 20, 1, 57, 46, 6, 88, 40] 
#[114, 5] 
#[3]
insertar(114,5)
print(arb)
eliminar(3)
print(arb)


"""
Sample Output

[0, 20, 1, 88, 46, 114, None, 40, None, None, 6]
[0, 20, 1, 88, 46, 114, None, 40, None, None, 6]


"""