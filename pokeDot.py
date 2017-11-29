# Poke The Dots
# Version 4
# Summary of game.

import pygame, sys, time,math,random
from pygame.locals import *

# User-defined classes
class Dot: # a method is a function inside a class. every method is a function but not every function is a method. function has to exist in a class to be a method. 
   
   def __init__(self, color, center, radius, speed):
      self.color = color #to 'absorb' first parameter that are being passed 
      self.center = center
      self.radius = radius
      self.speed = speed
      
   def moveDot(self, surface): #Moves the dot by changing the center of the dot by its speed
      size = surface.get_size()
      for coord in range(0,2):
         self.center[coord] = self.center[coord] + self.speed[coord]
         #Detect collision with left edge or top edge
         if self.center[coord] < self.radius:
            self.speed[coord] = - self.speed[coord]
         # Detect collision with right or bottom edge
         if self.center[coord] + self.radius > size[coord]:
            self.speed[coord] = - self.speed[coord]      
   
   def randomizeDot(self,surface):
      #This function randomizes the center of the dot
      # -center is the center of the dot
      # - radius is the radius of the dot
      # - surface is pygame.Surface object 
      size = surface.get_size()
      for coord in range(0,2):
         self.center[coord] = random.randint(self.radius, size[coord] - self.radius)  
   
   def dotsIntersect(self, otherDot):
      #checks if the dots have collided - refer to Practice 6
      # Return True if the dots have collided - False otherwise
      distanceX = self.center[0] - otherDot.center[0]
      distanceY = self.center[1] - otherDot.center[1]
      distance = math.sqrt(distanceX**2 + distanceY**2)
      return distance <= self.radius + otherDot.radius
   
   def drawDot(self, surface):
      pygame.draw.circle(surface, self.color, self.center, self.radius, 0)

# User-defined functions

def main():

   # Initialize pygame
   pygame.init()

   # Set window size and title, and frame delay
   surfaceSize = (500, 400) # example window size
   windowTitle = 'Poke The Dots' # example title
   frameDelay = 0.02 # smaller is faster game

   # Create the window
   surface = pygame.display.set_mode(surfaceSize)
   pygame.display.set_caption(windowTitle)

   # create and initialize objects
   gameOver = False
   #Red Dot
   color1 = pygame.Color('red')
   center1 = [300,200]
   radius1 = 30
   speed1 = [1,2]
   #Blue Dots
   color2 = pygame.Color('blue')
   center2 = [100,200]
   radius2 = 40
   speed2 = [2,1]
   dot1 = Dot(color1, center1, radius1, speed1)
   dot2 = Dot(color2, center2, radius2, speed2)
   
   #Randomize the Dots
   dot1.randomizeDot(surface) # randomize red dot
   dot2.randomizeDot(surface) # randomize blue dot

   # Draw objects
   # The next line is an example - replace it
   dot1.drawDot(surface)
   dot2.drawDot(surface)
   
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
            handleMouseUp(surface, dot1, dot2)

      # Update and draw objects for the next frame
      gameOver = update(surface,dot1, dot2)

      # Refresh the display
      pygame.display.update()

      # Set the frame speed by pausing between frames
      time.sleep(frameDelay)

def handleMouseUp(surface, dot1, dot2):
   dot1.randomizeDot(surface)
   dot2.randomizeDot(surface)
   bgColor = pygame.Color('black')
   surface.fill(bgColor)
   dot1.drawDot(surface)
   dot2.drawDot(surface)
   drawScore(surface)

def update(surface,dot1, dot2):
   # Check if the game is over. If so, end the game and
   # return True. Otherwise, update the game objects, draw
   # them, and return False.
   
   if dot1.dotsIntersect(dot2): # check if the game is over
      drawGameOver(surface)
      return True
   else: # continue the game  - erase, move, draw
      # erase the dot
      bgColor = pygame.Color('black')
      surface.fill(bgColor)
      # move the dot
      dot1.moveDot(surface)
      dot2.moveDot(surface)
      # draw the dot
      dot1.drawDot(surface)
      dot2.drawDot(surface)
      drawScore(surface)
      return False
      
def drawGameOver(surface):
   # This function draws Game Over on the window
   # - surface - window on which we will draw Game OVer
   fontSize = 60
   fgColor = pygame.Color('red')
   bgColor = pygame.Color('blue')
   # Step 1
   displayString = 'Game Over'
   # Step 2
   font = pygame.font.SysFont(None, fontSize, True)
   # Step 3
   textSurface = font.render(displayString, True, fgColor, bgColor)
   # Step 4
   x = 0
   surface_height = surface.get_height()
   textSurface_height = textSurface.get_height()
   y = surface_height - textSurface_height
   location = (x,y)
   # Step 5
   surface.blit(textSurface,location)

def drawScore(surface):
   # This function draws the score on the window
   # - surface is the window on which the Score will be drawn
   fontSize = 50
   fgColor = pygame.Color('white')
   bgColor = pygame.Color('black')
   # Step 1
   time = pygame.time.get_ticks() // 1000
   displayString = 'Score: '+str(time)
   # Step 2
   font = pygame.font.SysFont(None, fontSize, True)
   # Step 3
   textSurface = font.render(displayString, True,fgColor,bgColor)
   # Step 4
   location = (0,0)
   # Step 5
   surface.blit(textSurface,location)

main()



