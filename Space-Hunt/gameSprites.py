'''
By : Gary Huang
Date : April 30, 2019
Description : This is contains many class and sprites which will help the development of the game
'''
import pygame, random

class Crosshair (pygame.sprite.Sprite):
    '''This class defines a sprite for our crosshair.'''
    def __init__ (self, screen):
        '''This initializer takes the mouse position as a parameter and displays an image on the mouse.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        # Loads crosshair image
        self.image = pygame.image.load("myImages/CrossHair.png").convert_alpha()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect() 

    def reset (self, center):
        '''This method will update the crosshair.'''
        self.rect.center = center
        
class Enemy (pygame.sprite.Sprite):
    '''This class defines a sprite for ours enemies.'''
    def __init__ (self, screen, number, waves, y):
        '''The class defines an enemy sprite.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Load the enemy depending on number
        self.number = number
        if self.number == 1:
            self.image = pygame.image.load ("myImages/Alien.png").convert_alpha()
        else:
            self.image = pygame.image.load ("myImages/SpaceShip.png").convert_alpha()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        while True:
            position = random.randint (40,550)
            if  20 <= position <= 260  or 380 <= position <= 570:
                break
        self.rect.left = position
        self.rect.centery = screen.get_height() + 40 + y
        
        self.window = screen
        self.dx = 1 + waves
        self.dy = -1 - waves

    def get_Enemy (self):
        '''This method will return the enemy.'''
        return self.number
    
    def changeDirection (self):
        '''This method will change the direction of the enemy once it touches the border.'''   
        self.dx = - self.dx
        self.rect.centerx += self.dx
    
    def update (self):
        '''This method will update the movement of the enemy until killed.'''
        self.rect.left += self.dx
        self.rect.top += self.dy
        
class Bullet (pygame.sprite.Sprite):
    '''This class will detect if the user press the down mouse buttom on an enemy sprite.'''
    def __init__ (self):
        '''This class defines a box for our crosshair.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface ((10, 10))
        self.image.set_colorkey ((255, 255, 255))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
    
        self.rect.center = (-10, -10)
        
    def set_position (self, xyPosition):
        '''This method will set the position of the box.'''
        self.rect.center = xyPosition
        
class Datakeeper (pygame.sprite.Sprite):
    '''This class will store all the data and display it at the top of the screen.'''
    def __init__ (self):
        '''This class defines a font for the messages.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        self.font = pygame.font.SysFont ("Arial", 30)
        self.points = 0
        self.lives = 20
        self.waves = 1
        self.highscore = 0
        self.num = 1
    
    def difficulty (self, num):
        '''This method will change the lives depending on the difficultly.'''
        self.num = num
        if self.num == 1:
            self.lives = 20
        elif self.num == 2:
            self.lives = 10
        elif self.num == 3:
            self.lives = 1                
    
    def addPoints (self, points):
        '''This method will add points depends what the user has hit.'''
        self.points += points * self.num
        
    def subtractPoints (self, points):
        '''This method will subtract points if the user has hit nothing.'''
        self.points -= points * self.num
        if self.points < 0:
            self.points = 0
            
    def addWaves (self):
        '''This method will increase the wave by 1 everytime a wave is cleared.'''
        self.waves += 1   
        
    def get_Waves (self):
        '''This method will return the waves.'''
        return self.waves
    
    def addHighscore (self):
        '''This method will keep tract of the highscore.'''
        self.highscore = score
        
    def get_Score (self):
        '''This method will return the score.'''
        return self.points
        
    def subtractLives (self):
        '''This method will subtract a live every time the enemy hits the endzone.'''
        self.lives -= 1
        if self.lives < 0:
            self.lives = 0
    
    def get_Lives (self):
        '''This method will return the lives remaining.'''
        return self.lives
    
    def update (self):
        '''This method will update the data at the top of the screen.'''
        message = f"Lives: {self.lives} Waves: {self.waves} Score: {self.points}"
        self.image = self.font.render(message, True, (0, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (320, 15)
        
class Borders (pygame.sprite.Sprite):
    '''This class will create the movements of the enemies.'''
    def __init__ (self, screen, x):
        '''This class defines a border for the enemy.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((1, screen.get_height()+ 900))
        self.image = self.image.convert()
        self.image.fill((255, 255, 255))
         
        # Set the rect attributes for the endzone
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = 0
        
        
class Endzone (pygame.sprite.Sprite):
    '''This class will create an endzone.'''
    def __init__ (self, screen):
        '''This class defines an endzone for our game.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((screen.get_width(), 1))
        self.image = self.image.convert()
        self.image.fill((255, 255, 255))
         
        # Set the rect attributes for the endzone
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 0        
        
class Astronaut (pygame.sprite.Sprite):
    '''This class will create the astronaut.'''
    def __init__ (self, screen, waves, y):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        self.number = 3
        self.imageNum = 0
        self.images = [pygame.image.load("myImages/astronaut0.png").convert_alpha(), pygame.image.load ("myImages/astronaut1.png").convert_alpha()]
        self.image = self.images[self.imageNum]
        self.image.set_colorkey((0,0,0))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        while True:
            position = random.randint (40,565)
            if  20 <= position <= 270  or 370 <= position <= 585:
                break
        self.rect.left = position
        self.rect.centery = screen.get_height() + 40 + y
        
        self.window = screen
        self.dx = 7 
        self.dy = -7

    def changeDirection (self):
        '''This method will change the direction of the astronaut once it touches the border.'''
        self.imageNum = (self.imageNum+1) % 2
        self.image = self.images[self.imageNum]
        self.dx = - self.dx
        self.rect.centerx += self.dx
        
    def get_Enemy (self):
        '''This method will return the enemy.'''
        return self.number 
    
    def update (self):
        '''This method will update the movement of the astronaut until dies.'''
        self.rect.left += self.dx
        self.rect.top += self.dy        
        
class Background (pygame.sprite.Sprite):
    '''This class will define the background image (earth).'''
    def __init__(self):
        '''This initializer method will instance earth image.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load ("myImages/globe.png").convert_alpha()
        self.originalImage = self.image
        self.rotationDegree = 360
        self.rect = self.image.get_rect()
        self.rect.left = -125
        self.rect.top = 500
        
    def update (self):
        '''This method will update the background's rotation.'''
        self.originalCenter = self.rect.center
        self.image = pygame.transform.rotate(self.originalImage, self.rotationDegree)
        self.rect = self.image.get_rect()
        self.rect.center = self.originalCenter
        self.rotationDegree -= 1
        if self.rotationDegree == 0:
            self.rotationDegree = 360
            
class FloatPoints (pygame.sprite.Sprite):
    '''This class will ascend points.'''
    def __init__(self, points, xy_pos):
        '''This initializer mthod will instance the timer.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        self.timer = 1
        font = pygame.font.SysFont('Arial', 30)
        self.image = font.render(f'{points}', True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = xy_pos
        
    def update(self):
        '''This method will update the motion of points.'''
        self.rect.centery -= 1
        self.timer += 1
        if self.timer > 15:
            self.kill()