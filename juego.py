import pygame
import sys
import random

#Dimensiones de la ventana
ancho = 800
alto = 600

ventana = pygame.display.set_mode((ancho,alto))

#Color del jugador
colorRojo = (255,0,0)
#Color de la ventana
colorNegro = (0,0,0,0)
#Color enemigos 
colorAzul = (0,0,255)

#Valores del jugador
posicionJugador = [350,500]
dimensionJugador = 50

gameOver = False
clock = pygame.time.Clock()

def detectarColision(posicionJugador, posicionEnemigo):
    jx = posicionJugador[0]
    jy = posicionJugador[1]
    ex = posicionEnemigo[0]
    ey = posicionEnemigo[1]

    if (ex >= jx and ex < (jx + dimensionJugador)) or (jx >= ex and jx <(ex + dimensionEnemigo)):
        if (ey >= jy and ey < (jy + dimensionJugador)) or (jy >= ey and jy <(ey + dimensionEnemigo)):
            return True
    return False
        
#Valores enemigos
dimensionEnemigo = 50
posicionEnemigo =[random.randint(0,ancho - dimensionEnemigo),0]

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            x = posicionJugador[0]
            if event.key == pygame.K_LEFT:
                x -= dimensionJugador
            if event.key == pygame.K_RIGHT:
                x += dimensionJugador
            posicionJugador[0] = x 
    ventana.fill(colorNegro )
    if posicionEnemigo[1] >= 0 and posicionEnemigo[1] < alto:
        posicionEnemigo[1] += 20
    else:
        posicionEnemigo[0] = random.randint(0,ancho - dimensionEnemigo)
        posicionEnemigo[1] = 0

    #Colisiones
    if detectarColision(posicionJugador,posicionEnemigo):
        gameOver = True
    #Dibujar enemigo (Azul)
    pygame.draw.rect(ventana,colorAzul,(posicionEnemigo[0],posicionEnemigo[1],dimensionEnemigo,dimensionEnemigo))

    #Dibujar jugador (Rojo)
    pygame.draw.rect(ventana,colorRojo,(posicionJugador[0],posicionJugador[1],dimensionJugador,dimensionJugador))
     
    clock.tick(30)
    pygame.display.update()
