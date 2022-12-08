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
            if laberinto[m][n+1] == ' ' and solucion[-1]!='Izquierda': #Misma fila, una columna a la derecha, y que el anterior no sea izquierda
                solucion.append('Derecha')
                n += 1 #Avanzar a la derecha
            elif laberinto[m+1][n] == ' ' and solucion[-1]!='Arriba': #Una fila abajo, misma columna, y que el anterior no sea arriba
                solucion.append('Abajo')
                m += 1 #Avanzar hacia abajo
            elif laberinto[m][n-1] == ' ' and solucion[-1]!='Derecha': #Misma fila, una columna a la izquierda, y que el anterior no sea derecha
                solucion.append('Izquierda')
                n -= 1 #Avanzar a la izquierda
            else: #Una fila arriba, misma columna
                solucion.append('Arriba')
                m -= 1 #Avanzar hacia arriba
        elif laberinto[m][n] == 'S':
            solucion.append('Abajo')
        else:
            solucion.append('No hay solución')
    return solucion
# Mostrar por pantalla la lista de movimientos
print('Solución: ', recorrer_laberinto(laberinto))
