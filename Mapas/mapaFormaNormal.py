import pygame
import sys

pygame.init()

# Ventana
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simulación de mi pantalla")

reloj = pygame.time.Clock()

# Colores
FONDO = (166, 132, 128)
GRIS = (90, 90, 90)
VERDE = (40, 170, 50)
BLANCO = (245, 245, 245)
NEGRO = (20, 20, 20)

ejecutando = True

while ejecutando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.fill(FONDO)

    # =====================================================
    # MAPA
    # Cada cuadrado mide 30 x 30
    # =====================================================

    # -----------------------------------------------------
    # FILA 1
    # -----------------------------------------------------

    pygame.draw.rect(pantalla, GRIS, (50, 100, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (80, 100, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (110, 100, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (140, 100, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (170, 100, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (200, 100, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (230, 100, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (260, 100, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (290, 100, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (320, 100, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (350, 100, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (380, 100, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (410, 100, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (440, 100, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (470, 100, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (500, 100, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (530, 100, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (560, 100, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (590, 100, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (620, 100, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (650, 100, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (680, 100, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (710, 100, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (740, 100, 30, 30))

    # -----------------------------------------------------
    # FILA 2
    # -----------------------------------------------------

    pygame.draw.rect(pantalla, GRIS, (50, 130, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (80, 130, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (110, 130, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (140, 130, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (170, 130, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (200, 130, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (230, 130, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (260, 130, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (290, 130, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (320, 130, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (350, 130, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (380, 130, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (410, 130, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (440, 130, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (470, 130, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (500, 130, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (530, 130, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (560, 130, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (590, 130, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (620, 130, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (650, 130, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (680, 130, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (710, 130, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (740, 130, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (770, 130, 30, 30))

    # -----------------------------------------------------
    # FILA 3
    # -----------------------------------------------------

    pygame.draw.rect(pantalla, GRIS, (50, 160, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (80, 160, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (110, 160, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (140, 160, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (170, 160, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (200, 160, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (230, 160, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (260, 160, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (290, 160, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (320, 160, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (350, 160, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (380, 160, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (410, 160, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (440, 160, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (470, 160, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (500, 160, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (530, 160, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (560, 160, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (590, 160, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (620, 160, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (650, 160, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (680, 160, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (710, 160, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (740, 160, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (770, 160, 30, 30))

    # -----------------------------------------------------
    # FILA 4
    # -----------------------------------------------------

    pygame.draw.rect(pantalla, GRIS, (50, 190, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (80, 190, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (110, 190, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (140, 190, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (170, 190, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (200, 190, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (230, 190, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (260, 190, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (290, 190, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (320, 190, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (350, 190, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (380, 190, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (410, 190, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (440, 190, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (470, 190, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (500, 190, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (530, 190, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (560, 190, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (590, 190, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (620, 190, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (650, 190, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (680, 190, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (710, 190, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (740, 190, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (770, 190, 30, 30))

    # -----------------------------------------------------
    # FILA 5
    # -----------------------------------------------------

    pygame.draw.rect(pantalla, GRIS, (50, 220, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (80, 220, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (110, 220, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (140, 220, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (170, 220, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (200, 220, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (230, 220, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (260, 220, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (290, 220, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (320, 220, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (350, 220, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (380, 220, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (410, 220, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (440, 220, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (470, 220, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (500, 220, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (530, 220, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (560, 220, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (590, 220, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (620, 220, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (650, 220, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (680, 220, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (710, 220, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (740, 220, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (770, 220, 30, 30))

    # -----------------------------------------------------
    # FILA 6
    # -----------------------------------------------------

    pygame.draw.rect(pantalla, GRIS, (50, 250, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (80, 250, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (110, 250, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (140, 250, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (170, 250, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (200, 250, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (230, 250, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (260, 250, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (290, 250, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (320, 250, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (350, 250, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (380, 250, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (410, 250, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (440, 250, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (470, 250, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (500, 250, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (530, 250, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (560, 250, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (590, 250, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (620, 250, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (650, 250, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (680, 250, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (710, 250, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (740, 250, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (770, 250, 30, 30))

    # -----------------------------------------------------
    # FILA 7
    # -----------------------------------------------------

    pygame.draw.rect(pantalla, GRIS, (50, 280, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (80, 280, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (110, 280, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (140, 280, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (170, 280, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (200, 280, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (230, 280, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (260, 280, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (290, 280, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (320, 280, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (350, 280, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (380, 280, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (410, 280, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (440, 280, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (470, 280, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (500, 280, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (530, 280, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (560, 280, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (590, 280, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (620, 280, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (650, 280, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (680, 280, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (710, 280, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (740, 280, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (770, 280, 30, 30))

    # -----------------------------------------------------
    # FILA 8
    # -----------------------------------------------------

    pygame.draw.rect(pantalla, GRIS, (50, 310, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (80, 310, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (110, 310, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (140, 310, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (170, 310, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (200, 310, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (230, 310, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (260, 310, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (290, 310, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (320, 310, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (350, 310, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (380, 310, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (410, 310, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (440, 310, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (470, 310, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (500, 310, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (530, 310, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (560, 310, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (590, 310, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (620, 310, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (650, 310, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (680, 310, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (710, 310, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (740, 310, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (770, 310, 30, 30))

    # -----------------------------------------------------
    # FILA 9
    # -----------------------------------------------------

    pygame.draw.rect(pantalla, GRIS, (50, 340, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (80, 340, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (110, 340, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (140, 340, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (170, 340, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (200, 340, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (230, 340, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (260, 340, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (290, 340, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (320, 340, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (350, 340, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (380, 340, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (410, 340, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (440, 340, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (470, 340, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (500, 340, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (530, 340, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (560, 340, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (590, 340, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (620, 340, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (650, 340, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (680, 340, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (710, 340, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (740, 340, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (770, 340, 30, 30))

    # -----------------------------------------------------
    # FILA 10
    # -----------------------------------------------------

    pygame.draw.rect(pantalla, GRIS, (50, 370, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (80, 370, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (110, 370, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (140, 370, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (170, 370, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (200, 370, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (230, 370, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (260, 370, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (290, 370, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (320, 370, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (350, 370, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (380, 370, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (410, 370, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (440, 370, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (470, 370, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (500, 370, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (530, 370, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (560, 370, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (590, 370, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (620, 370, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (650, 370, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (680, 370, 30, 30))
    pygame.draw.rect(pantalla, BLANCO, (710, 370, 30, 30))
    pygame.draw.rect(pantalla, VERDE, (740, 370, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (770, 370, 30, 30))

    # -----------------------------------------------------
    # FILA 11
    # -----------------------------------------------------

    pygame.draw.rect(pantalla, GRIS, (50, 400, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (80, 400, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (110, 400, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (140, 400, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (170, 400, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (200, 400, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (230, 400, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (260, 400, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (290, 400, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (320, 400, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (350, 400, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (380, 400, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (410, 400, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (440, 400, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (470, 400, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (500, 400, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (530, 400, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (560, 400, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (590, 400, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (620, 400, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (650, 400, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (680, 400, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (710, 400, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (740, 400, 30, 30))
    pygame.draw.rect(pantalla, GRIS, (770, 400, 30, 30))


    # =====================================================
    # BORDE DE LOS CUADRADOS
    # =====================================================

    # Puedes quitar esta parte si no quieres líneas.

    for x in range(50, 801, 30):
        pygame.draw.line(pantalla, NEGRO, (x, 100), (x, 430), 1)

    for y in range(100, 431, 30):
        pygame.draw.line(pantalla, NEGRO, (50, y), (800, y), 1)


    pygame.display.flip()
    reloj.tick(60)


pygame.quit()
sys.exit()