#!/usr/bin/env python
# -*- coding: utf-8 -*-
def counting(l):
	min = l[0]
	max = min
	for i in range(len(l)):				#Buscamos los maximos y minimoz
		if(min>l[i]):
			min = l[i]
		if(max < l[i]):
			max = l[i]

	print("Minimo: ",min )	
	print("Maximo ",max)
	rango = (max - min + 1)
	ocu = [0 for i in range(rango)]		#Llenamos de '0' un arrego del tamaño del rango
	 
	for i in range(len(l)):				#Contamos las ocurreias de los elementos del arreglo
		ocu[l[i] - min] +=1
	
	for i in range(len(ocu)-1):
		ocu[i+1] = ocu[i] + ocu[i+1]	#Sumamos las ocurrencias
	
	s = [0 for k in range(len(l))]		#Generamos un arreglo para llenar los ya ordenados
	for i in range(len(l)-1,-1,-1): 	#hasta -1 de -1
		ocu[l[i]-min]-=1				#Cuando hay repetidos
		s[ ocu[l[i] - min] ] = l[i]  	#Llenamos el arreglo final con las posiciones correctas
	print s

counting([9,1,1,4,2,2,1,1,1,1,12,8,9])
