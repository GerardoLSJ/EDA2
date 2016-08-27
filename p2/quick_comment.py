#!/usr/bin/python
# -*- coding: utf-8 -*-
#Import library for stdin 
import sys
import time


"""
Funcionamiento:
QuickSort ubica a los pivotes en su lugar ideal "sweat spot" y convierte en otro arreglo a
 los elementos de su derecha y su izquierda, con los cuales se uso un "pivote" en cada caso que busca su 
"sweet spot" tambien y repite lo mismo que el primero. En resumen podriamos 
decir que ubica a los pivotes en sus posiciones ideales.

"""

comps = 0
def reacomodo(lista,posPivote):
    global comps
    j=0
    for i in range(0,posPivote):            #iteramos hasta el pivote
        if (lista[i] < lista[posPivote]):   #intercambiamos los valores
            comps+=1                        #si son menores que el pivote
            aux		 = lista[j]
            lista[j] = lista[i]
            lista[i] = aux
            j+=1
    
    aux		 = lista[j]                     #si son mayores tambien 
    lista[j] = lista[posPivote]             #tambien intercambiamos
    lista[posPivote] = aux
    return [lista, j] 


def quick(lista):
    global comps
    if(len(lista) <= 1):                #Caso base 1 elemnto
        comps+=1
        return lista
    
    pivote	= len(lista)-1              #Pivote para las comparaciones
    retorno = reacomodo(lista,pivote)   #Funcion recursiva 
    lista 	= retorno[0]                #nueva lista con pivote en su 
    piv 	= retorno[1]                #lugar y pivote

    lista1	= quick(lista[:piv])        #recursivamente dividimos la lista del... 
    lista2  = quick(lista[piv+1:])      #... pivote para atras y adelante
    lista1.append(lista[piv])           #Agregamos el pivote
    return lista1[:] + lista2[:]        #retorna las listas divididas


print (quick([2,4,7,8,5,6,9,5]))
print(comps)

"""

def timeElapsed(arr):
	global comps
	start_time = time.time()
	wow = quick(arr) #custom function
	elapsed_time = time.time() - start_time
	print((elapsed_time ))
	print("Comparaciones: " + str( comps) )
	comps = 0



"""