import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 600
screen_height = 300

#COLOR
white = (255,255,255)

#Font
font = pygame.font.SysFont('Calibri', 25, True, False)
Font = pygame.font.SysFont('Calibri', 12, True, False)

run = True


def update():
    clock.tick(fps)
    pygame.display.update()
