def radix(l):
    max = 0
    for i in l:
        if(len(i) > max ):
            max = len(i)
    for i in range(len(l)):                         #normalizar la cadena ceros en decimas centenas etc
        while(len(l[i]) < max):
            l[i] = "0"+l[i]


    for j in range(max-1,-1,-1):                    #max-1 hasta -1 en incrementos de -1
        ocu = [ 0 for i in range(0,200) ]
        for i in range(len(l)):
            print (l[i][j])
            print ord(l[i][j])
            ocu[ int(ord(l[i][j])) ] +=1					#cast y ...accedemos a "123" luego al "3"
        
        for i in range(9):
            ocu[i+1] = ocu[i] + ocu[i+1]
        
        s = [0 for i in range(len(l))]
        
        for i in range(len(l)-1,-1,-1):
            ocu[ int(ord(l[i][j])) ] -=1
            s[ ocu[ int(ord(l[i][j])) ] ] = l[i]
        l=s
        print ocu

    return l 
                                

#modificaciones para que acomode cadenas de letras TODAS MAYUS aplicar UPPERCASE 
"""
Mapreamos el codigo ASCII, acomodamos y luego volvemos a covneritr 
[aaa,aab,abc]
"""
print( radix(["aaa","bbb","abc","aab","aeiou"]))
