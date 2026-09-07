import pygame

pygame.init()
ventana = pygame.display.set_mode((800, 600))

fuente = pygame.font.SysFont("Arial", 48)
texto = fuente.render("Ivan Andres Gutierrez Vargas", True, (255, 255, 255))
rect = texto.get_rect(center=(400, 300))

ejecutando = True
while ejecutando:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            ejecutando = False

    ventana.fill((30, 30, 40))
    ventana.blit(texto, rect)
    pygame.display.flip()

pygame.quit()