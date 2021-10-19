# I - Import and Initialize
import pygame, myPacmanSprites
pygame.init()
pygame.mixer.init()
 
def main():
   '''This function defines the 'mainline logic' for our game.'''
    
   # Display
   screen = pygame.display.set_mode((640, 480))
   pygame.display.set_caption("Pacman")
     
   # Entities
   background = pygame.Surface(screen.get_size())
   background.fill((255, 255, 255))
   screen.blit(background, (0, 0))
   
   directionX = 5
   directionY = 0
   
   # Sounds effects
   eat = pygame.mixer.Sound("PacmanEating.WAV")
   eat.set_volume(0.5)
 
   # Create 10 random cherries using a loop and a list
   cherries = []
   for i in range(10):
      cherries.append(myPacmanSprites.Cherry(screen))
   
   pacman = myPacmanSprites.Pacman(screen, directionX, directionY)
   allCherries = pygame.sprite.OrderedUpdates(cherries)
     
   # Add list of Sprites to one OrderedUpdates Sprite Group
   allSprites = pygame.sprite.OrderedUpdates(cherries, pacman)
     
   # ACTION
     
   # Assign 
   keepGoing = True
   clock = pygame.time.Clock()
    
   # Loop
   while keepGoing:
     
      # Time
      clock.tick(30)
     
      # Events
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            keepGoing = False
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
               pacman.go_up()
            if event.key == pygame.K_DOWN:
               pacman.go_down()
            if event.key == pygame.K_LEFT:
               pacman.go_left()         
            if event.key == pygame.K_RIGHT:
               pacman.go_right()         
               
      # Multiple-Sprite Collision Detection and Reporting
      collision = pygame.sprite.spritecollide(pacman, allCherries, False)
      if collision:
         for i in collision:
            eat.play()
            i.kill()

      if len(allCherries) == 0:
         cherries = []
         for i in range(10):
            cherries.append(myPacmanSprites.Cherry(screen))
         allCherries = pygame.sprite.OrderedUpdates(cherries)
         allSprites = pygame.sprite.OrderedUpdates(cherries, pacman)

      # Refresh screen
      allSprites.clear(screen, background)
      allSprites.update()
      allSprites.draw(screen)
         
      pygame.display.flip()
 
   # Close the game window
   pygame.quit()     
       
# Call the main function
main()
