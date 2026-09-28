import pygame
import sys

pygame.init()

# Ventana
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mapa de Bomberman")

reloj = pygame.time.Clock()

# Colores
FONDO = (166, 132, 128)
LIBRE = (245, 245, 245)
INDESTRUCTIBLE = (90, 90, 90)
DESTRUCTIBLE = (40, 170, 50)
NEGRO = (20, 20, 20)

# 25 columnas x 11 filas
# 0 = libre
# 1 = indestructible
# 2 = destructible

mapa = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],

    [1,0,2,2,0,2,0,0,2,0,2,0,2,0,2,0,0,2,0,2,2,0,1],

    [1,2,0,1,2,0,1,2,0,1,0,0,0,1,0,2,1,0,2,1,0,2,1],

    [1,0,2,0,2,2,0,2,2,0,2,2,2,0,2,2,0,2,2,0,2,0,1],

    [1,2,0,2,0,0,2,0,0,2,0,2,0,2,0,0,2,0,0,2,0,2,1],

    [1,2,0,1,0,1,2,0,1,0,0,1,0,0,1,0,2,1,0,1,0,2,1],

    [1,0,2,0,2,0,2,2,0,2,2,0,2,2,0,2,2,0,2,0,2,0,1],

    [1,2,0,2,0,2,0,2,2,0,0,0,0,0,2,2,0,2,0,2,0,2,1],

    [1,0,2,1,2,0,1,2,0,1,2,0,2,1,0,2,1,0,2,1,2,0,1],

    [1,2,0,0,2,2,0,0,2,0,2,2,2,0,2,0,0,2,2,0,0,2,1],

    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

# Tamaño de cada cuadrado
TAM = 28

# Posición del mapa en la pantalla
MAPA_X = 50
MAPA_Y = 140


ejecutando = True

while ejecutando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Fondo
    pantalla.fill(FONDO)

    # Dibujar mapa
    for fila in range(len(mapa)):
        for columna in range(len(mapa[fila])):

            tipo = mapa[fila][columna]

            x = MAPA_X + columna * TAM
            y = MAPA_Y + fila * TAM

            if tipo == 0:
                color = LIBRE

            elif tipo == 1:
                color = INDESTRUCTIBLE

            elif tipo == 2:
                color = DESTRUCTIBLE

            pygame.draw.rect(
                pantalla,
                color,
                (x, y, TAM, TAM)
            )

            # Borde de cada cuadrado
            pygame.draw.rect(
                pantalla,
                NEGRO,
                (x, y, TAM, TAM),
                width=1
            )

    pygame.display.flip()
    reloj.tick(60)


pygame.quit()
sys.exit()