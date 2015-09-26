import pygame
import sys
from pygame.locals import *


def main():
    
    screen = pygame.display.set_mode((1366,768),pygame.FULLSCREEN)
    pygame.display.set_caption('WordzZap')
    FPS=120
    clock=pygame.time.Clock()
    
    backglist=['./Assets/layer_1.png','./Assets/layer_2.png','./Assets/layer_3.png']
    
    backg = []
    
    character = pygame.image.load('./Assets/1.png')
    character.convert_alpha()
    
    board=pygame.image.load('./Assets/board1.png')
    board.convert_alpha()
    
    for img in backglist:
        backg.append(pygame.image.load(img))
        
    
    backg[2]=pygame.transform.scale(backg[2],(1366,683))
    
    for img1 in backg:
        img1.convert_alpha()
    xb=40
    xc=110
    frames=0
    
    while True:
        
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key ==  K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        screen.fill((255,255,255))
        screen.blit(board,(xb,565))
        screen.blit(character,(xc,573))
        
        screen.blit(backg[2],(0,768-683))
        
        if frames%2==0:
            xb=xb+5
            xc=xc+5
        
        clock.tick(FPS)
        pygame.display.update()
        
        frames=frames+1
        
if __name__=="__main__":
    main()