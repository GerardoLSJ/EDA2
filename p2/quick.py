#!/usr/bin/python
# -*- coding: utf-8 -*-
#Import library for stdin 
import sys
#import numpy as np
import time

comps = 0
def reacomodo(lista,posPivote):
    global comps
    j=0
    for i in range(0,posPivote):
        if (lista[i] < lista[posPivote]):
            comps+=1

            aux		 = lista[j]
            lista[j] = lista[i]
            lista[i] = aux
            j+=1
    
    aux		 = lista[j]
    lista[j] = lista[posPivote]
    lista[posPivote] = aux
    return [lista, j] 





def quick(lista):
    global comps
    if(len(lista) <= 1):
        comps+=1
        return lista
    
    pivote	= len(lista)-1
    retorno = reacomodo(lista,pivote)
    lista 	= retorno[0]
    piv 	= retorno[1]

    lista1	= quick(lista[:piv])
    lista2  = quick(lista[piv+1:])
    lista1.append(lista[piv])
    return lista1[:] + lista2[:]


for line in sys.stdin:
    line = line.replace('[','')
    line = line.replace(']','')
    line = line.split(',')
    line = list(map(int, line))
    comps = 0
    print (quick(line))
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