import sys
import re
from operator import itemgetter
sys.setrecursionlimit(10000)
#el codigo de funes se lu quitaron funcionnes pero se dejo en su ejecucion la funcion cuenta_palabras, por lo tanto al ejecutar funes() 
#dirá el número de palabras
def cuenta_palabras(dicc):
    if len(dicc) > 0:
        respaldo_nombre,frecuencia = dicc.popitem()
        cantidad = frecuencia
        return cantidad + cuenta_palabras(dicc)
    else:
        return 0
 
def funes():
    f = open("funes.txt","r",encoding='utf-8')
    respaldo = f.read()
    respaldo=respaldo.lower()
    l = respaldo.split()
    dicc = {}
    dicc = dict.fromkeys(l,0)
    for palabra in l:
        if palabra in dicc:
            dicc[palabra]=int(dicc[palabra]+1)
    print("El número de palabras del texto es :",cuenta_palabras(dicc))
    f.close()
 

