# Speed

import pygame, sys, time, random
from pygame.locals import *

# User-defined classes

class Dot:
   bgColor = pygame.Color('black')
   bColor = pygame.Color('blue')
   rColor = pygame.Color('red')
   maxSpeed = 4
   minSpeed = 1

   def __init__(self, surface):
      self.surface = surface
      self.center = [250, 200]
      self.radius = 30
      self.color = Dot.bColor
      self.speed = [1, 1]
      
   def moveDot(self):
      size = self.surface.get_size()
      for coord in range(2):
         self.center[coord] = self.center[coord] + self.speed[coord]
         if self.center[coord] < self.radius: # check left or top
            self.speed[coord] = -self.speed[coord]
         if self.center[coord] + self.radius > size[coord]:
            self.speed[coord] = -self.speed[coord]
   
   def draw(self):
      if self.speed[0] or self.speed[1] != 0:
         pygame.draw.circle(self.surface, self.color, self.center, self.radius)
      else:
         pygame.draw.circle(self.surface, Dot.rColor, self.center, self.radius)
   
   def randomizeSpeed(self):
      for coord in range(2):
         self.speed[coord] = random.randint(Dot.minSpeed, Dot.maxSpeed)
      
   def handleKey(self, key): 
      if key == K_a:
         self.speed[0] -= 1
      if key == K_d:
         self.speed[0] += 1
      if key == K_w:
         self.speed[1] += 1
      if key == K_s:
         self.speed[1] -= 1
         
   def update(self):
      if False:
         return True
      else:
         self.surface.fill(Dot.bgColor)
         self.moveDot()
         self.draw()
         return False
         
# User-defined functions

def main():

   # Initialize pygame
   pygame.init()

   # Set window size and title, and frame delay
   surfaceSize = (500, 400) # example window size
   windowTitle = 'Speed' # example title
   frameDelay = 0.02 # smaller is faster game

   # Create the window
   surface = pygame.display.set_mode(surfaceSize, 0, 0)
   pygame.display.set_caption(windowTitle)

   # create and initialize objects
   gameOver = False
   dot = Dot(surface)

   # Draw Objects
   dot.randomizeSpeed()
   dot.draw()
   
   # Refresh the display
   pygame.display.update()

   # Loop forever
   while True:
      # Handle events
      for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            sys.exit()
         # Handle additional events
         if event.type == KEYDOWN and not gameOver:
            dot.handleKey(event.key)

      # Update and draw objects for the next frame
      dot.update()

      # Refresh the display
      pygame.display.update()

      # Set the frame speed by pausing between frames
      time.sleep(frameDelay)

main()
