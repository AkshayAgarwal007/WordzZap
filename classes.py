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
            
        elif image_string=='./Assets/banana.gif':
            x=x1+70
            y=78
            width=40
            height=80
        
            
        elif image_string=='./Assets/plum.gif':
            x=x1+75
            y=79
            width=37
            height=77
            
        elif image_string=='./Assets/cherry.gif':
            x=x1+75
            y=77
            width=60
            height=70
            
        elif image_string=='./Assets/pear.gif':
            x=x1+79
            y=83
            width=37
            height=70
            
        elif image_string=='./Assets/melon.gif':
            x=x1+66
            y=86
            width=50
            height=70
            
        elif image_string=='./Assets/orange.gif':
            x=x1+75
            y=83
            width=40
            height=50
            
        elif image_string=='./Assets/strawberry.gif':
            x=x1+75
            y=83
            width=37
            height=70
  
        self.image=pygame.transform.scale(self.image,(width,height)) 
        self.rect = self.image.get_rect()
  
        self.rect.x = x
        self.rect.y = y
        self.base=644

        self.width = width
        self.height = height
 
    def destroy(self,ClassName):
        ClassName.List.remove(self)
        BaseClass.allsprites.remove(self)
        del self
        
        
class Tux:
    movex = []
    score = 0
    
class Fruit (BaseClass):
    List = pygame.sprite.Group()
    
    def __init__(self,x1,image_string):
        BaseClass.__init__(self,x1,image_string)
        Fruit.List.add(self)
        self.going_right=True
        self.going_down=False
        self.move=True
        self.velx=2
        self.vely=2
        
    def motion(self):
        
        if self.going_right==True:  
            self.rect.x +=self.velx
        elif self.going_down==True:
            self.rect.y+=self.vely
            if self.rect.y+self.width+self.vely>=self.base:
                print self.rect.y
                self.going_down=False
                Tux.movex.append(self.rect.x)
                self.move=False            
    
