import pygame
 
class Ball(pygame.sprite.Sprite):
    '''This class defines the sprite for our Ball.'''
    def __init__(self, screen):
        '''This initializer takes a screen surface as a parameter, initializes
        the image and rect attributes, and x,y direction of the ball.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Set the image and rect attributes for the Ball
        self.image = pygame.Surface((20, 20))
        self.image = pygame.image.load("ball.png")
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width()/2,screen.get_height()/2)
 
        # Instance variables to keep track of the screen surface
        # and set the initial x and y vector for the ball.
        self.window = screen
        self.dx = 3
        self.dy = -6
 
    def changeDirection(self):
        '''This method causes the y direction of the ball to reverse.'''
        self.dy = -self.dy
        self.rect.centery += self.dy 
        
    def reset (self):
        '''This function resets the ball once it hits the endzone'''
        self.rect.center = (self.window.get_width()/2, self.window.get_height()/2)
        self.dx = 3
        self.dy = -6        
             
    def update(self):
        '''This method will be called automatically to reposition the
        ball sprite on the screen.'''
        self.rect.left += self.dx
        self.rect.top += self.dy
        if self.rect.left <= 0 or self.rect.right >= self.window.get_width():
            self.dx = -self.dx 
        elif self.rect.top <= 0:
            self.dy = - self.dy
        
class Player(pygame.sprite.Sprite):
    '''This class defines the sprite for Player'''
    def __init__(self, screen):
        '''This initializer takes a screen surface, and player as a
        parameters. It loads an image and positions it on the bottom center'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Creates a paddle in the center of the screen
        self.image = pygame.Surface((100, 10))
        self.image = pygame.image.load("paddle.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width()/2,screen.get_height()/2)
 
        # Position it 50 pixels from screen up.
        self.rect.top = screen.get_height()-50
 
        # Center the player horizontally in the window.
        self.rect.centerx = screen.get_width()//2
        self.window = screen
        self.dx = 0
      
    def changeDirection(self, xyChange):
        '''This method takes a (x,y) tuple as a parameter, extracts the 
        y element from it, and uses this to set the players y direction.'''
        self.dx = xyChange[0] * 5
        self.rect.left += self.dx
         
    def update(self):
        '''This method will be called automatically to reposition the
        player sprite on the screen.'''
        # Check if we have reached the right or left of the screen.
        # If not, then keep moving the player in the same x direction.
        if self.rect.left <= 0:
            self.rect.left = 0
        # If yes, then we don't change the y position of the player at all.
        elif self.rect.right >= self.window.get_width():
            self.rect.right = self.window.get_width()

class EndZone(pygame.sprite.Sprite):
    '''This class defines the sprite for our left and right end zones'''
    def __init__(self, screen, xPosition):
        '''This initializer takes a screen surface, and x position  as
        parameters.  For the left (player 1) endzone, x_position will = 0,
        and for the right (player 2) endzone, x_position will = 639.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # Our endzone sprite will be a 1 pixel wide black line.
        self.image = pygame.Surface((screen.get_width(), 1))
        self.image = self.image.convert()
        self.image.fill((0, 0, 0))
         
        # Set the rect attributes for the endzone
        self.rect = self.image.get_rect()
        self.rect.left = xPosition
        self.rect.top = screen.get_height()-1
        
class DataKeeper(pygame.sprite.Sprite):
    '''This class defines a label sprite to display the score and the lives.'''
    def __init__(self):
        '''This initializer loads the system font "samFont/otf", and sets the score to 0 and lives to 3'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        # Load our custom font, and initialize the starting score and lives.
        self.font = pygame.font.Font("samFont.otf", 30)
        self.score = 0
        self.lives = 3
        
    def points(self, value):
        '''This method adds points depending on the bricks'''
        self.score += value
    
    def removeLives(self):
        '''This methods subtracts lives every time ball hits the endzone'''
        self.lives -= 1
     
    def gameOver(self):
        '''There is a winner when the player runs out of 3 lives.
        This method returns 0 if there is no winner yet, 1 if player 1 has
        won, or 2 if player 2 has won.'''
        if self.lives <= 3 and self.lives >= 1:
            return False
        else:
            return True
 
    def update(self):
        '''This method will be called automatically to display 
        the current score and lives at the top of the game window.'''
        message = f"Lives: {self.lives} Score: {self.score}"
        self.image = self.font.render(message, True, (0, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (320, 15)
        
class Brick(pygame.sprite.Sprite):
    '''This class creates the bricks'''
    def __init__ (self, screen, x, y, value):
        '''This function initalizes the image and colour as an instance variable'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        # Creates the bricks
        self.image = pygame.Surface((40, 20))
        # Creates a dictonary for each colour row of bricks
        self.colour = {40 : (255,20,147),
                       60 : (255, 0 ,0), 
                       80 : (255,215,0),
                       100 : (255,125,64),
                       120 : (0,201,87),
                       140 : (30,144,255)}
        # Fills the bricks with a colour depending on their y coordinate
        self.image.fill (self.colour[y])
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.value = value[y]
        
    def get_Value(self):
        """Accessor to return the y coordinate of the brick"""
        return self.value
        
        