from random import randint

class Color:
  """ Basic color object """

  def __init__(self, r=0, g=0, b=0):
    self.r, self.g, self.b = r, g, b

  def get(self):
    """ Get the color values as tuple """
    return (self.r, self.g, self.b)

### Static Colors ###

  @staticmethod
  def BLACK():
    return Color(0, 0, 0)

  @staticmethod
  def RED():
    return Color(255, 0, 0)

  @staticmethod
  def GREEN():
    return Color(0, 255, 0)

  @staticmethod
  def BLUE():
    return Color(0, 0, 255)

  @staticmethod
  def WHITE():
    return Color(255, 255, 255)

  @staticmethod
  def Rand():
    args = (randint(0,255) for _ in range(3))
    return Color(*args)