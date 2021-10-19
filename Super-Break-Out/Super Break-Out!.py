'''
By : Gary Huang
Date : April 24, 2019
Description : This program is a game that represents Super Break-Out!
'''
# This version of A Super Break-Out! 

# I - IMPORT AND INITIALIZE
import pygame, Sprites
pygame.init()
     
def main():
    '''This function is the mainline logic of the program'''
      
    # D - DISPLAY
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Super Break-Out!")
     
    # E - ENTITIES
    background = pygame.image.load ("background.jpg")
    background.convert()
    screen.blit(background, (0, 0))
    
    # Music and sound effects
    pygame.mixer.music.load("Time to Love-October.mp3")
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(-1)
    wow = pygame.mixer.Sound("FairyTail WOW.wav")
    wow.set_volume(0.1)
    ohNo = pygame.mixer.Sound("Oh No.wav")
    ohNo.set_volume (1.0)
 
    # Sprites for: ScoreKeeper label, End Zones, Ball, and Player
    dataKeeper = Sprites.DataKeeper()
    ball = Sprites.Ball(screen)
    player = Sprites.Player(screen)
    playerEndzone = Sprites.EndZone(screen,0)
    playerMirror = Sprites.Player(screen)
    value = {40 : 6, 60 : 5, 80 : 4, 
            100 : 3, 120 : 2, 140 : 1}    
    bricks = []
    for yDirection in range (40, 141, 20):
        for xDirection in range (5, screen.get_width()-39, 35):
            bricks.append (Sprites.Brick(screen, xDirection, yDirection, value))
    brickSprites = pygame.sprite.Group(bricks)
    allSprites = pygame.sprite.OrderedUpdates(dataKeeper, bricks, playerEndzone, ball, player)
    
    # "Game Over" and "You won!" or "You lost!" is displayed after game loop terminates
    font = pygame.font.Font("font.ttf", 60)
    message = "Gameover"
    message1 = "You lost!"
    message2 = "You won!"
    gameover = font.render(message, True, (255,69,0))
    Lose = font.render(message1, True, (255,69,0))
    Win = font.render(message2, True, (255,69,0))
    
    # A - ACTION
    # A - ASSIGN 
    clock = pygame.time.Clock()
    keepGoing = True
    mirror = False
    
    # Hide the mouse pointer
    pygame.mouse.set_visible(False)    
    
    # L - LOOP
    while keepGoing:
     
        # TIME
        clock.tick(30)
        
        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        keys = pygame.key.get_pressed
        if keys()[pygame.K_RIGHT] == True:
            if mirror == True:
                playerMirror.changeDirection ((-1, 0))
            player.changeDirection((1, 0))
        if keys()[pygame.K_LEFT] == True:
            if mirror == True:
                playerMirror.changeDirection ((1, 0))          
            player.changeDirection((-1, 0))
        
        # Check for game over (if a player runs out of lives)
        if ball.rect.colliderect(playerEndzone):
            dataKeeper.removeLives()
            ball.reset()
            ohNo.play()
            if dataKeeper.gameOver():
                screen.blit (gameover, (165, 125))
                screen.blit(Lose, (165, 215))
                keepGoing = False
                ball.kill()
        
        # Check if the ball hits brick(s)
        collisions = pygame.sprite.spritecollide(ball, brickSprites, False)
        if collisions:
            ball.changeDirection()
            for i in collisions:
                i.kill()
                wow.play()
                dataKeeper.points(i.get_Value())
                     
        # Check if the ball hits the player 
        if ball.rect.colliderect(player):
            ball.changeDirection()
            
        # Check if the ball hits the mirror player
        if mirror == True:
            if ball.rect.colliderect(playerMirror):
                ball.changeDirection()
            
        # Check if there's no more bricks and displays "Gameover!" and "You Won!"
        if len (brickSprites) == 0:
            screen.blit (gameover, (165, 115))
            screen.blit (Win, (165, 205))
            
        # Check if there's are half bricks left then inputs the second paddle
        if len(brickSprites) <= len(bricks)//2:
            mirror = True
            allSprites.add (playerMirror)
            
        # R - REFRESH SCREEN
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen) 
        pygame.display.flip()
 
    # Unhide the mouse pointer
    pygame.mouse.set_visible(True)
    pygame.display.flip()
    
    # Close the game window
    pygame.time.delay (3000)
    pygame.quit()    
     
# Call the main function
main()    