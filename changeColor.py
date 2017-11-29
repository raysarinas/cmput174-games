# Color
# In this game, the player can change the color of a dot at the center
# of the game window by pressing a key after clicking the the dot.
# If the click is outside the dot, the color of the dot does not change.

import pygame, sys, time
from pygame.locals import *

# User-defined classes

class Dot:
   bgColor = pygame.Color('black')
   rColor = pygame.Color('red')
   bColor = pygame.Color('blue')
   yColor = pygame.Color('yellow')
   
   def __init__(self, surface): 
      self.surface = surface
      self.radius = 25
      self.center = [250, 200]
      self.color = Dot.bColor
      self.clicked = False
      self.rect = None
      
   def draw(self):
      self.rect = pygame.draw.circle(self.surface, self.color, self.center, self.radius)
      
   def handleMouseClick(self, position):
      if self.rect.collidepoint(position):
         self.clicked = True
      else: 
         self.clicked = False
   
   def handleMouseUp(self, position):
      self.handleMouseClick(position)
      
   def handleKey(self, key):
      if self.clicked:
         if key == K_r:
            self.color = Dot.rColor
         if key == K_b:
            self.color = Dot.bColor
         if key == K_y:
            self.color = Dot.yColor
         
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
   windowTitle = 'Color' # example title
   frameDelay = 0.02 # smaller is faster game

   # Create the window
   surface = pygame.display.set_mode(surfaceSize, 0, 0)
   pygame.display.set_caption(windowTitle)

   # create and initialize objects
   gameOver = False
   color = Dot(surface)

   # Draw objects

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
            color.handleKey(event.key)
         if event.type == MOUSEBUTTONUP and not gameOver:
            color.handleMouseUp(event.pos)

      # Update and draw objects for the next frame
      gameOver = color.update()

      # Refresh the display
      pygame.display.update()

      # Set the frame speed by pausing between frames
      time.sleep(frameDelay)

main()