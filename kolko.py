import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 102)

dis_width = 600
dis_height  = 400


dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('plus i minus to jedyne co widze')

clock = pygame.time.Clock()

def pole(rozmiar, szerokość, wysokość):
    x=40
    y=40

    for i in range(wysokość):
        x=40
        for s in range(szerokość):
            pygame.draw.rect(dis, white, [x, y, rozmiar, rozmiar], 1)
            x+=rozmiar

        y+=rozmiar

while True:
    pole(50, 4, 5)
    pygame.display.update()

