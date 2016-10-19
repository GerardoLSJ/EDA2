
# -*- coding: utf-8 -*-
import os

def createDirectory(ruta):
    try:
        os.makedirs(ruta)
    except OSError as e:
        print('e')

    os.chdir(ruta)


createDirectory('/users/edaII08/edaII08alu23/Escritorio/EDA2/p10/')
dic = {}
a = open('hola.txt','r')
l = a.readlines()

for line in l:
    line = line.replace('\n','').split()
    for word in line:
        if word not in dic.keys():
            dic[word] = 1
        else:
            dic[word] += 1

print dic
print sorted(dic.items(), key=lambda x: x[1])
'''
print line[0]
print line[1]
dic['hola'] = 1
print dic['hola']
dic['hola'] +=1
print dic['hola']
'''
