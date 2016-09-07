import sys

def radix(l):
    max = 0
    for i in l:
        if(len(i) > max ):
            max = len(i)
    for i in range(len(l)):   #normalizar la cadena ceros en decimas centenas etc
        while(len(l[i]) < max):
            l[i] = "0"+l[i]

    

    for j in range(max-1,-1,-1): #max-1 hasta -1 en incrementos de -1
        ocu = [ 0 for i in range(10) ]
        for i in range(len(l)):
            ocu[ int(l[i][j]) ] +=1					#cast y ...accedemos a "123" luego al "3"
        
        for i in range(9):
            ocu[i+1] = ocu[i] + ocu[i+1]
        
        s = [0 for i in range(len(l))]
        
        for i in range(len(l)-1,-1,-1):
            ocu[ int(l[i][j]) ] -=1
            s[ ocu[ int(l[i][j]) ] ] = l[i]
        l=s
        

    return l 



line = ["10000000000","0000744444444444444444444442","4","8177","57","8","87","78","73"]
result = radix(line)
result = list(map(int, result))     #MAP string to int of the result 
print (result)                               
""" 
for line in sys.stdin:
    line = line.replace('[','')
    line = line.replace(']','')
    line = line.split(',')
    result = (radix(line))
    result = list(map(int, result))     #MAP string to int of the result 
    print (result)
"""