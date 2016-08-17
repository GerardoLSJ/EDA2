comparations = 0

def BubbleSort(arr):
    global comparations
    list = arr
    for j in range(len(list)-1):
      for i in range ( len(list)-1-j):
         comparations+=1     
  	 if(list[i] > list[i+1] ):
      	   aux = list[i+1]
	   list[i+1] = list[i]
	   list[i] = aux
           
    
    print(list)
    print("Comparaciones: " + str( comparations) )


BubbleSort([2,3,4,5,1,51,2,41,0])
