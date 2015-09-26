import pygame
import sys
from pygame.locals import *


def main():
    
    screen = pygame.display.set_mode((1366,768),pygame.FULLSCREEN)
    pygame.display.set_caption('WordzZap')
    FPS=60
    clock=pygame.time.Clock()
    
    backglist=['./Assets/layer_1.png','./Assets/layer_2.png','./Assets/layer_3.png']
    
    backg = []
    
    character = pygame.image.load('./Assets/1.png')
    
    board=pygame.image.load('./Assets/board1.png')
    
    for img in backglist:
        backg.append(pygame.image.load(img))
    
    backg[2]=pygame.transform.scale(backg[2],(1366,683))
    
    while True:
        
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==  K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        screen.fill((255,255,255))
        screen.blit(board,(40,600))
        screen.blit(character,(100,608))
        
        screen.blit(backg[2],(0,768-683))
        clock.tick(FPS)
        pygame.display.update()
        
        
        
if __name__=="__main__":
    main()