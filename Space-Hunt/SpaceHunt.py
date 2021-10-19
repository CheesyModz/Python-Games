'''
By : Gary Huang
Date : April 30, 2019
Description : This is a game that represents Space Hunt (similar to duck hunt)
'''
# I - Import and Initialize
import pygame, gameSprites
pygame.init()
pygame.mixer.init()

def game (datakeeper): 
    '''This function is the game of the program.'''  
    
    # D - Display configuration
    screen = pygame.display.set_mode((640, 800))
    pygame.display.set_caption("Space Hunt!")    
    
    # E - Entities 
    background = pygame.Surface(screen.get_size())
    background.convert()
    background.fill((0, 0, 0))
    screen.blit (background, (0,0))
    
    # Creates borders for the enemy and endzone
    borderLeft = gameSprites.Borders (screen, 20)
    borderMid = gameSprites.Borders (screen, 320)
    borderRight = gameSprites.Borders (screen, 620)
    borderSprites = pygame.sprite.Group (borderLeft, borderMid, borderRight)
    endzone = gameSprites.Endzone(screen)
    
    # Sounds
    pygame.mixer.music.load("Sound/Wii_Sports.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
    shot = pygame.mixer.Sound("Sound/Pow.wav")
    shot.set_volume(0.6)
    angry = pygame.mixer.Sound("Sound/NowImAngry.wav")
    angry.set_volume(0.8)
    one = pygame.mixer.Sound("Sound/OneShot.wav")
    one.set_volume(0.4)
    kill = pygame.mixer.Sound("Sound/OneKill.wav")
    kill.set_volume(0.4)
    
    # Defines the font    
    font = pygame.font.SysFont ("Arial", 10)
    
    # Creates a crosshair and a box sprite for the mouse
    crosshair = gameSprites.Crosshair(screen)  
    bullet = gameSprites.Bullet()     
    
    # Creates the enemies coming in at different y coordinates
    y = 100
    aliens = []
    for i in range (5):
        aliens.append (gameSprites.Enemy(screen, 1, datakeeper.get_Waves(), y*i))
    spaceship = []
    for i in range (5):
        spaceship.append (gameSprites.Enemy(screen, 2, datakeeper.get_Waves(), y*(i+5)))    
    enemies = pygame.sprite.Group(aliens, spaceship)
    
    # background
    back = gameSprites.Background()
    
    allSprites = pygame.sprite.LayeredUpdates (back, datakeeper, endzone, aliens, spaceship, crosshair)
    
    # A - Action (broken into ALTER steps)
     
        # A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True
    points = {"alien" : 20, "ship" : 30, "miss" : 25}
    miss = False
    teammate = True
    music = 1
    
    # Hide the mouse pointer
    pygame.mouse.set_visible(False)
    
        # L - Loop
    while keepGoing:
     
        # T - Timer to set frame rate
        clock.tick(30)
     
        # E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return datakeeper
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    bullet.set_position(pygame.mouse.get_pos())
                    miss = True
        crosshair.reset(pygame.mouse.get_pos())
        
        # If the user is on the 5th wave, an astronaut will appear
        if datakeeper.get_Waves() >= 5 and teammate:
            astronaut = gameSprites.Astronaut(screen, datakeeper.get_Waves(), y)
            enemies.add(astronaut)
            allSprites.add (astronaut)
            allSprites.move_to_front (crosshair)
            teammate = False
        
        # If no more lives left display gameover
        if datakeeper.get_Lives() == 0:
            return datakeeper
        
        # Check for collision between the bullet and enemies
        # If so then add points depending on the type of monster
        collisions = pygame.sprite.spritecollide(bullet, enemies, False)
        if collisions: 
            miss = False
            for monster in collisions:
                monster.kill()
                if music == 1:
                    one.play()
                    music += 1
                else:
                    kill.play()
                    music -= 1
                # Add different points depending on what the user hits or subtract a live if astronaut hit
                if monster.get_Enemy() == 1:
                    datakeeper.addPoints(points["alien"])
                    floatingLabel = gameSprites.FloatPoints(f'+{points["alien"]*datakeeper.num}', monster.rect.center)
                    allSprites.add(floatingLabel)
                elif monster.get_Enemy() == 2:
                    datakeeper.addPoints(points["ship"])
                    floatingLabel = gameSprites.FloatPoints(f'+{points["ship"]*datakeeper.num}', monster.rect.center)
                    allSprites.add(floatingLabel)               
                elif monster.get_Enemy() == 3:
                    datakeeper.subtractLives()
                    floatingLabel = gameSprites.FloatPoints(-1, monster.rect.center)
                    allSprites.add(floatingLabel)                   
                    
        # If the player presses down button and doesn't collid with anything then subtract points
        if miss:
            datakeeper.subtractPoints (points["miss"])
            shot.play()
            miss = False 
            floatingLabel = gameSprites.FloatPoints(f'-{points["miss"]*datakeeper.num}', pygame.mouse.get_pos())
            allSprites.add(floatingLabel)             
        bullet = gameSprites.Bullet()
        
        # Check for collisions between enemies and border 
        # If so, change the direction of the enemy
        collisions = pygame.sprite.groupcollide (enemies, borderSprites, False, False)
        for monster in list (collisions):
            monster.changeDirection()
        
        # Check for collisions between the endzone and enemies
        # If so, kill the enemy sprite and subtract a life
        collisions = pygame.sprite.spritecollide (endzone, enemies, False)
        if collisions:
            for monster in collisions:
                monster.kill()
                if monster.get_Enemy() == 3:
                    continue
                else:
                    datakeeper.subtractLives()
                    angry.play()
                    floatingLabel = gameSprites.FloatPoints(f'-1', monster.rect.center)
                    allSprites.add(floatingLabel)                     
        
        # Increase the waves once there are no more enemies and resets the enemies
        if len(enemies) == 0:
            y = 100
            aliens = []
            for i in range (5):
                aliens.append (gameSprites.Enemy(screen, 1, datakeeper.get_Waves(), y*i))
            spaceship = []
            for i in range (5):
                spaceship.append (gameSprites.Enemy(screen, 2, datakeeper.get_Waves(), y*(i+5)))
            enemies = pygame.sprite.Group(aliens, spaceship)
            if datakeeper.get_Waves() >= 5 and teammate:
                astronaut = gameSprites.Astronaut(screen, datakeeper.get_Waves(), y)
                enemies.add(astronaut)
            allSprites.add(enemies)
            allSprites.move_to_front(crosshair)
            datakeeper.addWaves()
            
        # R - Refresh display
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        pygame.display.flip() 

def menu ():
    '''This function is the start menu of the game.'''
    # D - Display configuration
    screen = pygame.display.set_mode((640, 800))
    pygame.display.set_caption("Space Hunt!")
    
    # E - Entities
    background = pygame.Surface(screen.get_size())
    background.convert()
    background.fill((0, 0, 0))
    
    #Sounds
    pygame.mixer.music.load("Sound/CrabRave.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)    
    shot = pygame.mixer.Sound("Sound/Pow.wav")
    shot.set_volume(0.6)    
    
    # Creates the font
    font = pygame.font.SysFont("Arial", 30)
    titleFont = pygame.font.Font ("SpaceHunt.ttf", 60)
    
    # Displays the highscore at the top
    try:
        highscore = open ("highscore.txt", "r")
        highscores = 0
        for line in (highscore):
            highscores = int (line)
                
        score = font.render (f"Highscore: {highscores}", True, (0, 255, 255))
        background.blit (score, (245, 5))
        highscore.close()
        
    except FileNotFoundError:
        print ("Bro, you deleted the file.")      
    
    # Scoreboard
    datakeeper = gameSprites.Datakeeper()    
    
    # Creates a crosshair   
    crosshair = gameSprites.Crosshair(screen)
    
    # Background
    back = gameSprites.Background()
    allSprites = pygame.sprite.OrderedUpdates (back, crosshair) 
    
    # Title
    title = titleFont.render ("Space Hunt", True, (255, 0, 0))
    background.blit (title, (170, 50))
    
    # Creates a start button
    box = pygame.draw.rect (background, (255, 140, 0), (275, 150, 100, 50), 1)
    boxXcord = range (box.left, box.right + 1)
    boxYcord = range (box.top, box.bottom + 1)
    start = font.render ("Start!", True, (255, 140, 0))
    background.blit (start, (295, 155))
    
    # Creates mode difficuly
    # Easy mode
    easyBox = pygame.draw.rect (background, (0, 255, 0), (150, 225, 100, 50), 1)
    easyBoxXcord = range (easyBox.left, easyBox.right + 1)
    easyBoxYcord = range (easyBox.top, easyBox.bottom + 1) 
    easy = font.render ("Easy", True, (0, 255, 0))
    background.blit (easy, (175, 230))
    
    # Normal mode
    normalBox = pygame.draw.rect (background, (255, 255, 0), (275, 225, 100, 50), 1)
    normalBoxXcord = range (normalBox.left, normalBox.right + 1)
    normalBoxYcord = range (normalBox.top, normalBox.bottom + 1)    
    normal = font.render ("Normal", True, (255, 255, 0))
    background.blit (normal, (285, 230))    
    
    # Hard mode
    hardBox = pygame.draw.rect (background, (255, 0, 0), (400, 225, 100, 50), 1)
    hardBoxXcord = range (hardBox.left, hardBox.right + 1)
    hardBoxYcord = range (hardBox.top, hardBox.bottom + 1) 
    hard = font.render ("Hard", True, (255, 0, 0))
    background.blit (hard, (423, 230))    
    
    # Underline
    pygame.draw.rect (background, (255,255,255), (150, 285, 100, 10), 0)
    
    # Instructions
    instructionBox = pygame.draw.rect (background, (30, 144, 255), (250, 325, 150, 50), 1)
    instructionBoxXcord = range (instructionBox.left, instructionBox.right + 1)
    instructionBoxYcord = range (instructionBox.top, instructionBox.bottom + 1) 
    instruction = font.render ("Instructions", True, (30, 144, 255))
    background.blit (instruction, (262, 330))      
    
    screen.blit (background, (0,0))  
    
    # Action
    
    # Assign Values
    clock = pygame.time.Clock()
    
    # Hide the mouse pointer
    pygame.mouse.set_visible(False)    
    
    # Loop
    while True:
        
        # Time
        clock.tick(30)
        
        # Event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, datakeeper
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    if (pygame.mouse.get_pos()[0] in boxXcord) and (pygame.mouse.get_pos()[1] in boxYcord):
                        return True, datakeeper
                    if (pygame.mouse.get_pos()[0] in easyBoxXcord) and (pygame.mouse.get_pos()[1] in easyBoxYcord):
                        datakeeper.difficulty(1)
                        # Underline the one selected with white and fill the others with black
                        pygame.draw.rect (background, (255, 255, 255), (150, 285, 100, 10), 0) 
                        pygame.draw.rect (background, (0, 0, 0), (275, 285, 100, 10), 0) 
                        pygame.draw.rect (background, (0, 0, 0), (400, 285, 100, 10), 0)
                        screen.blit (background, (0,0))
                    if (pygame.mouse.get_pos()[0] in normalBoxXcord) and (pygame.mouse.get_pos()[1] in normalBoxYcord):
                        datakeeper.difficulty(2)
                        # Underline the one selected with white and fill the others with black
                        pygame.draw.rect (background, (255, 255, 255), (275, 285, 100, 10), 0) 
                        pygame.draw.rect (background, (0, 0, 0), (150, 285, 100, 10), 0)
                        pygame.draw.rect (background, (0, 0, 0), (400, 285, 100, 10), 0)
                        screen.blit (background, (0,0))
                    if (pygame.mouse.get_pos()[0] in hardBoxXcord) and (pygame.mouse.get_pos()[1] in hardBoxYcord):
                        datakeeper.difficulty(3)
                        # Underline the one selected with white and fill the others with black
                        pygame.draw.rect (background, (255, 255, 255), (400, 285, 100, 10), 0)
                        pygame.draw.rect (background, (0, 0, 0), (150, 285, 100, 10), 0)
                        pygame.draw.rect (background, (0, 0, 0), (275, 285, 100, 10), 0) 
                        screen.blit (background, (0,0))
                    if (pygame.mouse.get_pos()[0] in instructionBoxXcord) and (pygame.mouse.get_pos()[1] in instructionBoxYcord):
                        instructions (screen)
                        screen.blit (background, (0,0))
                    shot.play()                 
        crosshair.reset(pygame.mouse.get_pos())
        
        # R - Refresh display
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        pygame.display.flip()  

def instructions (screen):
    '''This function will display the instructions.'''
    # E - Entities
    background = pygame.image.load("myImages/Instructions.png")
    background.convert()
    screen.blit (background, (0,0))
    
    # Creates a crosshair and a box sprite for the mouse
    crosshair = gameSprites.Crosshair(screen)  
    allSprites = pygame.sprite.OrderedUpdates (crosshair)
    
    # Action
    
    # Assign Values
    check = True
    clock = pygame.time.Clock()
    
    # Hide the mouse pointer
    pygame.mouse.set_visible(False)    
    
    # Loop
    while check:
        
        # Time
        clock.tick(30)
        
        # Event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                check = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                check = False
        crosshair.reset(pygame.mouse.get_pos())
        
        # R - Refresh display
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        pygame.display.flip()          

def gameOver(datakeeper):
    '''This function is the gameover screen.'''
    # D - Display configuration
    screen = pygame.display.set_mode((640, 800))
    pygame.display.set_caption("Space Hunt!")    
    
    # E - Entities
    background = pygame.Surface(screen.get_size())
    background.convert()
    background.fill((0, 0, 0)) 
    
    # Adds the score to highscore.txt file  
    try:
        highscore = open ("highscore.txt", "r")
        for line in (highscore):
            highscores = int (line)
        highscore.close()
        
        highscore = open ("highscore.txt", "w")
        highscore.write (str(max (highscores, datakeeper.get_Score())))
        highscore.close()
        
    except FileNotFoundError:
        print ("Bro, you deleted the file.")         
    
    # Creates a cross hair
    crosshair = gameSprites.Crosshair(screen)  
    
    # background
    back = gameSprites.Background()  
    
    allSprites = pygame.sprite.OrderedUpdates (back, crosshair)
    
    # Creates a font
    font = pygame.font.SysFont("Arial", 30)
    gameover = font.render(f"Game Over!", True, (0, 255, 255))
    background.blit (gameover, (250, 250))
    displayScore = font.render (f"You got a score {datakeeper.get_Score()}", True, (0, 255, 255))
    background.blit (displayScore, (220, 280))
    pressContinue = font.render (f"Press anywhere to continue...", True, (255, 255, 255))
    background.blit (pressContinue, (170, 400))
    
    pygame.display.flip()
    
    screen.blit (background, (0,0))
    
    # Stops the music
    pygame.mixer.music.stop()
    
    # A - Action (broken into ALTER steps)
     
        # A - Assign values to key variables
    clock = pygame.time.Clock()
    check = True
    # Loop
    while check:
        
        # Time
        clock.tick (30)
        
        # Event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                check = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                check = False
        crosshair.reset(pygame.mouse.get_pos())
                
        # R - Refresh display
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        pygame.display.flip()  
        
        # Hide the mouse pointer
        pygame.mouse.set_visible(False)        
    return datakeeper

def main():
    '''This function is the mainline logic of the program.'''       
    keepGoing = True
    # Continue the game until the user quits the menu screen
    while keepGoing:
        keepGoing, datakeeper = menu()
        if keepGoing:
            datakeeper = game(datakeeper)
            gameOver (datakeeper)                
    pygame.quit()
    
# Starts the program            
main()