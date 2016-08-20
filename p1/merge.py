#Import library for stdin 
import sys
#import numpy as np
import time

comparations = 0
def mergeList(list1,list2):
	global comparations
	list3 = []
	while(len(list1)>0 and len(list2)>0  ):
		comparations+=1

		if( list1[0] < list2[0] ):
			list3.append(list1[0])
			list1 = list1[1:]			
		
		else:
			list3.append(list2[0])
			list2 = list2[1:]
			
	while(len(list1)>0):
		list3.append(list1[0])
		list1 = list1[1:]
				
	while(len(list2)>0):
		list3.append(list2[0])
		list2 = list2[1:]
			
	return (list3)


 
def mergeSort(list):
	if(len(list) == 1):
		return list
	
	leftList  = list[:len(list)//2]
	rigthList = list[len(list)//2:]

	leftList  = mergeSort(leftList)  #ask in class
	rigthList = mergeSort(rigthList)

	return mergeList(leftList , rigthList)	

def timeElapsed(arr):
	global comparations
	start_time = time.time()
	mergeSort(arr)
	elapsed_time = time.time() - start_time
	print((elapsed_time ))
	print("Comparaciones: " + str( comparations) )
	comparations = 0

timeElapsed([5,1,6,-4,7]) #5
timeElapsed([5,1,6,-4,7,7,9,11,-95,74]) #10
timeElapsed([5,1,6,-4,7,7,9,11,-95,74,4,8,7,1,5]) #15
timeElapsed([5,1,6,-4,7,7,9,11,-95,74,4,8,7,1,5,44,7,-874,47,98,14]) #20
timeElapsed([5,1,6,-4,7,7,9,11,-95,74,4,8,7,1,5,44,7,-874,47,98,14,88,7,963,741,85]) #25
timeElapsed([5,1,6,-4,7,7,9,11,-95,74,4,8,7,1,5,44,7,-874,47,98,14,88,7,963,741,85,15,24,-9,74,-36]) #30
timeElapsed([5,1,6,-4,7,7,9,11,-95,74,4,8,7,1,5,44,7,-874,47,98,14,88,7,963,741,85,15,24,-9,74,-36,1,5,2,7,8]) #35
timeElapsed([5,1,6,-4,7,7,9,11,-95,74,4,8,7,1,5,44,7,-874,47,98,14,88,7,963,741,85,15,24,-9,74,-36,1,5,2,7,8,55,-99,-451,-967,-4]) #40
timeElapsed([5,1,6,-4,7,7,9,11,-95,74,4,8,7,1,5,44,7,-874,47,98,14,88,7,963,741,85,15,24,-9,74,-36,1,5,2,7,8,55,-99,-451,-967,-4,8,96,-789,-74,-967]) #45
timeElapsed([5,1,6,-4,7,7,9,11,-95,74,4,8,7,1,5,44,7,-874,47,98,14,88,7,963,741,85,15,24,-9,74,-36,1,5,2,7,8,55,-99,-451,-967,-4,8,96,-789,-74,-967,-159,-753,-7894,-1245]) #50
timeElapsed([5,1,6,-4,7,7,9,11,-95,74,4,8,7,1,5,44,7,-874,47,98,14,88,7,963,741,85,15,24,-9,74,-36,1,5,2,7,8,55,-99,-451,-967,-4,8,96,-789,-74,-967,-159,-753,-7894,-1245,1,65,987,45,25]) #55
timeElapsed([5,1,6,-4,7,7,9,11,-95,74,4,8,7,1,5,44,7,-874,47,98,14,88,7,963,741,85,15,24,-9,74,-36,1,5,2,7,8,55,-99,-451,-967,-4,8,96,-789,-74,-967,-159,-753,-7894,-1245,1,65,987,45,25,415,484,96,147544,145]) #60
timeElapsed([5,1,6,-4,7,7,9,11,-95,74,4,8,7,1,5,44,7,-874,47,98,14,88,7,963,741,85,15,24,-9,74,-36,1,5,2,7,8,55,-99,-451,-967,-4,8,96,-789,-74,-967,-159,-753,-7894,-1245,1,65,987,45,25,415,484,96,147544,145,-963,-78485,-4515,-7415,45]) #65
timeElapsed([5,1,6,-4,7,7,9,11,-95,74,4,8,7,1,5,44,7,-874,47,98,14,88,7,963,741,85,15,24,-9,74,-36,1,5,2,7,8,55,-99,-451,-967,-4,8,96,-789,-74,-967,-159,-753,-7894,-1245,1,65,987,45,25,415,484,96,147544,145,-963,-78485,-4515,-7415,45,1,2,5,4,8]) #70
timeElapsed([5,1,6,-4,7,7,9,11,-95,74,4,8,7,1,5,44,7,-874,47,98,14,88,7,963,741,85,15,24,-9,74,-36,1,5,2,7,8,55,-99,-451,-967,-4,8,96,-789,-74,-967,-159,-753,-7894,-1245,1,65,987,45,25,415,484,96,147544,145,-963,-78485,-4515,-7415,45,1,2,5,4,8,99,5,-999,-4481,-875441]) #75



"""

#Read from stdin and pass it to the function
for line in sys.stdin:
    line = line.split(',')              #We recived 10,5,...n so we split by ","
    arr =[int(e.strip()) for e in line] #Now we have an arr ['10','5'...'n'] and we need to cast to NUMBERS
    print(mergeSort(arr))               #Now we pass the arr [10,5,...,n]
    print(comparations)
    

"""