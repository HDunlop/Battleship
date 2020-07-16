class Ship(object):

  def __init__(self,name,size,coords:list=[],hitCount:int=0,sunk:bool=False):
    self.name = name
    self.size = size
    self.coords = coords
    self.hitCount = hitCount
    self.sunk = sunk

  def addCoords(self,coords):
    self.coords = coords

  def checkDidHit(self,coord):
    if coord in self.coords:
      self.hitCount += 1
      if self.hitCount == self.size:
        self.sunk = True
      if self.sunk:
        return 2
      return 1
    return 0
