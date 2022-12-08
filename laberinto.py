from datos import muro
#Laberinto
def laberinto(xy, muro): #Función que crea el laberinto(dimensión, muro)
    S = (4,4) #Coordenadas de la S
    laberinto = [] #Lista vacía del laberinto
    for x in range(5):
        filas=[]
        for y in range(xy): #Recorre las filas
            if (x,y) in muro:
                filas.append('X') #Si la coordenada está en muro, agrega una X
            elif (x,y) == S: #Si la coordenada es igual a S, agrega una S
                filas.append('S')
            elif (x,y) == (0,0): #Si la coordenada es igual a (0,0), agrega una E
                filas.append('E')
            else:
                filas.append(' ')
        laberinto.append(filas)
    return laberinto

laberinto_deseado = laberinto(5, muro)
#Función que muestra el laberinto
def laberinto_impreso(laberinto_deseado):
    for x in laberinto_deseado:
        print(''.join(x))
