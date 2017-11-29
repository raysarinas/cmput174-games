# Memory Version 3

import pygame, sys, time, random
from pygame.locals import *
pygame.init()

# User-defined classes

class Tile:
# Class Attributes
   bgColor = pygame.Color('black')
   borderWidth = 4 # the pixel width of the tile border
   coverImage = pygame.image.load('image0.bmp')

   def __init__(self, x, y, image, surface):
      self.image = image
      self.location = (x , y)
      self.surface = surface
      self.tileExposed = False

   def __eq__(self, otherTile):
      if self is None or otherTile is None:
         return False
      else :
         return (self.image == otherTile.image)

   def isTileExposed(self):
      self.tileExposed = True

   def draw(self):
      if self.tileExposed:
         self.surface.blit(self.image, self.location)
      else:
         self.surface.blit(Tile.coverImage, self.location)
      size = self.image.get_size()
      rectangle = pygame.Rect(self.location, size) 
      pygame.draw.rect(self.surface, Tile.bgColor, rectangle, Tile.borderWidth) 

   def cursorPosition(self, position):
      size = self.image.get_size()
      rectangle = pygame.Rect(self.location, size) 
      if not self.tileExposed and rectangle.collidepoint(position):
         return True
      else:
         return False

   def hideTile(self): # hide tileImage behind coverImage # need to define this function because can’t access tileExposed attribute inside Memory class (since it is an instance attribute)
      self.tileExposed = False
      
class Memory:
# Class Attributes
   boardSize = 4
   img = 'image'
   bmp = '.bmp'
   number_of_images = 9 # actually 8 images but +1 so range function works
   showTime = 1 # number of seconds to expose the tile

   def __init__(self, surface):
      self.surface = surface
      self.board = []
      self.bgColor = pygame.Color('black')
      self.fgColor = pygame.Color('white')
      self.exposedTiles = 0
      self.makeImages()
      self.makeTiles()
      self.clickedTiles = None


   def makeImages(self):
      self.images = []
      for index in range(1, Memory.number_of_images):
         file = Memory.img + str(index) + Memory.bmp
         image = pygame.image.load(file)
         self.images.append(image)
      self.images = 2 * self.images
      random.shuffle(self.images)

   def makeTiles(self):
      for rowIndex in range(0, Memory.boardSize):
         row = []
         for colIndex in range(0, Memory.boardSize):
            i = rowIndex * Memory.boardSize + colIndex # i is the image index
            image = self.images[i]
            width = image.get_width()
            height = image.get_height()
            x = colIndex * width
            y = rowIndex * height
            tile = Tile(x, y, image, self.surface)
            row.append(tile)
         self.board.append(row)

   def draw(self):
      self.surface.fill(self.bgColor)
      for row in self.board:
         for tile in row:
            tile.draw()
      self.drawScore()

   def drawScore(self):
      fontSize = 75
      font = pygame.font.SysFont(None, fontSize, True)
      time = pygame.time.get_ticks() // 1000 # divide to convert to seconds
      textSurface = font.render(str(time), True, self.fgColor, self.bgColor)
      textWidth = textSurface.get_width()
      surfaceWidth = self.surface.get_width()
      textLocation = (surfaceWidth - textWidth, 0)
      self.surface.blit(textSurface, textLocation)

   def tilePosition(self, position):
      # Return the tile that has been clicked which contained the cursor; this tile is returned so the handleMouseUp method can use it. Otherwise, return None.
      for row in self.board:
         for tile in row:
            if tile.cursorPosition(position):
               return tile
      return None

   def update(self):
      if self.isGameOver():
         return True
      else:
         self.draw()
         return False

   def handleMouseUp(self, position):
      tile = self.tilePosition(position)
      if tile is not None and tile is not self.clickedTiles:
         tile.isTileExposed()
         if self.clickedTiles is None: # if there are no tiles that have been clicked
            self.clickedTiles = tile # set clickedTiles to the tile that has been clicked on/exposed.
         elif tile == self.clickedTiles : # ELIF tiles are matching
            self.clickedTiles = None # reset so can click 2 more tiles
            self.exposedTiles += 1
            tile.draw()
         else : # else, if tiles don’t match
            tile.draw()
            pygame.display.update()
            time.sleep(Memory.showTime)
            tile.hideTile()
            self.clickedTiles.hideTile() # use hide method and call it on the 2 selected mismatched/not matching tiles
            self.clickedTiles = None # reset to None so can click more tiles

   def isGameOver(self):
      totalTilePairs = Memory.boardSize * 2 # clickedTiles method returns the number of tiles as pairs rather than as individual tiles
      return self.exposedTiles == totalTilePairs

def main():
   # Initialize pygame
   pygame.init()
         
   # Set window size and title, and frame delay
   surfaceSize = (500, 400)
   windowTitle = 'Memory V3'
   pauseTime = 0.01 # smaller is faster game
         
   # Create the window
   surface = pygame.display.set_mode(surfaceSize, 0, 0)
   pygame.display.set_caption(windowTitle)
         
   # create and initialize objects
   gameOver = False
   game = Memory(surface)
         
   # Draw objects
   game.draw()
         
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
            game.handleMouseUp(event.pos)
         
      # Update and draw objects for next frame
      gameOver = game.update()
         
      # Refresh the display
      pygame.display.update()
         
      # Set the frame speed by pausing between frames
      time.sleep(pauseTime)
      
main()