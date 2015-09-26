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
    
    character = pygame.image.load('./Assets/1.png').convert_alpha()
 
    
    board=pygame.image.load('./Assets/board1.png').convert_alpha()
        
    for img in backglist:
        backg.append(pygame.image.load(img).convert_alpha())
        
    
    backg[2]=pygame.transform.scale(backg[2],(1366,683))
    backg[0]=pygame.transform.scale(backg[0],(1366,683))
    
    imglist=[]

    for kp in range(0,4):
        imglist.append(pygame.image.load("PNG/frame-%s.png"%str(kp+1)).convert_alpha())
 
    for f in range(0,4):
        imglist[f]=pygame.transform.scale(imglist[f],(100,70))
        
  
    
    for img1 in backg:
        img1.convert_alpha()
    xb=40
    xc=110
    xp=0
    r=0
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
        screen.blit(backg[0],(0,0))
        
        
        
        screen.blit(backg[2],(0,768-683))
        
        screen.blit(board,(xb,565))
        screen.blit(character,(xc,573))
        
        
        if frames%10==0:

      
            r=r+1
            if r==4:
                r=0

        xp=xp+2
        screen.blit(imglist[r],(xp,40))
 
        
        
        xb=xb+2
        xc=xc+2
        
        clock.tick(FPS)
        pygame.display.update()
        
        frames=frames+1
        
if __name__=="__main__":
    main()