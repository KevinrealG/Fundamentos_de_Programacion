import pygame #libreria para crear juegos
import numpy as np #libreria para trabajar con matrices y operaciones matematicas
import time #libreria para incluir funciones de control temporal

# Para comenzar vamos a crear la pantalla de nuestro juego
pygame.init()
#largo y ancho de 400x400 pixeles
width, height = 600, 400
#bg es para darle el color de fondo del juego (background)
bg = 25, 25 ,25
#pygame.display.set_mode para crear la ventana del juego
screen  = pygame.display.set_mode((height, width))
#llenar toda la ventana del juego con la variable bg
screen.fill(bg)

# Número de celdas
nxC, nyC = 60, 60

# se crea una matriz con el Estado de las celdas vivas tendran un valor de 1. Viva = 1 / Muerta = 0
gameState = np.zeros((nxC,  nyC)) # np.zeros para que empieze con un valor de 0 dentro del parametro de X y Y

#haremos que el juego empiece con algunas celdas vivas en un grupo de interacciones, 
#Esto es para determinar el tamaño de las celdas, que es el alto entre el total de celdas y el ancho entre el total de celdas
dimCW = width / nxC
dimCH = height / nyC

#Línea 3×1: Rota en 45º en cada iteración (Oscila)
# Oscilador.
gameState[38, 20] = 1
gameState[39, 20] = 1
gameState[40, 20] = 1

#El corredor: uson 5 celdas vivas que se desplaza en diagonal por la matriz (naves espaciales).
# Runner 1
gameState[10,5] = 1
gameState[12,5] = 1
gameState[11,6] = 1
gameState[12,6] = 1
gameState[11,7] = 1

#Runner 2
gameState[5,10] = 1
gameState[5,12] = 1
gameState[6,11] = 1
gameState[6,12] = 1
gameState[7,11] = 1

#Caja 2×2: Es invariable en el tiempo (vidas estáticas)
#Box 1
gameState[18,15] = 1
gameState[17,16] = 1
gameState[17,15] = 1
gameState[18,16] = 1

#Serpent 1
gameState[30,20] = 1
gameState[31,20] = 1
gameState[32,20] = 1
gameState[32,19] = 1
gameState[33,19] = 1
gameState[34,19] = 1

#permitirá controlar desde el teclado la ejecución o pausa de nuestro sistema, y empezara sin pausa
pauseExect = False

# Bucle de ejecución
while True:

    # Copiamos la matriz del estado anterior
    # para representar la matriz en el nuevo estado
    newGameState = np.copy(gameState)

    # Ralentizamos la ejecución a 0.1 segundos
    time.sleep(0.1)

    # Limpiamos la pantalla
    screen.fill(bg)

    # Registramos eventos de teclado y ratón.
    ev = pygame.event.get()

    # Cada vez que identificamos un evento lo procesamos
    for event in ev:
        # Detectamos si se presiona una tecla.
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect

        # Detectamos si se presiona el ratón.
        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = 1

#el bucle for es para que recorran todas las celdas en el eje X y Y, y se muestren
    for y in range(0, nxC):
        for x in range (0, nyC):

            if not pauseExect:

                # Calculamos el número de vecinos cercanos.
                n_neigh =   gameState[(x - 1) % nxC, (y - 1)  % nyC] + \
                            gameState[(x)     % nxC, (y - 1)  % nyC] + \
                            gameState[(x + 1) % nxC, (y - 1)  % nyC] + \
                            gameState[(x - 1) % nxC, (y)      % nyC] + \
                            gameState[(x + 1) % nxC, (y)      % nyC] + \
                            gameState[(x - 1) % nxC, (y + 1)  % nyC] + \
                            gameState[(x)     % nxC, (y + 1)  % nyC] + \
                            gameState[(x + 1) % nxC, (y + 1)  % nyC]

                # Regla #1 : Una celda muerta con exactamente 3 vecinas vivas, "revive".

                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1

                # Regla #2 : Una celda viva con menos de 2 o más 3 vecinas vinas, "muere".

                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0

            #Poly (poligono) se defeniera con las siguientes 4
            poly = [((x)   * dimCW, y * dimCH),
                    ((x+1) * dimCW, y * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x)   * dimCW, (y+1) * dimCH)]

            # Si la celda está "muerta" pintamos un recuadro con borde gris
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (40, 40, 40), poly, 1)
           # Si la celda está "viva" pintamos un recuadro relleno de color
            else:
                pygame.draw.polygon(screen, (200, 100, 100), poly, 0)

    # Actualizamos el estado del juego.
    gameState = np.copy(newGameState)

    # Mostramos el resultado
    pygame.display.flip()