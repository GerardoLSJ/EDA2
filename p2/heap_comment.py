#!/usr/bin/python
# -*- coding: utf-8 -*-
#Import library for stdin 
import sys
#import numpy as np
import time

"""
Funcionamiento:
Basicamente recorremos el arreglo una vez o "arbol" para encontrar un MAXIMO 
este se vuelve nuestro ROOT, despues los nodos "padres" con sus hijos estan 
de cierta manera "ordenaodos" por lo que aprovechamos eso para ahora solo reccorer
las partes del arreglo necesarias, es decir de las hojas mas grandes el camino
mas corto a la ROOT con heapify_rec, de esta manera nos ahorramos el recorrer elementos
que ya esta pseudo-ordenados en sus localidades de "padre - hijos"

"""

comps = 0
def heapify(list,i):                
    global comps                    
    if(2*i + 1 	<= len(list)-1 ):       #primero caso 
        comps+=1
        if(list[2*i] < list[2*i + 1]):  #Primero checamos cual hijo es mayor
            comps+=1
            max = 2*i+1                 #y guardamos su localidad
        else:
            max = 2*i                   #en ambos casos 
        if (list[i] < list[max]):       #checamos si es mayor que el "padre"
            comps+=1
            aux		 = list[i]          #de ser así los intercambiamos
            list[i]	 = list[max]
            list[max] = aux   
    elif (2*i <= len(list)-1):          # Segundo PARES
        comps+=1
        if(list[i] < list[2*i]):        #checamos que el padre
            comps+=1                    #no sea menor que el hijo
            aux		 = list[i]
            list[i]	 = list[2*i]
            list[2*i] = aux
    
    return list

def heapify_rec(list,i):                #Comparamos a los nodos padres con sus
    global comps                        #hijos para hacer o no un intercambio
    if(2*i + 1 	<= len(list)-1 ):       #primero IMPARES 
        comps+=1                        
        if(list[2*i] < list[2*i + 1]):  #Primero checamos cual hijo es mayor
            comps+=1
            max = 2*i+1                 #y guardamos su indice
        else:                           #
            max = 2*i                   #en ambos casos
        if (list[i] < list[max]):       #checamos si es mayor que el "padre"
            comps+=1
            aux		 = list[i]          #de ser así los intercambiamos
            list[i]	 = list[max]
            list[max] = aux
            heapify_rec(list,max)       #ejecutamos sobre la misma rama
                                        # y no sobre todo el arbol
    elif (2*i <= len(list)-1):          # Segundo caso
        comps+=1
        if(list[i] < list[2*i]):        #checamos que el padre
            comps+=1                    #no sea menor que el hijo
            aux		 = list[i]
            list[i]	 = list[2*i]
            list[2*i] = aux
            heapify_rec(list,2*i)       #ejecutamos sobre la misma rama
                                        # y no sobre todo el arbol
    
    return list




def heap(list):

    for i in range(len(list)//2,1,-1 ): #ejecutamos una primera vez 
        list = heapify(list,i)          #sobre todo el arbol para tener un MAX 
                                        #como ROOT
    list =	heapify_rec(list,1 )        
    
    list3 = []                          #almacenamos los valores MAX que 
                                        #vamos "pusheando"
    for i in range(0, len(list)-1 ):    #pusheamos los MAX en vada vuelta
        aux			 = list[1]          # y los eliminamos 
        list[1] 	 = list[len(list)-1]   #conforme vayamos subiendo mas hojas
        list[len(list)-1] = aux
        list3.append(aux)
        list = list[:len(list)-1]
        heapify_rec(list,1)

    return list3


for line in sys.stdin:      
    line = line.replace('[','') #recibimos un String y para volverlo
    line = line.replace(']','') #arreglo tenemos que elimiar esos chars
    line = line.split(',')      #para despues separar en un arr de letras
    line = list(map(int, line)) #y mappearlos (cast) a enteros
    comps = 0
    print (heap(line))
    print(comps)

    

"""


def timeElapsed(arr):
	global comps
	start_time = time.time()
	wow = heap(arr) #custom function
	elapsed_time = time.time() - start_time
	print((elapsed_time ))
	print("Comparaciones: " + str( comps))
	comps = 0


"""