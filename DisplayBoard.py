import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'
import pygame

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Lindsey.ttf', 60)

def settingUpColoUUUUrs():
  global red, blue, light_blue, dark_blue, black, white

  red = pygame.Color(255, 0, 0)
  blue = pygame.Color(51,153,255)
  light_blue = pygame.Color(51,255,255)
  dark_blue = pygame.Color(51,51,255)
  black = pygame.Color(0, 0, 0)
  white = pygame.Color(255, 255, 255)

  return red,blue,black

def drawBoard():
  global rectangles,sizeBtwn,mapper,factor
  mapper = {}
  board.fill(black)
  sizeBtwn = width // rows
  factor = (sizeBtwn // 10) + 2
  x = 0 - sizeBtwn
  y = 0 - sizeBtwn
  rectangles = []
  colour = light_blue
  for vert in range(11):
    y += sizeBtwn
    for hori in range(11):
      x += sizeBtwn
      if (hori == 0) and (vert == 0):
        colour = black
      elif (hori == 0) or (vert == 0):
        colour = dark_blue
      rectangles.append(pygame.draw.rect(board, colour, (x+2,y+2,sizeBtwn-2,sizeBtwn-2), 0))
      if colour != light_blue:
        y_coord = y+factor+2
        if vert == 10:
          x_coord = x+4
        elif (vert == 0) and (hori == 9):
          x_coord = round(x+(3*factor))
        elif vert > 0:
          x_coord = round(x+(2*factor))
        elif vert == 0:
          x_coord = round(x+(1.7*factor))
        if (hori == 0) and (vert == 0):
          x_coord = 0
          y_coord = 0
      else:
        x_coord = 0
        y_coord = 0
      mapper[(hori,vert)] = [(x_coord,y_coord),x,y]
      colour = light_blue
    x = 0 - sizeBtwn
  pygame.display.update()
  return mapper,sizeBtwn

def settingUpBoard():
  global width, rows, board, moves
  width = 550
  size = (width,width)
  rows = 11
  board = pygame.display.set_mode(size)
  pygame.display.set_caption("Battleship")
  return drawBoard()

def drawCoords(copy3):
  vert = 0
  for row in copy3:
    for item in row:
      if item != "0":
        hori = row.index(item)
        writeText(item,(hori,vert))
    vert += 1
  pygame.display.update()

def writeText(copy4,copy5):
  text = font.render(copy4,True,white)
  coord = mapper[copy5]
  if coord[0] != (0,0):
    board.blit(text, coord[0])

def action(x_copy,y_copy,colour):
  if type(x_copy) != int:
    for i in range(len(x_copy)):
      x_coord = mapper[(x_copy[i],y_copy[i])][1]
      y_coord = mapper[(x_copy[i],y_copy[i])][2]
      dimensions = (x_coord+2,y_coord+2,sizeBtwn-2,sizeBtwn-2)
      pygame.draw.rect(board,colour,dimensions,0)
  else:
    x_coord = mapper[(x_copy,y_copy)][1]
    y_coord = mapper[(x_copy,y_copy)][2]
    dimensions = (x_coord+2,y_coord+2,sizeBtwn-2,sizeBtwn-2)
    pygame.draw.rect(board,colour,dimensions,0)
  pygame.display.update()
