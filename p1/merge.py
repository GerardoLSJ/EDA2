#Import library for stdin 
import sys


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

#print(mergeSort([10,2,5,6,2,-1,-5]))



#Read from stdin and pass it to the function
for line in sys.stdin:
    line = line.split(',')              #We recived 10,5,...n so we split by ","
    arr =[int(e.strip()) for e in line] #Now we have an arr ['10','5'...'n'] and we need to cast to NUMBERS
    print(mergeSort(arr))               #Now we pass the arr [10,5,...,n]
    print(comparations)
    

