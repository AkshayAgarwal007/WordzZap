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
    
    board=pygame.image.load('./Assets/board1.png')
    
    for img in backglist:
        backg.append(pygame.image.load(img))
    
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
        screen.blit(board,(40,40))
        clock.tick(FPS)
        pygame.display.update()
        
        
        
if __name__=="__main__":
    main()