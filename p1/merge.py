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
	start_time = time.time()
	print(mergeSort(arr)) 
	elapsed_time = time.time() - start_time
	print(float("{0:.12f}".format(elapsed_time )))
	print("Comparaciones: " + str( comparations) )

timeElapsed([5,1,6,-4,7]) #5
timeElapsed([5,1,6,-4,7,7,9,11,-95,74]) #10
timeElapsed([5,1,6,-4,7,7,9,11,-95,74,4,8,7,1,5]) #15
timeElapsed([5,1,6,-4,7,7,9,11,-95,74,4,8,7,1,5,44,7,-874,47,98,14]) #20



#print(np.random.rand(10,1))

"""

#Read from stdin and pass it to the function
for line in sys.stdin:
    line = line.split(',')              #We recived 10,5,...n so we split by ","
    arr =[int(e.strip()) for e in line] #Now we have an arr ['10','5'...'n'] and we need to cast to NUMBERS
    print(mergeSort(arr))               #Now we pass the arr [10,5,...,n]
    print(comparations)
    

"""