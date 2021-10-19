import pygame, random
 
class Cherry(pygame.sprite.Sprite):
    '''A simple Sprite subclass to represent static Cherry sprites.'''
    def __init__(self, screen):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Set the image and rect attributes for the cherries
        self.image = pygame.image.load("cherry.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.rect.centery = random.randrange(0, screen.get_height())

 
class Pacman(pygame.sprite.Sprite):
    '''A simple Sprite subclass to represent static Cherry sprites.'''
    def __init__(self, screen, directionX, directionY):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        self.directionX = directionX
        self.directionY = directionY
        self.window = screen
 
        # Set the image and rect attributes for the pacman
        self.image = pygame.image.load("pacman-right.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.rect.centery = random.randrange(0, screen.get_height())   

    def go_left (self):
        '''This function will display the Pacman going left'''
        self.image = pygame.image.load ("pacman-left.png")
        self.directionX = -5
        self.directionY = 0
        
    def go_right (self):
        '''This function will display the Pacmman going right'''
        self.image = pygame.image.load ("pacman-right.png")
        self.directionX = 5
        self.directionY = 0      
        
    def go_up (self):
        '''This function will display the Pacman going up'''
        self.image = pygame.image.load ("pacman-up.png")
        self.directionX = 0
        self.directionY = -5      
        
    def go_down (self):
        '''This function will display the Pacman going down'''
        self.image = pygame.image.load ("pacman-down.png")
        self.directionX = 0
        self.directionY = 5       
    
    
    def update(self):
        '''Automatically called in the Refresh section to update our Box Sprite's position.'''
        self.rect.left += self.directionX
        self.rect.top += self.directionY
        if self.rect.left < 0:
            self.rect.right = self.window.get_width()
        if self.rect.right > 640:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.bottom = self.window.get_height()
        if self.rect.bottom > 480:
            self.rect.top = 0
