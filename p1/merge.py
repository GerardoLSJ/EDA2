

def mergeList(list1,list2):
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


print(mergeSort([14,7,4,2,57,2,7,-2,455,78,12,36,25,58,98,9]))
mergeSort([8,2,56,5,4,9])



