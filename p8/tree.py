
arb = [0,1,6,3,7,9,4,8,19]

def insertar(v,p): #valor(o nodo), posicion
	if p == len(arb):
		arb.append(v)
		
	elif p < len(arb):
		if hijos(p) >= 1:
			aux = arb[p]
			arb[p] = v
			insertar(aux, 2*p)
		
		elif hijos(p) == 0:
			print("hijos=0")
			crecer(2*p)
			arb[2*p] = arb[p]
			arb[p] = v
			



def hijos(p):
	if (len(arb)-1 <= p):	#no existe, fuera de rango
		return -1

	if len(arb)-1 >= (2*p): #tiene hijo izquierdo
		if len(arb)-1 >= 2*p+1:
			return 2	#tiene 2hijos

		return 1		#tiene 1 hijo
	else: 	
		return 0		#tiene 0 hijos



def crecer(i):
	j = i - len(arb)+1
	for l in range(j):
		arb.append(0)




def eliminar(p):
	if (hijos(p) !=-1 ):
		if(hijos(p) == 0):
			arb[p] = 0
		elif(hijos(p) >= 1):
			arb[p] = arb[2*p]
			eliminar(2*p)
			






print(arb)
print hijos(8)
insertar(999,8)


print(arb)


