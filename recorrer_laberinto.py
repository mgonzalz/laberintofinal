from datos import *
'''
    ['E', 'X', 'X', 'X', 'X'], 
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '], 
    [' ', ' ', ' ', 'X', ' '], 
    ['X', 'X', 'X', 'X', 'S']
'''
def recorrer_laberinto(laberinto):
    # Fila y columnas iniciales
    m = 0
    n = 0
    movimientos = ['Abajo'] # Movimiento inicial
    tam = len(laberinto) # Tamaño del laberinto
    while m < tam-1 and n < tam-1: # Mientras no llegue al final
        if m + 1 < n and laberinto[m + 1][n] != 'X': # Movimiento anterior NO arriba; Fil+1 NO pared= ABAJO
            m += 1 #Movimiento cuando es derecha
            movimientos.append('Abajo')
        elif m - 1 > 0 and laberinto[m - 1][n] != 'X':
            m -= 1 #Movimiento cuando es arriba
            movimientos.append('Arriba')
        elif laberinto[m][n + 1] != 'X':
            n += 1 #Movimiento cuando es derecha
            movimientos.append('Derecha')
        else:
            n -= 1 #Movimiento cuando es izquierda
            movimientos.append('Izquierda')
    print(movimientos)
if __name__ == '__main__':
    recorrer_laberinto(laberinto)
