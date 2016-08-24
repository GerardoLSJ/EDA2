def reacomodo(lista,posPivote):
	j=0
	for i in range(0,posPivote):
		if (lista[i] < lista[posPivote]):

			aux		 = lista[j]
			lista[j] = lista[i]
			lista[i] = aux
			j+=1
	
	aux		 = lista[j]
	lista[j] = lista[posPivote]
	lista[posPivote] = aux
	return [lista, j] 





def quick(lista):
	if(len(lista) <= 1):
		return lista
	
	pivote	= len(lista)-1
	retorno = reacomodo(lista,pivote)
	lista 	= retorno[0]
	piv 	= retorno[1]

	lista1	= quick(lista[:piv])
	lista2  = quick(lista[piv+1:])
	lista1.append(lista[piv])
	return lista1[:] + lista2[:]


print( quick(['a',4,6,2,1,3,8,5,5,8,4,15152,4,847,-514,5,'b']) )
print( quick(['a','A','b','z' ]) )
