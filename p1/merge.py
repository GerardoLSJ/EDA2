
#list3 = []
def mergeList(list1,list2):
	#global list3
	list3 = []
	while(len(list1)>0 and len(list2)>0  ):

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

print(mergeSort([2,1,5,3,10,0]))
#mergeSort([1,2,56,5,4,9])
#print(list3)



