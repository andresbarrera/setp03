#la función mostrar_pascal es iterativa, pero la función tri_pascal es la recursiva pedida en el ejercicio.
def tri_pascal(n):
    if n == 0:
        return [1]
    else:
        fila_correspondiente = [ ]
        for cont in range(n+1):
            if cont == 0 or cont == n :
                fila_correspondiente = fila_correspondiente + [1]
            else:
                fila_correspondiente = fila_correspondiente + [ tri_pascal(n-1)[cont-1] + tri_pascal(n-1)[cont]]
    
    return  fila_correspondiente

def mostrar_pascal(n):
    cont = 0
    for i in range(n):
        print(tri_pascal(cont))
        cont=cont+1
