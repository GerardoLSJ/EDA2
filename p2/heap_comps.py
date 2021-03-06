#!/usr/bin/python
# -*- coding: utf-8 -*-
#Import library for stdin 
import sys
#import numpy as np
import time

comps = 0

def heapify_rec(list,i):
    global comps
    if(2*i + 1 	<= len(list)-1 ):
        comps+=1
        if(list[2*i] < list[2*i + 1]):
            
            max = 2*i+1
        else:
            max = 2*i
        comps+=1
        if (list[i] < list[max]):
            
            aux		 = list[i]
            list[i]	 = list[max]
            list[max] = aux
            heapify_rec(list,max)
    
    elif (2*i <= len(list)-1):
        comps+=1
        if(list[i] < list[2*i]):
            
            aux		 = list[i]
            list[i]	 = list[2*i]
            list[2*i] = aux
            heapify_rec(list,2*i)
    
    return list




def heap(list):

    for i in range(len(list)//2,0,-1 ):
        list = heapify_rec(list,i)


    
    list3 = []
    
    for i in range(0, len(list)-1 ):
        aux			 = list[1]
        list[1] 	 = list[len(list)-1]
        list[len(list)-1] = aux
        list3.append(aux)
        list = list[:len(list)-1]
        heapify_rec(list,1)

    return list3


for line in sys.stdin:
    line = line.replace('[','')
    line = line.replace(']','')
    line = line.split(',')
    line = list(map(int, line))
    comps = 0
    print (heap(line))
    print(comps)

    

    


