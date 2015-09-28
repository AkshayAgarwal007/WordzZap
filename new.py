import pygame
import sys
from pygame.locals import *

class name:
    name1 = 'apple'


def text_display(text,color):
   FONT=pygame.font.SysFont('monospace',32)
   FONT.set_bold(True)
   SURFACEFONT=FONT.render(text,True,color)
   return SURFACEFONT



pygame.init()
screen = pygame.display.set_mode((1366,768),pygame.FULLSCREEN)
pygame.display.set_caption('WordzZap')

white= (255,255,255)
black=(0,0,0)
red=(255,0,0)
text1=text_display(name.name1,white)
text1_a=text1.get_rect()

FONT=pygame.font.SysFont('monospace',32)
FONT.set_bold(True)
u=FONT.size(name.name1)
text1_a.top=40
text1_a.left=40

while True:
    # PROCESSING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            pygame.quit()
            sys.exit()
            
        if event.type==pygame.KEYDOWN:
                if event.key ==  K_ESCAPE:
                    pygame.quit()
                    sys.exit()
    text1_a.left= text1_a.left+1             
    
    screen.fill(black)
    screen.blit(text1,text1_a)
                    
    pygame.display.update()