def radix(l):
    max = 0
    for i in l:
        if(len(i) > max ):
            max = len(i)
    for i in range(len(l)):                         #normalizar la cadena ceros en decimas centenas etc
        while(len(l[i]) < max):
            l[i] = chr(123)+l[i]


    for j in range(max-1,-1,-1):                    #max-1 hasta -1 en incrementos de -1
        ocu = [ 0 for i in range(0,28) ]


        for i in range(len(l)):
            #print (l[i][j])
            #print( chr(96) )
            #print (ord("z") )
            ocu[ int(ord(l[i][j])-96 ) ] +=1
            #print(ocu)
          					
        
        for i in range(0,27):
            ocu[i+1] = ocu[i] + ocu[i+1]
            #print(i,ocu)
        
        s = [0 for i in range(len(l))]
        
        for i in range(len(l)-1,-1,-1):
            ocu[ int(ord(l[i][j]) -96) ] -=1
            s[ ocu[ int(ord(l[i][j]) -96) ] ] = l[i]
        l=s
        #print( ocu)

    return l 
                                

#modificaciones para que acomode cadenas de letras TODAS MAYUS aplicar UPPERCASE 
"""
Mapreamos el codigo ASCII, acomodamos y luego volvemos a covneritr 
[aaa,aab,abc]
"""

#SOLO ORDENA CUANTO HAY LE MISMO NUMERO DE CARACTERES 
print( radix(["zaz","bbx","aba","aab","aei"]))       



#print (radix ( ['do','l','r','r','s','wf','hf','sy','fj','wr' ]))



'''
            zero = int((l[i][j])
            
            if(True ):
                print("twf")
                ocu[0] +=1     

            else:    

'''