import pygame
from pygame.draw import *

pygame.init()


FPS = 30
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((400, 400))
screen.fill(WHITE)

# face
circle(screen, (0, 0, 0), (200, 200), 120, 2)
circle(screen, (255, 255, 0), (200, 200), 118)

# left
circle(screen, (0, 0, 0), (150, 160), 10)
circle(screen, (255, 0, 0), (150, 160), 25, 15)
circle(screen, (0, 0, 0), (150, 160), 25, 1)

# right
circle(screen, (0, 0, 0), (250, 160), 10)
circle(screen, (255, 0, 0), (250, 160), 20, 10)
circle(screen, (0, 0, 0), (250, 160), 20, 1)

line(screen, (0, 0, 0), [180, 200], [150, 180], 10)
pygame.draw.rect(screen, (0, 0, 0), [130, 250, 140, 20])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()