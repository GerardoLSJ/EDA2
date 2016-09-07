import sys

def BinarySearch(arr,query,start,end):
    if(start > end):
        print("False")
        return False

    medium = int((end - start)/2) + start

    arrInt = int(arr[medium][0])
    if(arrInt == query):
        return medium

    else:
        arrInt = int(arr[medium][0])
        if(query > arrInt):
            return BinarySearch(arr,query,medium+1,end)

        else:
            return  BinarySearch(arr,query,start,medium-1)
                      
query = ""
lista_alumnos = []
for linea in sys.stdin:
    
    tupla = linea.split("\t")
    if(query == ""):
        query = tupla[0].replace("\n","")
    
    else:
        tupla[2] = tupla[2].replace("\n","")
        lista_alumnos.append(tupla)

        
lista = lista_alumnos #Beautify code 
index = BinarySearch(lista,int(query),0, (len(lista)-1) )
print(lista[index])