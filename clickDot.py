# Click the Dot

import pygame, sys, time, math, random
from pygame.locals import *

# User-defined classes

# User-defined functions

def main():

   # Initialize pygame
   pygame.init()

   # Set window size and title, and frame delay
   surfaceSize = (500, 400) # example window size
   windowTitle = 'Click The Dot' # example title
   frameDelay = 0.03 # smaller is faster game

   # Create the window
   bgColor = pygame.Color('black')
   surface = pygame.display.set_mode(surfaceSize, 0, 0)
   pygame.display.set_caption(windowTitle)

   # create and initialize objects
   gameOver = False
   center = [50, 75]
   radius = 30
   color = pygame.Color('red')
   speed = [2, 1]
   
   # Set count values
   count = [0]
   maxCount = 5

   # Draw objects
   pygame.draw.circle(surface, color, center, radius, 0)

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
         if event.type == MOUSEBUTTONUP and not gameOver:
            handleMouseUp(event.pos, center, radius, count)

      # Update and draw objects for the next frame
      gameOver = update(surface, bgColor, color, center, radius, speed, count, maxCount)

      # Refresh the display
      pygame.display.update()

      # Set the frame speed by pausing between frames
      time.sleep(frameDelay)

def update(surface, eraseColor, dotColor, dotCenter, radius, speed, count, maxCount):
   # Check if the game is over. If so, end the game and
   # returnTrue. Otherwise, update the game objects, draw
   # them, and return False.
   # This is an example update function - replace it.
   # - center is a list containing the x and y int coords
   # of the center of a circle
   # - surface is the pygame.Surface object for the window

   if count[0] == maxCount: # check if the game is over
      drawScore(surface, eraseColor, count)
      return True
   else: # continue the game
      surface.fill(eraseColor)
      moveDot(surface, dotCenter, radius, speed)
      pygame.draw.circle(surface, dotColor, dotCenter, radius, 0)
      drawScore(surface, eraseColor, count)
      return False

def moveDot(surface, center, dotRadius, speed):
   for coord in range(2):
      center[coord] = center[coord] + speed[coord]
      if center[coord] < dotRadius:
         speed[coord] = -speed[coord]
      size = surface.get_size()
      if center[coord] + dotRadius > size[coord]:
         speed[coord] = -speed[coord]
      
def handleMouseUp(position, center, radius, count):
   X = position[0] - center[0]
   Y = position[1] - center[1]
   distance = math.sqrt(X**2 + Y**2)
   if distance <= radius:
      count[0] = count[0] + 1
   if distance > radius:
      if count[0] != 0:
         count[0] = count[0] - 1
         
def randomizeDot(surface, radius, dotCenter):
   size = surface.get_size()
   for coord in range(2):
      dotCenter = random.randint(radius, size[coord] - radius)

def drawScore(surface, bgColor, count):
   fgColor = pygame.Color('white')
   fontSize = 50
   displayString = 'Score: ' + str(count[0])
   font = pygame.font.SysFont(None, fontSize, True)
   textSurface = font.render(displayString, True, fgColor, bgColor)
   location = (0, 0)
   surface.blit(textSurface, location)
   
main()