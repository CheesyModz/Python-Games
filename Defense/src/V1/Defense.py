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
    
    person = Sprites.Character(screen)
    pandas = []
    for i in range (10):
        pandas.append (Sprites.Panda(screen))
    allSprites = pygame.sprite.OrderedUpdates (person, pandas)

    # A - ACTION
    # A - ASSIGN 
    clock = pygame.time.Clock()
    keepGoing = True

    # L - LOOP
    while keepGoing:
     
        # T - Timer to set frame rate
        clock.tick(30)
        
        # E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    person.changeX("left")
                elif event.key == pygame.K_d:
                    person.changeX("right")
                elif event.key == pygame.K_w:  
                    person.changeY("up")
                elif event.key == pygame.K_s:  
                    person.changeY("down")
         # R - Refresh display
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        pygame.display.flip()


    pygame.quit()

main()