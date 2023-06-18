#Pygame
import random

import pygame
pygame.init()
blue=(0,0,255)
red=(255,0,0)
white=(255,255,255)
bleck=(0,0,0)
dis = pygame.display.set_mode((800, 500))

pygame.display.set_caption('snake')
game_over= False
x_1=100
y_1=400

x_1_change=0
y_1_change=0
clock=pygame.time.Clock()
wind_size=pygame.display.get_window_size()
apple_x=random.randrange(0,wind_size[0],10)
apple_y=random.randrange(0,wind_size[1],10)
obstacle_x=random.randrange(0,wind_size[0],10)
obstacle_y=random.randrange(0,wind_size[1],10)
score = 0 #cчетчики яблок
score_1=0 #cчетчики яблок
score_2=0 #cчетчики яблок
font = pygame.font.Font(None,18)
eating_sound = pygame.mixer.Sound('499fe33297885e4.mp3') # создал переменную со звуком для еды
game_over_sound = pygame.mixer.Sound('game_over.mp3')#создал переменную со звуком для конец игры

len_s=[]# список координат всех точек змейки
m = 1 #длинна змейки
sped=8 #создал переменную для скорости змейки
while not game_over:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True

        if event.type==pygame.KEYDOWN:
            if event.key== pygame.K_LEFT:
                x_1_change=-10
                y_1_change=0
            if event.key== pygame.K_RIGHT:
                x_1_change=10
                y_1_change=0
            if event.key== pygame.K_UP:
                y_1_change=-10
                x_1_change=0
            if event.key== pygame.K_DOWN:
                y_1_change=10
                x_1_change=0
    if x_1 >=wind_size[0] or y_1>=wind_size[1] or x_1<=0 or y_1<=0:
        game_over=True
        sped=1# притормозил скорость кадров для прослушивания трека конец игры
        game_over_sound.play()# прослушивание трека конец игры

    x_1+=x_1_change
    y_1+=y_1_change


    dis.fill(white)
    nadpis = font.render('Съедено яблок: ' + str(score), True, red)
    nadpis_1=font.render('Скорость: ' + str(sped), True, red)
    dis.blit(nadpis, (10, 10))
    dis.blit(nadpis_1,(680,10)) # размещение надписи со скоростью


    head=[] # создал список для координат положения головы змейки
    head.append(x_1) # добавил в список координату х
    head.append(y_1) # добавил в список координату у
    len_s.append(head) # добавил список координат головы в список длинны змейки
    print(len_s)
    if len(len_s) > m: # если длинна списка с координатами змейки больше длинны змейки, удаляем первую координату
        del len_s[0]

    for x in len_s:
        pygame.draw.rect(dis, blue, [x[0], x[1], 10, 10])# проходим циклом по списку списков координат, и создаем по координатам змейку

    pygame.draw.rect(dis,red,[apple_x,apple_y,10,10]) # создаю рандомное яблоко
    pygame.display.update()
    if score_2>2:
        pygame.draw.rect(dis, bleck, [obstacle_x, obstacle_y, 30, 30])#создал препятствие
        pygame.display.update()

    if x_1 in range(obstacle_x,obstacle_x+30,10) and y_1 in range(obstacle_y,obstacle_y+30,10):
        game_over=True
        game_over_sound.play()#
    if len_s[-1] in len_s[0:-2]:
        game_over = True
        game_over_sound.play()#
    if x_1==apple_x and y_1==apple_y:
        score += 1 # если змейка съела яблоко уаеличиваем количество съеденых яблок
        score_1+=1 # Увеличиваем счетчик съеденых яблок для повышения скорости
        score_2+=1
        m+=1
        eating_sound.play()
        if score_1==2: #  с каждым второым яблоком
            sped+=1#увеличиваю скорость
            score_1=0 # обнуляю счетчик


        apple_x = random.randrange(0, wind_size[0], 10)
        apple_y = random.randrange(0, wind_size[1], 10)


    clock.tick(sped)

pygame=quit()
quit()




