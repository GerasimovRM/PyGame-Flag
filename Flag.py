import pygame


pygame.init()
screen = pygame.display.set_mode((300, 500))

pygame.draw.rect(screen, pygame.Color("#D2691E"), [(30, 20), (10, 450)])
pygame.draw.rect(screen, pygame.Color("#D2691E"), [(20, 470), (30, 10)])
pygame.draw.rect(screen, pygame.Color("blue"), [(40, 70), (250, 50)])

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()