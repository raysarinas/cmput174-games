# Pong V3
# Description/Summary

import pygame, sys, time
from pygame.locals import *

# User-defined classes

# User-defined functions

def main():

   # Initialize pygame
   pygame.init()
   pygame.key.set_repeat(20, 20)

   # Set window size and title, and frame delay
   surfaceSize = (500, 400)
   windowTitle = 'Pong V3'
   frameDelay = 0.01

   # Create the window
   surface = pygame.display.set_mode(surfaceSize, 0, 0)
   pygame.display.set_caption(windowTitle)

   # create and initialize objects
   gameOver = False
   x = surface.get_width()
   y = surface.get_height()
   center = [x//2, y//2]
   bgColor = pygame.Color('black')
   fgColor = pygame.Color('white')
   
   # Paddles
   paddleSize = [10, 50]
   recHeight = (y - paddleSize[1])//2
   leftPaddle = pygame.Rect(100, recHeight, paddleSize[0], paddleSize[1])
   rightPaddle = pygame.Rect(x-100, recHeight, paddleSize[0], paddleSize[1])
   
   # Ball
   radius = 5
   speed = [4, 1]

   # Score
   score = [0, 0]

   # Moving the Paddles
   move = 10

   # Draw objects
   pygame.draw.circle(surface, fgColor, center, radius)
   pygame.draw.rect(surface, fgColor, leftPaddle)
   pygame.draw.rect(surface, fgColor, rightPaddle)

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
            keyDown(event, leftPaddle, rightPaddle, move, surface)

      # Update and draw objects for the next frame
      gameOver = update(surface, bgColor, center, radius, speed, leftPaddle, rightPaddle, fgColor, score)

      # Refresh the display
      pygame.display.update()

      # Set the frame speed by pausing between frames
      time.sleep(frameDelay)

def update(surface, bgColor, center, radius, speed, leftPaddle, rightPaddle, fgColor, score):
   # Check if the game is over. If so, end the game and return True. Otherwise, update the game objects, draw them, and return False.

   maxScore = 11
   if score[0] == maxScore or score[1] == maxScore: # check if the game is over
      drawScore(surface, score, fgColor, bgColor)
      return True
   else: # continue the game
      surface.fill(bgColor)
      moveBall(center, radius, speed, leftPaddle, rightPaddle, surface, score)
      pygame.draw.circle(surface, fgColor, center, radius)
      pygame.draw.rect(surface, fgColor, leftPaddle)
      pygame.draw.rect(surface, fgColor, rightPaddle)
      drawScore(surface, score, fgColor, bgColor)
      return False

def moveBall(center, radius, speed, leftPaddle, rightPaddle, surface, score):
   # Moves the ball by changing the center of the ball by its speed.
   # Ensures ball remains on surface by making it bounce off the edges of the surface.
   
   size = surface.get_size()
   
   for coord in range(0,2):
      center[coord] = center[coord] + speed[coord]

      if center[coord] < radius:
         speed[coord]= -speed[coord]
         if coord == 0:
            score[1] = score[1] + 1

      if center[coord] + radius > size[coord]:
         speed[coord]= -speed[coord]
         if coord == 0:
            score[0] = score[0] + 1
              
      if rightPaddle.collidepoint(center) and speed[0] > 0:
         speed[coord] = -speed[coord]

      if leftPaddle.collidepoint(center) and speed[0] < 0:
         speed[coord] = -speed[coord]

def drawScore(surface, score, fgColor, bgColor):
   fontSize = 70
   leftScore = [0, 0]
   width = surface.get_width()
   font = pygame.font.SysFont(None, fontSize, True)
   
   textSurfaceLeft = font.render(str(score[0]), True, fgColor)
   surface.blit(textSurfaceLeft, leftScore)
   
   textSurfaceRight = font.render(str(score[1]), True, fgColor)
   textSurfaceRight_width = textSurfaceRight.get_width()
   rightScore = [width - textSurfaceRight_width, 0]
   surface.blit(textSurfaceRight, rightScore)

def movePaddleUp(paddle, move, surface):
   # Move a paddle up but only up to the edge of the surface.
   if paddle.top < move:
      move = paddle.top
   paddle.move_ip(0, -move)

def movePaddleDown(paddle, move, surface):
   # Move a paddle down but only up to the edge of the surface.
   maxDown = surface.get_height()
   if maxDown - paddle.bottom < move:
      move = maxDown - paddle.bottom
   paddle.move_ip(0, move)

def keyDown(event, leftPaddle, rightPaddle, move, surface):
   # Responding to a player pressing down a key that results in a corresponding action, i.e. paddle moves up or down depending on the key that is held/pressed down.
   if event.key == K_q:
      movePaddleUp(leftPaddle, move, surface)
   
   if event.key == K_a:
      movePaddleDown(leftPaddle, move, surface)

   if event.key == K_p:
      movePaddleUp(rightPaddle, move, surface)
      
   if event.key == K_l:
      movePaddleDown(rightPaddle, move, surface)

main()