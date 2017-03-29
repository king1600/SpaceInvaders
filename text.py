from color import Color

def getSlots(char):
  """ Get active slots for each character """

  if char == 'A':
    active = [1,2,3,4,6,7,8,9,10,12,13,15]
  elif char == 'C':
    active = [1,2,3,4,7,10,13,14,15]
  elif char == 'E':
    active = [1,2,3,4,7,8,9,10,13,14,15]
  elif char == 'H':
    active = [1,3,4,6,7,8,9,10,12,13,15]
  elif char == 'I':
    active = [1,2,3,5,8,11,13,14,15]
  elif char == 'L':
    active = [1,4,7,10,13,14,15]
  elif char == 'O':
    active = [1,2,3,4,6,7,9,10,12,13,14,15]
  elif char == 'R':
    active = [1,2,3,4,6,7,8,10,12,13,15]
  elif char == 'S':
    active = [1,2,3,4,7,8,9,12,13,14,15]
  elif char == 'V':
    active = [1,3,4,6,7,9,11,14]
  elif char == ' ':
    active = []
  elif char == ':':
    active = [2,14]
  elif char == '0':
    active = [1,2,3,4,6,7,9,10,12,13,14,15]
  elif char == '1':
    active = [1,2,5,8,11,13,14,15]
  elif char == '2':
    active = [1,2,3,6,7,8,9,10,13,14,15]
  elif char == '3':
    active = [1,2,3,6,7,8,9,12,13,14,15]
  elif char == '4':
    active = [1,3,4,6,7,8,9,12,15]
  elif char == '5':
    active = [1,2,3,4,7,8,9,12,13,14,15]
  elif char == '6':
    active = [1,2,3,4,7,8,9,10,12,13,14,15]
  elif char == '7':
    active = [1,2,3,6,9,11,13]
  elif char == '8':
    active = [1,2,3,4,6,7,8,9,10,12,13,14,15]
  elif char == '9':
    active = [1,2,3,4,6,7,8,9,12,13,14,15]
  else:
    active = []
  slots = [0 for _ in range(15)]
  for i in active: slots[i - 1] = 1
  return slots

class Text:
  """ Retro ASCII text object """
  
  def __init__(self, string, x=0, y=0, w=0, h=0):
    self.color = Color.WHITE()
    self.x, self.y, self.w, self.h = x, y, w, h
    self.set_text(string)

  def set_text(self, text):
    """ Redo calculations """
    self.string = str(text).upper()
    cols = (len(self.string) * 3) + (len(self.string) - 1)
    self.unit_y = int(round(self.h / 5.0,1))
    self.unit_x = int(round(self.w / cols,1))

    # generate characters
    self.chars = [getSlots(char) for char in self.string]

  def draw(self, batch=None):
    """ Draw the text """

    # setup variables for drawing
    x, y, w, h = self.x, self.y, self.w, self.h
    batch.set_color(self.color)

    # loop through character values
    for pos, char in enumerate(self.chars):
      init_x, init_y = x, y

      # draw each letter
      for i, active in enumerate(char):
        x, y = int(x), int(y)
        active = True if active == 1 else False
        if active:
          batch.draw_rect(x, y, self.unit_x, self.unit_y)
        x += self.unit_x
        if (i + 1) % 3 == 0:
          y += self.unit_y
          x = init_x

      # add space for next character
      if pos != len(self.chars) - 1:
        x, y = init_x + (4 * self.unit_x), init_y