import pygame
import time

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 102)

dis_width = 600
dis_height  = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Grajmy sobie w pinkponk')

clock = pygame.time.Clock()

wymiar_piłki=10
wymiar_kloca = [60, 10,]

pozycja_kloca_1 = [dis_width/2, dis_height-wymiar_kloca[1]-10]
pygame.draw.rect(dis, white, [pozycja_kloca_1[0], pozycja_kloca_1[1], wymiar_kloca[0], wymiar_kloca[1]])
pozycja_kloca_2 = [dis_width/2, 10]
pygame.draw.rect(dis, white, [pozycja_kloca_2[0], pozycja_kloca_2[1], wymiar_kloca[0], wymiar_kloca[1]])

pozycja_piłki=[dis_width/2, dis_height/2]
pygame.draw.rect(dis, yellow, [pozycja_piłki[0], pozycja_piłki[1], wymiar_piłki, wymiar_piłki])
pygame.display.update()
x1_change=0
x2_change=0
font_style = pygame.font.SysFont("bahnschrift", 25)
def wiadomosc (wiad,clr,wysokosc):
    wiad = font_style.render(wiad, True, clr)
    dis.blit(wiad, [int(dis_width / 3), int(dis_height / 3)+wysokosc])
game_over=False
xp = 10
yp = 10
koniec_partii=False
# while True:
#     print("start")
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
while not game_over:
    if pozycja_piłki[1] > dis_height or pozycja_piłki[1] < 0:
        print(dis, white, "PUNKT!")
        pozycja_piłki=[dis_width/2, dis_height/2]
        koniec_partii=True
        continue
    if koniec_partii == True:
        wiadomosc("Nowa Partia, nacisnij C", white, 0)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                    koniec_partii=False
                    continue
            if event.type == pygame.QUIT:
                quit()
        continue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -wymiar_piłki

            elif event.key == pygame.K_RIGHT:
                x1_change = wymiar_piłki
            elif event.key == pygame.K_a:
                x2_change = -wymiar_piłki
            elif event.key == pygame.K_d:
                x2_change = wymiar_piłki
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x1_change = 0

            elif event.key == pygame.K_RIGHT:
                x1_change = 0
            elif event.key == pygame.K_a:
                x2_change = 0
            elif event.key == pygame.K_d:
                x2_change = 0

    if pozycja_piłki[1] >= pozycja_kloca_1[1]:
        if pozycja_kloca_1[0] + wymiar_kloca[0] >= pozycja_piłki[0] >= pozycja_kloca_1[0]:
            yp=-yp
    if pozycja_piłki[1] <= pozycja_kloca_2[1]:
        if pozycja_kloca_2[0] + wymiar_kloca[0] >= pozycja_piłki[0] >= pozycja_kloca_2[0]:
            yp=-yp
    if pozycja_piłki[0] <= 0:
        xp=-xp
    if pozycja_piłki[0] + wymiar_piłki >= dis_width:
        xp=-xp
    pozycja_piłki[0] += xp
    pozycja_piłki[1] += yp
    pozycja_kloca_1[0] += x1_change
    pozycja_kloca_2[0] += x2_change
    dis.fill(black)
    pygame.draw.rect(dis, white, [pozycja_kloca_1[0], pozycja_kloca_1[1], wymiar_kloca[0], wymiar_kloca[1]])

    pygame.draw.rect(dis, white, [pozycja_kloca_2[0], pozycja_kloca_2[1], wymiar_kloca[0], wymiar_kloca[1]])

    pygame.draw.rect(dis, yellow, [pozycja_piłki[0], pozycja_piłki[1], wymiar_piłki, wymiar_piłki])
    pygame.display.update()
    clock.tick(10)
    clock.tick(10)



pygame.display.update()
time.sleep(3)