def radix(l):
    max = 0
    for i in l:
        if(len(i) > max ):
            max = len(i)
    for i in range(len(l)):                         #normalizar la cadena ceros en decimas centenas etc
        while(len(l[i]) < max):
            l[i] = l[i]+chr(96)                     #123  #Normalizar por la derecha!

    for j in range(max-1,-1,-1):                    #max-1 hasta -1 en incrementos de -1
        ocu = [ 0 for i in range(0,28) ]


        for i in range(len(l)):

            ocu[ int(ord(l[i][j])-96 ) ] +=1

          					
        
        for i in range(0,27):
            ocu[i+1] = ocu[i] + ocu[i+1]

        
        s = [0 for i in range(len(l))]
        
        for i in range(len(l)-1,-1,-1):
            ocu[ int(ord(l[i][j]) -96) ] -=1
            s[ ocu[ int(ord(l[i][j]) -96) ] ] = l[i]
        l=s


    return l 
                                

test1 = ['do','l','r','r','s','wf','hf','sy','fj','wr' ]

arr = radix(test1)
arr = list(map(lambda x: x.replace(chr(96),"") , arr))   #Borramos las " chr(96) " que agregamos para normalizar
print(arr)
