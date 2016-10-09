#Import library for stdin 
import sys

for linea in sys.stdin:
    linea = linea.replace("[","").replace("]","").split(",")
    if len(linea) > 1 :
        linea = list(map(int,linea))
       
    
    
lista = linea  
lista_infix = []
lista_prefix = []
lista_posfix = []



def infix(i):
    global lista
    global lista_infix
    

    if(len(lista) == 0):
        return 0

    elif(len(lista) == 1):
        lista_infix.append(lista[0])

    elif(len(lista)-1 >= 2*i):

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


def prefix(i):
    global lista
    global lista_prefix

    if(len(lista) == 0):
        return 0

    elif(len(lista) == 1):
        lista_prefix.append(lista[0])


    elif(len(lista)-1 >= 2*i):

        if(lista[i] != None):

            if(lista[2*i != None]):
                
                lista_prefix.append(lista[i])
                prefix(2*i)
                
            
        
            if(lista[2*i +1] != None):
                
                prefix(2*i+1)
                
    else:
        
        lista_prefix.append(lista[i])


def posfix(i):
    global lista
    global lista_posfix


    if(len(lista) == 0):
        return 0

    elif(len(lista) == 1):
        lista_posfix.append(lista[0])

    elif(len(lista)-1 >= 2*i):

        if(lista[i] != None):

            if(lista[2*i != None]): #Tiene izquierdo?
                posfix(2*i)

            if(lista[2*i +1] != None):
                
                posfix(2*i+1)
                #despues de imprimir el hijo derecho el padre
                lista_posfix.append(lista[i])
    else:
        
        lista_posfix.append(lista[i])


infix(1)
print (lista_infix)

prefix(1)
print (lista_prefix)

posfix(1)
print (lista_posfix)