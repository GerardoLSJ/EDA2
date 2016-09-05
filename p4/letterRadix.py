def radix(l):
    max = 0
    for i in l:
        if(len(i) > max ):
            max = len(i)
    for i in range(len(l)):                         #normalizar
        while(len(l[i]) < max):
            l[i] = l[i]+chr(96)                     #Normalizar por la derecha
                                                    #coon el char 96 
    for j in range(max-1,-1,-1):                    
        ocu = [ 0 for i in range(0,28) ]        # arr de 28 por el alfabeto


        for i in range(len(l)):

            ocu[ int(ord(l[i][j])-96 ) ] +=1    #para ocupar la localidad 1
                                                # con la 'a' le restamos 96
          					
        
        for i in range(0,27):                   #suma de parciales
            ocu[i+1] = ocu[i] + ocu[i+1]

        
        s = [0 for i in range(len(l))]
        
        for i in range(len(l)-1,-1,-1):         #acomodo en arreglo parcial
            ocu[ int(ord(l[i][j]) -96) ] -=1
            s[ ocu[ int(ord(l[i][j]) -96) ] ] = l[i]
        l=s


    return l 
                                

test1 = ['do','l','r','r','s','wf','hf','sy','fj','wr' ]

arr = radix(test1)
arr = list(map(lambda x: x.replace(chr(96),"") , arr))  #Borramos las "chr(96) "
print(arr)                                              #que agregamos para normalizar
