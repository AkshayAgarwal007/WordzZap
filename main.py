import pygame
import sys
from pygame.locals import *
from main2 import *
import random
import string

def text_display(text,color):
   FONT=pygame.font.SysFont('monospace',32)
   FONT.set_bold(True)
   SURFACEFONT=FONT.render(text,True,color)
   return SURFACEFONT

class name:
    name1=''
    name2=''
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((1366,768),pygame.FULLSCREEN)
    pygame.display.set_caption('WordzZap')
    metro2(screen)
    FPS=120
    clock=pygame.time.Clock()
    
    red=(255,0,0)
    white=(255,255,255)
    
    backglist=['./Assets/layer_1.png','./Assets/layer_2.png','./Assets/layer_3.png']
    
    backg = []
    
    character = pygame.image.load('./Assets/1.png').convert_alpha()
 
    
    board=pygame.image.load('./Assets/board1.png').convert_alpha()
    
    fruitlist = ['./Assets/lit.png','./Assets/lit.png','./Assets/lit.png']
    
    fruit = []
    for img1 in fruitlist:
        fruit.append(pygame.image.load(img1).convert_alpha())
        
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
    
    x1=100
    display_reg = []
    lst = ['apple','orange','banana']
    
    xf_lst = [0]
    yf_lst = [0]
    fs=100
    
    fall_list=[]
    fall_list_x=[]
    
   #-------------------------------------------------
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
    
    #---------------------------------------------
    sskey=''
    
    
    fallx=800
    move=True
    move_right=True
    
    fall=False
    
    yf=60
   
    
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
            fall_list.append(fruit[r1])
            fall_list_x.append(fs)
            fall=True
            current_string=''
            marker=0
            r1= random.randint(0,len(lst)-1)
            current_string = lst[r1] 
            name.name1=''
            name.name2=''
           
            
            
        
       
        text1=text_display(name.name1,white)
        text2=text_display(name.name2,red)
        
        
        screen.blit(backg[0],(0,0))
        
        screen.blit(backg[1],(0,768-683))
        
        screen.blit(tree,(1050,360))
        screen.blit(tree,(850,415))
        
        screen.blit(backg[2],(0,768-683))
        screen.blit(fruit[r1],(fs,60))
        
        
        
        screen.blit(board,(xb,565))
        screen.blit(character,(xc,573))
        
        
        
        
        fs=fs+1
        
        if frames%10==0:

      
            r=r+1
            if r==4:
                r=0

        xp=xp+1
        screen.blit(imglist[r],(xp,40))
        FONT=pygame.font.SysFont('monospace',32)
        FONT.set_bold(True)
        u=FONT.size(name.name1)
        
        text1_a.left=text1_a.left+1
        text2_a.left=text1_a.left+u[0]
        
 
        screen.blit(text1,text1_a)
        screen.blit(text2,text2_a)
        
        if fall==True:
            for imgh in fall_list:
                screen.blit(imgh,(fall_list_x[0],yf))
                yf=yf+1
        
                if yf+70>565+190:
                    fall=False
                    fallx=fall_list_x[0]
                    move=True
                    move_right=False
                    
        if xp>1450:
            xp=-200
            current_string=''
            marker=0
            
            r1= random.randint(0,len(lst)-1)
            current_string = lst[r1]
            name.name1=''
            name.name2=current_string
           
            
        
        
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