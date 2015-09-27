import pygame
import sys
from pygame.locals import *
from main2 import *
import random

def text_display(text,color):
   FONT=pygame.font.SysFont('monospace',32)
   FONT.set_bold(True)
   SURFACEFONT=FONT.render(text,True,color)
   return SURFACEFONT


    
def main():
    pygame.init()
    screen = pygame.display.set_mode((1366,768),pygame.FULLSCREEN)
    pygame.display.set_caption('WordzZap')
    metro2(screen)
    FPS=120
    clock=pygame.time.Clock()
    
    red=(255,0,0)
    a=text_display('GRAPES',red)
    SURFACER_a=a.get_rect()
    SURFACER_a.center=(100,150)
    
    backglist=['./Assets/layer_1.png','./Assets/layer_2.png','./Assets/layer_3.png']
    
    backg = []
    
    character = pygame.image.load('./Assets/1.png').convert_alpha()
 
    
    board=pygame.image.load('./Assets/board1.png').convert_alpha()
        
    for img in backglist:
        backg.append(pygame.image.load(img).convert_alpha())
        
    tree=pygame.image.load('./Assets/tree.png').convert_alpha()
    
    tree=pygame.transform.scale(tree,(400,400))
        
    
    backg[2]=pygame.transform.scale(backg[2],(1366,683))
    backg[0]=pygame.transform.scale(backg[0],(1366,683))
    backg[1]=pygame.transform.scale(backg[1],(1366,683))
    
    imglist=[]

    for kp in range(0,4):
        imglist.append(pygame.image.load("./Assets/PNG/frame-%s.png"%str(kp+1)).convert_alpha())
 
    for f in range(0,4):
        imglist[f]=pygame.transform.scale(imglist[f],(100,70))
        
  
    
    for img1 in backg:
        img1.convert_alpha()
    xb=40
    xc=110
    xp=0
    r=0
    frames=0
    onn=0
    x1=100
    display_reg = []
    lst = ['apple','orange','banana']
    
    r1= random.randint(0,len(lst)-1)
    current_string = list(lst[r1]) 
    for r3 in current_string:
        display_reg.append(0)
    
    print current_string
    sskey=''
    marker=0
    string_picker=0
    
    while True:
        
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key ==  K_ESCAPE:
                    metro2(screen)
                    
                if event.key <=127:
                    sskey = (chr(event.key))
                    if current_string[marker]==sskey:
                        
                        
                        display_reg[marker]=1
                        marker=marker+1
                        
                    else:
                        for i3 in range(0,len(display_reg)):
                            display_reg[i3]=0
                        marker=0
                        
        
        if marker == len(display_reg):
            current_string=[]
            display_reg=[]
            marker=0
            r1= random.randint(0,len(lst)-1)
            current_string = list(lst[r1]) 
            for r3 in current_string:
                display_reg.append(0)
            print current_string
            
        print display_reg
        screen.blit(backg[0],(0,0))
        
        screen.blit(backg[1],(0,768-683))
        
        screen.blit(tree,(1050,360))
        screen.blit(tree,(850,415))
        
        screen.blit(backg[2],(0,768-683))
        screen.blit(a,SURFACER_a)
        
        
        screen.blit(board,(xb,565))
        screen.blit(character,(xc,573))
        
        SURFACER_a.center=(x1,150)
        
        x1=x1+1
        
        if frames%10==0:

      
            r=r+1
            if r==4:
                r=0

        xp=xp+1
        screen.blit(imglist[r],(xp,40))
 
        
        if onn==0:
            xb=xb+2
            xc=xc+2
        
        if onn==1:
            xb=xb-2
            xc=xc-2
        
        if xb>=1000:
            
            onn=1
        if xb<=38:
            onn=0
        
        clock.tick(FPS)
        pygame.display.update()
        
        frames=frames+1
        
if __name__=="__main__":
    main()