import pygame,sys
import random

from seacow import Cow
pygame.init()
height = 600
width = 800
surface = pygame.display.set_mode((width, height))
black = (0,0,0)

seacow = Cow()
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(seacow)
pos = seacow.getposi()

while True:
    color = []
    for x in range(3):
        col = random.randint(1,255)
        color.append(col)
    surface.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and (seacow.rect.x + pos[1]) < width:
                seacow.move('r')
            elif event.key == pygame.K_LEFT and (seacow.rect.x) > 0:
                seacow.move('l')
            elif event.key == pygame.K_UP and (seacow.rect.y) > 0:
                seacow.move('u')
            elif event.key == pygame.K_DOWN and (seacow.rect.y + pos[0]) < height:
                seacow.move('d')
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    all_sprites_list.update()
    all_sprites_list.draw(surface)
    pygame.display.flip()

    
