from datos import *
'''
    ['E', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
'''
def recorrer_laberinto(laberinto):
    m = 0
    n = 0
    tam = len(laberinto)
    solucion = []
    while (m < tam-1 and n < tam-1): #Que no llegue al final
        if laberinto[m][n] == 'E':
            solucion.append('Abajo')
            m += 1 #Avanzar hacia abajo
        elif laberinto[m][n] == ' ': #Si es un espacio
            if laberinto[m][n+1] == ' ': #Misma fila, una columna a la derecha
                solucion.append('Derecha')
                n += 1 #Avanzar a la derecha
            elif laberinto[m+1][n] == ' ': #Una fila abajo, misma columna
                solucion.append('Abajo')
                m += 1 #Avanzar hacia abajo
            elif laberinto[m][n-1] == ' ': #Misma fila, una columna a la izquierda
                solucion.append('Izquierda')
                n -= 1 #Avanzar a la izquierda
            else: #Una fila arriba, misma columna
                solucion.append('Arriba')
                m -= 1 #Avanzar hacia arriba
    return solucion
# Mostrar por pantalla la lista de movimientos
print('Solución: ', recorrer_laberinto(laberinto))
