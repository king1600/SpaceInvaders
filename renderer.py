import time
import pygame
from color import Color

class Renderer:
  """ Helper class for drawing rects to screen """

  def __init__(self, game):
    """ Initialize render variables """
    self.game      = game
    self.timer     = pygame.time.Clock()
    self.started   = time.time()
    self.delta     = time.time() - (self.started + 1)
    self.c_color   = Color.BLACK()
    self.color     = self.c_color
    self.init_size = self.game.size
    self.ready     = [False, self.game.fps/8, 0]

  def sync(self, fps):
    """ limit time by fps """
    self.timer.tick(fps)

  def begin(self):
    """ clear screen and start drawing new frame """
    self.game.window.fill(self.c_color.get())
    self.started = time.time()

  def end(self):
    """ end frame an process """
    pygame.display.flip()
    self.delta = time.time() - self.started
    if not self.ready[0]:
      self.ready[2] += 1
      if self.ready[2] >= self.ready[1]:
        self.ready[0] = True

  def set_color(self, color):
    """ set the draw color """
    self.color = color

  def draw_rect(self, x, y, w, h):
    """ helper function to draw rect scalable """
    x = (self.game.width * x * 1.) / self.init_size[0]
    y = (self.game.height * y * 1.) / self.init_size[1]
    w = (self.game.width * w * 1.) / self.init_size[0]
    h = (self.game.height * h * 1.) / self.init_size[1]
    pygame.draw.rect(self.game.window, self.color.get(), (x, y, w, h), 0)
