import pygame
import random

class Panda (pygame.sprite.Sprite):
    '''This class defines a sprite for ours enemies'''
    def __init__ (self, screen, life):
        '''The class defines an enemy sprite.'''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load ("images/pandaRest1.jpg")
        self.image.set_colorkey((255,255,255))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = ((random.randrange(600, 680), random.randrange(40, 440)))
        self.speedx = random.randrange(1, 3)
        self.speedy = random.randrange(-3, 3)
        self.lives = life

    def changeY(self):
        self.speedy = -self.speedy

    def update(self):
        self.rect.x -= self.speedx
        self.rect.y += self.speedy
        if self.rect.x < -10:
            self.rect.center = ((600, random.randrange(0, 480)))
            self.lives.loseLives()

class Character (pygame.sprite.Sprite):
    '''This class defines a sprite for our character.'''
    def __init__ (self, screen):
        '''The class defines a character sprite.'''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load ("images/plane.png")
        self.image.set_colorkey((255,255,255))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = ((100, 400))
        self.lives = 3

    def update (self):
        self.rect.center = pygame.mouse.get_pos()

class Bullet (pygame.sprite.Sprite):
    '''This class will detect if the user press space it will generate a bullet'''
    def __init__ (self, screen):
        '''The class defines a bullet.'''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load ("images/bullet.png")
        self.image.set_colorkey((255,255,255))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = ((pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
        
    def update (self):
        self.rect.left += 3
        if self.rect.left > 640:
            self.kill()

class Borders (pygame.sprite.Sprite):
    '''This class will create the movements of the pandas.'''
    def __init__ (self, screen, y):
        '''This class defines a border for the pandas'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((screen.get_width(), 1))
        self.image = self.image.convert()
        self.image.fill((0, 0, 0))
         
        # Set the rect attributes for the endzone
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = y
        
class lives:
    def __init__(self):
        self.lives = 3

    def getLives(self):
        return self.lives

    def loseLives(self):
        self.lives -= 1