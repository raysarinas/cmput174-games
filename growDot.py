# Grow

import pygame, sys, time
from pygame.locals import *

# User-defined classes

class Dot:
   bgColor = pygame.Color('black')
   bColor = pygame.Color('blue')
   rColor = pygame.Color('red')

   def __init__(self, surface):
      self.surface = surface
      self.center = [250, 200]
      self.radius = 30
      self.color = Dot.bColor
      self.rect = None
      self.clickedCircle = False
      
   def draw(self):
      self.rect = pygame.draw.circle(self.surface, self.color, self.center, self.radius)
      
   def handleMouseClick(self, position): 
      if self.rect.collidepoint(position):
         self.clickedCircle = True
      else:
         self.clickedCircle = False
         
   def growCircle(self):
      if self.clickedCircle:
         self.radius = self.radius // 2
      else:
         self.radius = self.radius * 2
      
   def handleMouseUp(self, position):
      self.handleMouseClick(position)
      self.growCircle()
      
   def handleKey(self, key): 
      if self.clickedCircle: 
         if key == K_r:
            self.color = Dot.rColor
         if key == K_b:
            self.color = Dot.bColor
         
   def update(self):
      if False:
         return True
      else:
         self.surface.fill(Dot.bgColor)
         self.draw()
         return False
         
# User-defined functions

def main():

   # Initialize pygame
   pygame.init()

   # Set window size and title, and frame delay
   surfaceSize = (500, 400) # example window size
   windowTitle = 'Grow' # example title
   frameDelay = 0.02 # smaller is faster game

   # Create the window
   surface = pygame.display.set_mode(surfaceSize, 0, 0)
   pygame.display.set_caption(windowTitle)

   # create and initialize objects
   gameOver = False
   dot = Dot(surface)

   # Draw Objects
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
         if event.type is MOUSEBUTTONUP and not gameOver:
            dot.handleMouseUp(event.pos)

      # Update and draw objects for the next frame
      dot.update()

      # Refresh the display
      pygame.display.update()

      # Set the frame speed by pausing between frames
      time.sleep(frameDelay)

main()
