
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

lista_infix = []


lista = [0,67,27,28,79,72]
arb = lista
def infix(i):
    global lista
    global lista_infix
    
    if(2*i <= len(lista)-1  ):

        if(lista[i] != None):
            if(lista[2*i != None]):
                infix(2*i)
            
            
            print (lista[i])
            #lista_infix.append(lista[i])

            if(2*i+1 <= len(lista)-1 and lista[2*i +1] != None):
                infix(2*i+1)

    
    
    else:
        print (lista[i])

#

infix(1)
lista = [0,67,27]
arb = lista
print("---------")
infix(1)

