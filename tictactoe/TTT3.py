# Tic Tac Toe V3

import pygame, sys, time
from pygame.locals import *

# User-defined classes

class Tile:
   # Class Attributes
   pygame.init()
   fgColor = pygame.Color('white')
   bgColor = pygame.Color('black')
   fontSize = 100
   font = pygame.font.SysFont(None,fontSize,True)
   borderWidth = 3
   
   def __init__(self, x, y, width, height):
      self.rect = pygame.Rect(x, y, width, height)
      self.content = ''

   def __eq__(self, otherTile): # indicates special method in which python offers operator '=='
      if self.content != '' and self.content == otherTile.content:
         return True
      else:
         return False
   
   def handleMouseUp(self, position, surface, turn): # made into thumbs up or thumbs down function by adding return True/False
      if self.rect.collidepoint(position):
         if self.content == '':
            self.content = turn
            return True # valid click; unoccupied tile
         else: # not a valid click - click inside an occupied tile
            self.flash(surface)
            return False
         
   def flash(self,surface):
      pygame.draw.rect(surface, Tile.fgColor, self.rect)
      pygame.display.update()
      time.sleep(0.05)
      self.draw(surface)
       
   def draw(self, surface):
      pygame.draw.rect(surface, Tile.bgColor, self.rect, 0)
      pygame.draw.rect(surface, Tile.fgColor, self.rect, Tile.borderWidth)
      textSurface = Tile.font.render(self.content, True, Tile.fgColor, Tile.bgColor)
      textRectangle = textSurface.get_rect()
      # Setting the center of textRectangle to the center of the tile
      textRectangle.center = self.rect.center
      # location = self.rect.center # THIS IS WRONG
      surface.blit(textSurface, textRectangle)

class Cursor:
   def __init__(self, filename):
      infile = open(filename, 'r')
      longString = infile.read()
      alist = longString.splitlines()
      compiled = pygame.cursors.compile(alist, '*', '.')
      self.data = compiled[0]
      self.mask = compiled[1]
      height = len(alist)
      width = len(alist[0])
      self.size = (width, height)
      self.hotspot = (width // 2, height // 2)
      
   def activate(self):
      pygame.mouse.set_cursor(self.size, self.hotspot, self.data, self.mask)
   
class TTT:
   # Class Attributes
   boardSize = 3 # or [3, 3] or (3, 3)
   
   def __init__(self,surface):
      self.cursorx = Cursor('cursorx.txt')
      self.cursoro = Cursor('cursoro.txt')      
      self.surface = surface
      self.filled = []
      self.flashers = []
      self.turn = 'X'
      self.cursorx.activate()
      width = self.surface.get_width() // TTT.boardSize
      height = self.surface.get_height() // TTT.boardSize
      self.board = [] # more than 1 object inside like a chest of drawers; use a list
      for rowIndex in range(0, TTT.boardSize): # i is the rowIndex
         row = []
         for colIndex in range(0, TTT.boardSize):
            x = colIndex * width
            y = rowIndex * height
            myTile=Tile(x, y, width, height)
            row.append(myTile)
         self.board.append(row)
            
   def draw(self): # self is a keychain with instance attributes hanging
      for row in self.board:
         for everyTile in row:
            everyTile.draw(self.surface)
      
   def handleMouseUp(self,position):
      for row in self.board:
         for everyTile in row:
            if everyTile.handleMouseUp(position, self.surface, self.turn) == True: # board needs to pass who's turn bc Tile doesn't know. # Want to know if valid click inside occupied/unoccupied click? Change turns/don't change turns.
               self.filled.append(everyTile)
               self.changeTurn()

   def changeTurn(self):
      if self.turn == 'X':
         self.turn = 'O'
         self.cursoro.activate()
      else:
         self.turn = 'X'
         self.cursorx.activate()

   def isGameOver(self):
      return self.isWin() or self.isTie()
   
   def flash(self): # ask a smaller component to flash # simply flashes all tiles that need to be flashed
      for aTile in self.flashers:
         aTile.flash(self.surface)

   def isWin(self):
      return self.isRowWin() or self.isColumnWin() or self.isDiagonalWin()
   
   def isListWin(self, aList):
      if aList[0] == aList[1] == aList[2]: # determines there is a rowWin or not
         self.flashers = aList
         return True
      else:
         return False
      
   def isRowWin(self): # walk through rows and throws that list to isListWin method to determine whether or not we have a winning set
      for row in self.board:
         if self.isListWin(row) == True: # if enter row is True
            return True # Need to check every row before saying it's False so should not have an Else/Return False thing
      return False #should not return False unless ALL rows are checked for True
   
   def isColumnWin(self):
      for colIndex in range(TTT.boardSize):
         column = []
         for rowIndex in range(TTT.boardSize):
            tile = self.board[rowIndex][colIndex]
            column.append(tile)
         if self.isListWin(column) == True:
            return True
      return False # only when done checking all columns   
   
   def isDiagonalWin(self): 
      diagonal1 = [self.board[0][0], self.board[1][1], self.board[2][2]]
      diagonal2 = [self.board[0][2], self.board[1][1], self.board[2][0]]
      if self.isListWin(diagonal1) == True or self.isListWin(diagonal2) == True:
         return True
      else:
         return False
   
   def isTie(self):
      if len(self.filled) == TTT.boardSize ** 2:
         self.flashers = self.filled
         return True
      else: 
         return False

   def update(self):
      if self.isGameOver():
         self.flash()
         self.draw()
         return True
      else:
         self.draw()
         return False

def main():

   # Initialize pygame
   pygame.init()

   # Set window size and title, and frame delay
   surfaceSize = (500, 400) # example window size
   windowTitle = 'Tic Tac Toe' # example title
   frameDelay = 0.02 # smaller is faster game

   # Create the window
   surface = pygame.display.set_mode(surfaceSize, 0, 0)
   pygame.display.set_caption(windowTitle)

   # create and initialize objects
   gameOver = False
   game = TTT(surface)
   
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

      # Update and draw objects for the next frame
      gameOver = game.update()

      # Refresh the display
      pygame.display.update()

      # Set the frame speed by pausing between frames
      time.sleep(frameDelay)


main()