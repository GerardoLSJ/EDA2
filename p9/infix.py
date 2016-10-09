lista = [0, 67, 27, 28, 79, 72, 14, 48]


def infix(i):
    global lista
    if(len(lista)-1 >= 2*i):

        if(lista[i] != None):
            if(lista[2*i != None]):
                infix(2*i)
            
            print lista[i]

            if(lista[2*i +1] != None):
                infix(2*i+1)

    else:
        print lista[i]


infix(1)


def prefix(i):
    global lista
    if(len(lista)-1 >= 2*i):

        if(lista[i] != None):
            if(lista[2*i != None]):
                print lista[i]
                infix(2*i)
            
            

            if(lista[2*i +1] != None):
                print lista[i]
                infix(2*i+1)

    else:
        print None

#prefix(1)

def posfix(i):
    global lista
    if(len(lista)-1 >= 2*i):

        if(lista[i] != None):
            if(lista[2*i != None]): #Tiene izquierdo?
                print lista[i]
                prefix(2*i)
            
            

            if(lista[2*i +1] != None):
                print lista[2*i +1]
                posfix(2*i+1)

    else:
        print None

#posfix(1)