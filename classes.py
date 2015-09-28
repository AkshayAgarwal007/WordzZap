import pygame

class BaseClass(pygame.sprite.Sprite):
 
 allsprites = pygame.sprite.Group()
 def __init__(self,x1,image_string):
  
  pygame.sprite.Sprite.__init__(self)
  BaseClass.allsprites.add(self)

  self.image = pygame.image.load(image_string).convert_alpha()
  
  
  if image_string=='./Assets/grapes.gif':
    x=x1+68
    y=70
    width=50
    height=90
  
  self.image=pygame.transform.scale(self.image,(width,height)) 
  self.rect = self.image.get_rect()
  
  self.rect.x = x
  self.rect.y = y
  self.base=644

  self.width = width
  self.height = height
  
class Tux:
    movex = []
    
class Fruit (BaseClass):
    List = pygame.sprite.Group()
    
    def __init__(self,x1,image_string):
        BaseClass.__init__(self,x1,image_string)
        Fruit.List.add(self)
        self.going_right=True
        self.going_down=False
        self.move=True
        self.velx=1
        self.vely=1
        
    def motion(self):
        
        if self.going_right==True:  
            self.rect.x +=self.velx
        elif self.going_down==True:
            self.rect.y+=self.vely
            if self.rect.y+self.width+self.vely>=self.base:
                print self.rect.y
                self.going_down=False
                Tux.movex.append(self.rect.x)
            
    
