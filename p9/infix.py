lista = [0, 67, 27, 28, 79, 72, 14, 48]
lista_infix = []
lista_prefix = []
lista_posfix = []

def infix(i):
    global lista
    global lista_infix
    if(len(lista)-1 >= 2*i):

        if(lista[i] != None):
            if(lista[2*i != None]):
                infix(2*i)
            
            #print lista[i]
            lista_infix.append(lista[i])

            if(lista[2*i +1] != None):
                infix(2*i+1)

    else:
        #print lista[i]
        lista_infix.append(lista[i])


infix(1)
print lista_infix


def prefix(i):
    global lista
    global lista_prefix

    if(len(lista)-1 >= 2*i):

        if(lista[i] != None):

            if(lista[2*i != None]):
                #print lista[i]
                lista_prefix.append(lista[i])
                prefix(2*i)
                
            
        
            if(lista[2*i +1] != None):
                
                prefix(2*i+1)
                

    else:
        #print lista[i]
        lista_prefix.append(lista[i])

prefix(1)
print lista_prefix

def posfix(i):
    global lista
    global lista_posfix
    if(len(lista)-1 >= 2*i):

        if(lista[i] != None):

            if(lista[2*i != None]): #Tiene izquierdo?
                posfix(2*i)

            if(lista[2*i +1] != None):
                
                posfix(2*i+1)
                #print lista[i] #despues de imprimir el hijo derecho el padre
                lista_posfix.append(lista[i])
    else:
        #print lista[i]
        lista_posfix.append(lista[i])

posfix(1)
print lista_posfix