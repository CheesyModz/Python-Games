# I - IMPORT AND INITIALIZE
import pygame, Sprites
pygame.init()

def main():
     # D - DISPLAY
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Defense Simulator!")

    # E - ENTITIES
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit (background, (0,0))

    live = Sprites.lives()
    
    plane = Sprites.Character(screen)
    pandas = pygame.sprite.Group()
    for i in range (10):
        pandas.add(Sprites.Panda(screen, live))
    allSprites = pygame.sprite.OrderedUpdates (plane, pandas)

    bullet_group = pygame.sprite.Group()

    # Creates borders for the pandas
    borderTop = Sprites.Borders (screen, 0)
    borderBottom = Sprites.Borders (screen, 480)
    borderSprites = pygame.sprite.Group (borderTop, borderBottom)

    pygame.mixer.music.load("BGM.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    # A - ACTION
    # A - ASSIGN 
    clock = pygame.time.Clock()
    keepGoing = True
    score = 0
    font = pygame.font.Font("font.ttf",32)

    # L - LOOP
    while keepGoing:
     
        # T - Timer to set frame rate
        clock.tick(30)
        
        # E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                bullet = Sprites.Bullet(screen)
                bullet_group.add(bullet)
                allSprites.add(bullet)

        collisions = pygame.sprite.groupcollide(bullet_group, pandas, True, True)
        if collisions: 
            for bullet in collisions:
                bullet.kill()
                score += 1
                # generate a new panda once one is killed
                for i in range(1):
                    newPanda = Sprites.Panda(screen, live)
                    pandas.add(newPanda)
                    allSprites.add(newPanda)
        
        collisions = pygame.sprite.groupcollide(pandas, borderSprites, False, False)
        if collisions:
            for panda in collisions:
                panda.changeY()

        scoreText = font.render("Score: " + str(score), True, (0, 0, 0))
        scoreLives = font.render("Lives: " + str(live.getLives()), True, (0, 0, 0))
        screen.blit(scoreText, (0, 0))
        screen.blit(scoreLives, (475, 0))
        pygame.display.update()

         # R - Refresh display
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        bullet_group.draw(screen)
        bullet_group.update()
        # pygame.display.flip()

    pygame.quit()

main()