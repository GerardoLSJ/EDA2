#Import library for stdin 
import sys

for linea in sys.stdin:
    linea = linea.replace("[","").replace("]","").split(",")
    print (linea)
