def agregar(cad):
    global ht
    ht[hashD(cad)].append(cad)  #Encontramos la casilla y
                                # lo agreamos como si fuera 
                                #una lista ligada
def buscar(cad):
    global ht
    h = hashD(cad)
    for e in ht[h]:
        if(e == cad):   #Solo nos interesa saber si existe
            return h    # Y de ser así regresa la localidad
    else: return False    

def borrar(cad):
    global ht
    index = buscar(cad)
    if (index):         #Si existe solo borramos la primer
        print "***"     # la primer coincidencia con .remove()
        print ht        # no tenemos que iterar
        print "\t borrando: " + cad + " en indice: " + str(index)
        ht[index].remove(cad)
        print ht
        return True  
    else:
        print("No existe: " + cad)
        return False
  
def preHash(cad):   #Convertimos en ASCII las letras
	salida = ""
	for l in cad:
		salida+=str(ord(l))
	return int(salida)

def hashD(cad):     #El HASH real sucede aquí
    global m 
    x = preHash(cad)    #Tomamos la cadena de numeros
    A = 0.333           #Un numero aleatorio  y lo 
                        #regresamos de la siguiente manera
    return int(( m*((x*A)%1) ))

m   = 13
ht  = [[] for j in range(m) ]  
agregar("gerry")
agregar("perro")
agregar("123")
agregar("asd")
agregar("asde")
agregar("jose")
agregar("Jose")
print( borrar("123") )


