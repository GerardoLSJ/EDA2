'''
try:
    a = open("/users/edaII08/edaII08alu23/Escritorio/EDA2/p10/hola.txt", "r")
    lista = a.readlines()
    print (lista)
except Exception as e:
    print("ERROR al leer")


print "continua el programa \n"
#/users/edaII08/edaII08alu23/Escritorio/EDA2/p10
'''

"""
with open ('hola.txt', 'r+') as archivo:
    for line in archivo:
        print(line)
"""

archivo = open('hola.txt','r+')
l = archivo.readlines()
print(l)
print archivo.tell()
archivo.seek(archivo.tell())
archivo.write("NUEVA", )
print archivo.tell()
