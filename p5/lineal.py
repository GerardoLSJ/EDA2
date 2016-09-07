def bsec(l,j):
	for i in range(len(l)):
		if( j == int(l[i][0]) ):
			return l[i]
		
	return None					


archivo = open("lista.txt","r")
la = []
for linea in archivo.readlines():
	tupla = linea.split("\t")
	tupla[2] = tupla[2].replace("\n","")
	la.append(tupla)



#print(bsec(la,38))

print(bsec(  la, int(raw_input() )) )
