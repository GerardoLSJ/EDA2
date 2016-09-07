
def BinarySearch(arr,query,start,end):
    if(start > end):
        print("False")
        return False

    medium = int((end - start)/2) + start

    print("medium",medium)
    print("start",start)
    print("end",end)
    

    if(arr[medium] == query):
        print(medium)
        print("Arr[c] == query")
        return medium

    else:
        if(query > arr[medium]):
            print("if")


            return BinarySearch(arr,query,medium+1,end)

        else:
            print("else")


            return  BinarySearch(arr,query,start,medium-1)
           


lista = [1,2,3,4,5,6,7,11,44,85]

index = BinarySearch(lista,int(raw_input()),0, (len(lista)-1) )
print("index",index)
print("lista: ",lista[index])
