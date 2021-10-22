import pygame

class Panda (pygame.sprite.Sprite):
    '''This class defines a sprite for ours enemies'''
    def __init__ (self, screen):
        '''The class defines an enemy sprite.'''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load ("images/pandaRest1.jpg")
        self.image.set_colorkey((255,255,255))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = ((600, 400))

    def update(self):
        self.rect.left -= 1

class Character (pygame.sprite.Sprite):
    '''This class defines a sprite for our character.'''
    def __init__ (self, screen):
        '''The class defines a character sprite.'''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load ("images/person.png")
        self.image.set_colorkey((255,255,255))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = ((100, 400))

    def changeX (self, direction):
        if direction == "left":
            self.rect.left -= 10
        else:
            self.rect.left += 10

    def changeY (self, direction):
        if direction == "up":
            self.rect.top -=10
        else:
            self.rect.top += 10

    