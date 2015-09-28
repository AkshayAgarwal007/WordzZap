import pygame
import sys
from pygame.locals import *
from main2 import *
import random
import string
from classes import *

def text_display(text,color):                   #surface font functions
   text=text.upper()
   FONT=pygame.font.SysFont('monospace',32)
   FONT.set_bold(True)
   SURFACEFONT=FONT.render(text,True,color)
   return SURFACEFONT

class name:
    name1=''
    name2=''                  # class for surface font fruit names
    
def main():
    
    #--------------------- pygame initialisation------------------
    pygame.init()
    screen = pygame.display.set_mode((1366,768),pygame.FULLSCREEN)
    pygame.display.set_caption('WordzZap')
    metro2(screen)
    FPS=120
    clock=pygame.time.Clock()
    
    #------------------------some colours------------------------------
    
    red=(255,0,0)
    white=(255,255,255)
    
    
    
    #----------------------- character and board load-----------------------
    
    character = pygame.image.load('./Assets/1.png').convert_alpha()
 
    
    board=pygame.image.load('./Assets/board1.png').convert_alpha()
    
    
    
    
    #----------------------- fruit loader------------------------------------
    
    fruitlist = ['./Assets/lit.png','./Assets/lit.png','./Assets/lit.png']
        
    mfruit= Fruit('./Assets/grapes.gif')
        
    
    
    #-------------------three layer background and trees------------------------------
    
    backglist=['./Assets/layer_1.png','./Assets/layer_2.png','./Assets/layer_3.png']
    
    backg = []
    
    for img in backglist:
        backg.append(pygame.image.load(img).convert_alpha())
        
    tree=pygame.image.load('./Assets/tree.png').convert_alpha()
    
    tree=pygame.transform.scale(tree,(400,400))
        
    
    backg[2]=pygame.transform.scale(backg[2],(1366,683))
    backg[0]=pygame.transform.scale(backg[0],(1366,683))
    backg[1]=pygame.transform.scale(backg[1],(1366,683))
    
    for img1 in backg:
        img1.convert_alpha()
    
    
    #----------------------- bird sprite-----------------------------------------
    imglist=[]
    
    for kp in range(0,4):
        imglist.append(pygame.image.load("./Assets/PNG/frame-%s.png"%str(kp+1)).convert_alpha())
 
    for f in range(0,4):
        imglist[f]=pygame.transform.scale(imglist[f],(100,70))
        
    xp=0     #---------bird movement---------------
    
    r=0      #-----------bird animation-------------
    
   
    
    
    frames=0
   

   #-----------fruit names surface font---------------------
    
    lst = ['apple','orange','banana']
    marker=0
    r1= random.randint(0,len(lst)-1)
    current_string = lst[r1]
    nms1 = []
    nms2=[]
    
        
    name.name1=''
    name.name2=current_string
    text1=text_display(name.name1,white)
    text1_a=text1.get_rect()

    text2=text_display(name.name2,red)
    text2_a=text1.get_rect()
    
    FONT=pygame.font.SysFont('monospace',32)
    FONT.set_bold(True)
    u=FONT.size(name.name1)
    
    text1_a.top=150
    text1_a.left=40
    text2_a.top=150
    text2_a.left=40+u[0]
    
    sskey=''
    
    #------------tux movement----------------------
    
    
    xb=40
    xc=110
    fallx=800
    move=True
    move_right=True

    register=True
    
    while True:
        
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key ==  K_ESCAPE:
                    metro2(screen)
                   
                if event.key <=127 and register==True:
                    sskey = (chr(event.key))
                    if current_string[marker]==sskey:
                        
                        
                        marker=marker+1
                        for i4 in range(0,marker):
                            nms1.append(current_string[i4])
                        for i5 in range(marker,len(current_string)):
                            nms2.append(current_string[i5])
        
                        name.name1=''.join(nms1)
                        name.name2=''.join(nms2)
                        nms1=[]
                        nms2=[]
                        
                    else:
                        
                        marker=0
                        name.name1=''
                        name.name2=current_string
                        
        print name.name1
        print name.name2
        
        if marker == len(current_string):
            
            current_string=''
            marker=0
            r1= random.randint(0,len(lst)-1)
            current_string = lst[r1] 
            name.name1=''
            name.name2=''
            register=False
           
            
            
        
       
        text1=text_display(name.name1,white)
        text2=text_display(name.name2,red)
        
        
        screen.blit(backg[0],(0,0))
        
        screen.blit(backg[1],(0,768-683))
        
        screen.blit(tree,(1050,360))
        screen.blit(tree,(850,415))
        
        screen.blit(backg[2],(0,768-683))
       
        
        
        
        screen.blit(board,(xb,565))
        screen.blit(character,(xc,573))
        
        
  
        
        if frames%10==0:

      
            r=r+1
            if r==4:
                r=0

        xp=xp+1
        mfruit.motion()
        screen.blit(imglist[r],(xp,40))
        BaseClass.allsprites.draw(screen)
        
        FONT=pygame.font.SysFont('monospace',32)
        FONT.set_bold(True)
        u=FONT.size(name.name1)
        
        text1_a.left=text1_a.left+1
        text2_a.left=text1_a.left+u[0]
        
 
        screen.blit(text1,text1_a)
        screen.blit(text2,text2_a)
        
        
                    
        if xp>1450:
            xp=-200
            current_string=''
            marker=0
            
            r1= random.randint(0,len(lst)-1)
            current_string = lst[r1]
            name.name1=''
            name.name2=current_string
            text1_a.left=-160
            text2_a.left=-160
            register=True
            
        
        
        if move==True:
            if move_right==True:
                xb=xb+3
                xc=xc+3
                if xb+190>=fallx:
                    move = False
                    
            if move_right==False:
                xb=xb-3
                xc=xc-3
                if xb<=fallx:
                    move = False
        
        
        clock.tick(FPS)
        pygame.display.update()
        
        frames=frames+1
        
if __name__=="__main__":
    main()