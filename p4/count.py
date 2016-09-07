#!/usr/bin/env python
# -*- coding: utf-8 -*-
def counting(l):
	min = l[0]
	max = min
	for i in range(len(l)):
		if(min>l[i]):
			min = l[i]
		if(max < l[i]):
			max = l[i]

	print("Minimo: ",min )	
	print("Maximo ",max)
	rango = (max - min + 1)
	ocu = [0 for i in range(rango)]
	 
	for i in range(len(l)):
		ocu[l[i] - min] +=1
	
	for i in range(len(ocu)-1):
		ocu[i+1] = ocu[i] + ocu[i+1]
	
	s = [0 for k in range(len(l))]
	for i in range(len(l)-1,-1,-1):  #hasta -1 de --
		ocu[l[i]-min]-=1
		s[ ocu[l[i] - min] ] = l[i]  
	print s

counting([-9,1,-1,4,2,2,1,1,1,1,12,8,9])
