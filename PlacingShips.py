import random
import math

def defineOptions(permValues):
  options = []
  for _ in range(20):
    hori = random.randint(1,10)
    vert = random.randint(1,10)
    if (hori,vert) not in permValues:
      options.append([hori,vert])
  return options

def refineOptionsByProxToEdgeAndCentre(options,size,permValues):
  for _ in range(len(options)):
    total = 0
    current = options.pop(0)
    if ((current[0] == 1) and (current[1] == 1)) or ((current[0] == 10) and (current[1] == 10)) or ((current[0] == 1) and (current[1] == 10)) or ((current[0] == 10) and (current[1] == 1)):
      pass
    elif ((current[0] == 5) and (current[1] == 5)) or ((current[0] == 6) and (current[1] == 5)) or ((current[0] == 6) and (current[1] == 5)) or ((current[0] == 6) and (current[1] == 6)):
      pass
    elif (current[0] == 1) or (current[0] == 10) or (current[1] == 1) or (current[1] == 10):
      if random.randint(1,3) % 3 == 0:
        score,total = refineOptionsByCompass(current,size)
    else:
      score,total = refineOptionsByCompass(current,size)
    if total != 0:
      options.append([current,total,score])
  return refineOptionsByCollision(options,size,permValues)

def refineOptionsByCompass(option,size):
  fails = []

  n = option[1] - size
  e = 10 - (option[0] + size)
  s = 10 - (option[1] + size)
  w = option[0] - size

  if n < 1:
    fails.append(0)
  elif n == 0:
    fails.append(1)
  else:
    fails.append(2)

  if option[0] + size > 10:
    fails.append(0)
  elif e == 0:
    fails.append(1)
  else:
    fails.append(2)

  if option[1] + size > 10:
    fails.append(0)
  elif s == 0:
    fails.append(1)
  else:
    fails.append(2)

  if w < 1:
    fails.append(0)
  elif w == 0:
    fails.append(1)
  else:
    fails.append(2)

  tally = fails[0]+fails[1]+fails[2]+fails[3]
  return fails,tally

def refineOptionsByCollision(options,size,permValues):
  for _ in range(len(options)):
    option = options.pop(0)
    counter = 0
    x = option[0][0]
    y = option[0][1]
    for j in range(len(option[2])):
      score = option[2][j]
      if score != 0:
        end = False
        while not end:
          for i in range(size):
            if counter == 0:
              if ((x,y-i-1) in permValues) or ((x+1,y-i) in permValues) or ((x-1,y-i) in permValues) or ((x,y-size) in permValues) or ((x,y+1) in permValues) or ((x+1,y-i-1) in permValues) or ((x-1,y-i-1) in permValues) or ((x+1,y-i+1) in permValues) or ((x-1,y-i+1) in permValues):
                end = True
            elif counter == 1:
              if ((x+i+1,y) in permValues) or ((x+i,y+1) in permValues) or ((x+i,y-1) in permValues) or ((x+size,y) in permValues) or ((x-1,y) in permValues) or ((x+i+1,y+1) in permValues) or ((x+i-1,y+1) in permValues) or ((x+i+1,y-1) in permValues) or ((x+i-1,y-1) in permValues):
                end = True
            elif counter == 2:
              if ((x,y+i+1) in permValues) or ((x+1,y+i) in permValues) or ((x-1,y+i) in permValues) or ((x,y+size) in permValues) or ((x,y-1) in permValues) or ((x+1,y+i+1) in permValues) or ((x+1,y+i-1) in permValues) or ((x-1,y+i+1) in permValues) or ((x-1,y+i-1) in permValues):
                end = True
            else:
              if ((x-i-1,y) in permValues) or ((x-i,y+1) in permValues) or ((x-i,y-1) in permValues) or ((x-size,y) in permValues) or ((x+1,y) in permValues) or ((x-i+1,y+1) in permValues) or ((x-i-1,y+1) in permValues) or ((x-i+1,y+1) in permValues) or ((x-i-1,y-1) in permValues):
                end = True
          if end:
            option[1] -= score
            option[2][j] = 0
          end = True
      counter += 1
    if option[1] > 0:
      options.append(option)
  return refineOptionsByScore(options)

def refineOptionsByScore(options):
  currentTop = [0,-math.inf,0]
  currentBestDir = 0
  best = None
  if len(options) == 0:
    return None
  for option in options:
    if option[1] > currentTop[1]:
      currentTop = option
    elif (option[1] == currentTop[1]) and (random.randint(1,2) % 2 == 0):
      currentTop = option
  for i in range(len(currentTop[2])):
    direction = currentTop[2][i]
    if direction > currentBestDir:
      currentBestDir = direction
      best = [currentTop[0],i]
    elif (direction == currentBestDir) and (random.randint(1,2) % 2 == 0):
      currentBestDir = direction
      best = [currentTop[0],i]
  return best
