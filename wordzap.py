import pygame,sys
from pygame.locals import *

pygame.init()


WIDTH, HEIGHT = 1366, 768
screen = pygame.display.set_mode( (WIDTH, HEIGHT),pygame.FULLSCREEN )
pygame.display.set_caption('WordzZap')

clock = pygame.time.Clock()
FPS = 24


#------------character image----------------
img_bug = pygame.image.load("./Assets/1.png").convert_alpha()

board=pygame.image.load('./Assets/board1.png').convert_alpha()

diff=70


#----------background and trees ----------------

backglist=['./Assets/layer_1.png','./Assets/layer_2.png','./Assets/layer_3.png']
    
backg = []

for img in backglist:
        backg.append(pygame.image.load(img).convert_alpha())

backg[2]=pygame.transform.scale(backg[2],(1366,683))
backg[0]=pygame.transform.scale(backg[0],(1366,683))
backg[1]=pygame.transform.scale(backg[1],(1366,683))

tree=pygame.image.load('./Assets/tree.png').convert_alpha()
    
tree=pygame.transform.scale(tree,(400,400))


#--------------------





# -------- Main Program Loop -----------
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

    # PROCESSING


    # LOGIC
    # LOGIC

    # DRAW
    screen.blit(backg[0],(0,0))
    screen.blit(backg[1],(0,768-683))
    screen.blit(tree,(1050,360))
    screen.blit(tree,(850,415))
    screen.blit(backg[2],(0,768-683))
    
    screen.blit(board, (40,565) )
    screen.blit(img_bug, (40+diff,573) )
    
    pygame.display.flip()    
    # DRAW
    clock.tick(FPS)
