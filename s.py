
import pygame, sys

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((400,600))

#creating objects of game
tamoto_img = pygame.image.load("tamoto.png.JPG").convert_alpha()
mushroom_img = pygame.image.load("mushroom.png.JPG").convert_alpha()
carrot_img = pygame.image.load("carrot.png.JPG").convert_alpha()
brinjals_img = pygame.image.load("brinjals.png.JPG").convert_alpha()
pumpkin_img = pygame.image.load("pumpkin.png.JPG").convert_alpha()

tomatoes=[]
mushrooms=[]
carrots=[]
brinjals=[]
pumpkins=[]

for i in range(1,6):
    tomatoes.append(pygame.Rect(i*60,100,40,40))
    mushrooms.append(pygame.Rect(i*60,200,40,40))
    carrots.append(pygame.Rect(i*60,300,40,40))

    brinjals.append(pygame.Rect(i*60,400,40,40))

    pumpkins.append(pygame.Rect(i*60,500,40,40))

while True:    
    screen.fill((30,80,20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
             
    for tomato in tomatoes:        
        #pygame.draw.rect(screen,(223,50,20),tomato)
        screen.bli("tomato.png",tomato)
    for mushroom in mushrooms:        
        #pygame.draw.rect(screen,(220,220,220),mushroom)
        screen.blit("mushroom.png",mushroom)
    for carrot in carrots:  
        #pygame.draw.rect(screen,(250,20,20),carrot)
        screen.bilt("carrots.png",carrot)
    for brinjal in brinjals:
        #pygame.draw.rect(screen,(150,50,220),brinjal)
        screen.blit("brinjals.png",brinjal)
    for pumpkin in pumpkins:
        #pygame.draw.rect(screen,(223,250,20),pumpkin)
        screen.blit("pumpkin.png",pumpkin)
            

    pygame.display.update()
    clock.tick(30)

