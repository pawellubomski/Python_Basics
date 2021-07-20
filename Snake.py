import pygame
import random


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue=(0,0,255)
yellow = (255, 255, 102)
green = (0, 255, 0)

dis_width = 600
dis_height  = 400


dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Grajmy sobie w snejka')

clock = pygame.time.Clock()

wymiarsnejka = 10 #wielkość wężą

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def naszwąż(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

def wiadomosc (wiad,clr,wysokosc):
    wiad = font_style.render(wiad, True, clr)
    dis.blit(wiad, [int(dis_width / 3), int(dis_height / 3)+wysokosc])

def gejmLoop():
    game_over = False
    game_close = False
    game_samoboj = False
    x1 = int(dis_width / 2)
    y1 = int(dis_height / 2)

    x1_change = 0
    y1_change = 0

    snake_List = []
    długośćwęża = 1
    szybkoscweza=15
    illegal_move=0

    foodx = round(random.randrange(0, dis_width - wymiarsnejka) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - wymiarsnejka) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(white)
            if game_samoboj:
                wiadomosc("Samobój!", black,0)
            else:
                wiadomosc("Ściana!", black, 0)
            wiadomosc("Naciśnij Q by wyjść", red, 50)
            wiadomosc("lub C by zagrać ponownie", blue, 100)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gejmLoop()
                if event.type == pygame.QUIT:
                    quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and event.key!=illegal_move:
                    x1_change = -wymiarsnejka
                    y1_change = 0
                    illegal_move=pygame.K_RIGHT
                elif event.key == pygame.K_RIGHT and event.key!=illegal_move:
                    x1_change = wymiarsnejka
                    y1_change = 0
                    illegal_move=pygame.K_LEFT
                elif event.key == pygame.K_UP and event.key!=illegal_move:
                    y1_change = -wymiarsnejka
                    x1_change = 0
                    illegal_move=pygame.K_DOWN
                elif event.key == pygame.K_DOWN and event.key!=illegal_move:
                    y1_change = wymiarsnejka
                    x1_change = 0
                    illegal_move=pygame.K_UP
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: #jeśli przesunięcie snejka na x >= szerokości lub pozycja snejka na x < 0 i tak samo y to game over
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, blue, [foodx, foody, wymiarsnejka, wymiarsnejka])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len (snake_List) > długośćwęża:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_head:
                game_close=True
                game_samoboj=True
        naszwąż(wymiarsnejka, snake_List)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - wymiarsnejka) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - wymiarsnejka) / 10.0) * 10.0
            długośćwęża += 1
            szybkoscweza += 5

        clock.tick(szybkoscweza)


    pygame.quit()
    quit()
gejmLoop()


