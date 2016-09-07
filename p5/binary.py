contador = 0
def BinarySearch(arr,query,start,end):

    global contador
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
        return medium + 1

    else:
        if(query > arr[medium]):
            print("if")
            print("query",query)
            print("arr[medium]",arr[medium])
            contador+=1
            if(contador < 5):
                return BinarySearch(arr,query,medium+1,end)
            else:
                print("omg")
        else:
            print("else")
            print("query",query)
            print("arr[medium]",arr[medium])
            contador+=1
            if(contador < 5):
                return  BinarySearch(arr,query,start,medium-1)
            else:
                print("omg")
            #return BinarySearch(arr,query,start,medium)


lista = [1,2,3,4,5,6,7,11,448]

index = BinarySearch(lista,448,0, (len(lista)-1) )
print(index)