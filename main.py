import pygame


pygame.init()

pygame.display.set_caption("Solar System Viewer")
screen = pygame.display.set_mode((900,900))

while True:
    screen.fill(255)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()