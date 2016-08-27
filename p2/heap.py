#!/usr/bin/python
# -*- coding: utf-8 -*-
#Import library for stdin 
import sys
#import numpy as np
import time

comps = 0
def heapify(list,i):
	if(2*i + 1 	<= len(list)-1 ):
		if(list[2*i] < list[2*i + 1]):
			max = 2*i+1
		else:
			max = 2*i

		if (list[i] < list[max]):
			aux		 = list[i]
			list[i]	 = list[max]
			list[max] = aux

	elif (2*i <= len(list)-1):
		if(2*i <= len(list)-1):
			aux		 = list[i]
			list[i]	 = list[2*i]
			list[2*i] = aux
	
	return list


def heapify_rec(list,i):
	if(2*i + 1 	<= len(list)-1 ):
		if(list[2*i] < list[2*i + 1]):
			max = 2*i+1
		else:
			max = 2*i

		if (list[i] < list[max]):
			aux		 = list[i]
			list[i]	 = list[max]
			list[max] = aux
			heapify_rec(list,max)

	elif (2*i <= len(list)-1):
		if(list[i] < list[2*i]):
			aux		 = list[i]
			list[i]	 = list[2*i]
			list[2*i] = aux
			heapify_rec(list,2*i)
	
	return list




def heap(list):
	for i in range(len(list)//2,1,-1 ):
		list = heapify(list,i)
	list =	heapify_rec(list,1 )
	list3 = []
	for i in range(0, len(list)-1 ):
		print(list[1])
		aux			 = list[1]
		list[1] 	 = list[len(list)-1]
		list[len(list)-1] = aux
		list3.append(aux)
		list = list[:len(list)-1]
		heapify_rec(list,1)
	return list3


def timeElapsed(arr):
	global comps
	start_time = time.time()
	wow = heap(arr) #custom function
	elapsed_time = time.time() - start_time
	print((elapsed_time ))
	print("Comparaciones: " + str( comps))
	comps = 0


timeElapsed([0,72,4,17,57,8,87,78,73])