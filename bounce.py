# Bounce

import pygame, sys, time, math, random
from pygame.locals import *

# User-defined classes

# User-defined functions

def main():

   # Initialize pygame
   pygame.init()

   # Set window size and title, and frame delay
   surfaceSize = (500, 400) # example window size
   windowTitle = 'Bounce'
   frameDelay = 0.02 # smaller is faster game

   # Create the window
   surface = pygame.display.set_mode(surfaceSize, 0, 0)
   pygame.display.set_caption(windowTitle)

   # create and initialize objects
   gameOver = False
   centers = [[375, 350]]
   cueCenter = [275, 200]
   radius = 20
   speed = [2, 1]
   color = pygame.Color('black')
   cueColor = pygame.Color('red')
   bgColor = pygame.Color('white')

   # Draw objects
   
   draw(cueCenter, cueColor, centers, color, radius, bgColor, surface)

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

      # Update and draw objects for the next frame
      gameOver = update(cueCenter, cueColor, centers, color, radius, bgColor, speed, surface)

      # Refresh the display
      pygame.display.update()

      # Set the frame speed by pausing between frames
      time.sleep(frameDelay)

def update(movingCenter, movingColor, fixedCenters, fixedColor, radius, bgColor, speed, surface):
   centersMax = 5
   if len(fixedCenters) == centersMax: # check if the game is over
      return True
   else: # continue the game
      surface.fill(bgColor)
      moveBall(movingCenter, radius, speed, surface)
      collisions(movingCenter, fixedCenters, radius, surface)
      draw(movingCenter, movingColor, fixedCenters, fixedColor, radius, bgColor, surface)
      return True
   
def moveBall(center, radius, speed, surface):
   size = surface.get_size()
   for coord in range(2):
      center[coord] = center[coord] + speed[coord]
      # check left or top
      if center[coord] < radius:
         speed[coord] = -speed[coord]
      # check right or bottom
      if center[coord] + radius > size[coord]:
         speed[coord] = -speed[coord]

def draw(movingCenter, movingColor, fixedCenters, fixedColor, radius, bgColor, surface):
   pygame.draw.circle(surface, movingColor, movingCenter, radius, 0)
   for center in fixedCenters:
      pygame.draw.circle(surface, fixedColor, center, radius, 0)

def randomize(center, radius, surface):
   size = surface.get_size()
   for coord in range(2):
      center[coord] = random.randint(radius, size[coord] - radius)

def collisions(movingCenter, fixedCenters, radius, surface):
   for centers in fixedCenters:
      if ballsIntersect(movingCenter, centers, radius):
         newCenter = [0, 0]
         randomize(newCenter, radius, surface)
         fixedCenters.append(newCenter)
         randomize(movingCenter, radius, surface)

def ballsIntersect(center2, center1, radius):
   distanceX = center2[0] - center1[0]
   distanceY = center2[1] - center1[1]
   distance = math.sqrt(distanceX**2 + distanceY**2)
   return distance <= 2 * radius

main()
