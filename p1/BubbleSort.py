import time

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

def timeElapsed(arr):
	start_time = time.time()
	print(BubbleSort(arr)) 
	elapsed_time = time.time() - start_time
	print(float("{0:.12f}".format(elapsed_time )))


timeElapsed([5,1,6,-4,7]) #5
timeElapsed([5,1,6,-4,7,7,9,11,-95,74]) #10
timeElapsed([5,1,6,-4,7,7,9,11,-95,74,4,8,7,1,5]) #15
timeElapsed([5,1,6,-4,7,7,9,11,-95,74,4,8,7,1,5,44,7,-874,47,98,14]) #20