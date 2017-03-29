import pygame
from color import Color

class Monster(pygame.sprite.Sprite):

  def __init__(self, size, x=0, y=0, w=0, h=0, color=None):
    super(Monster, self).__init__()
    self.speed = 150
    self.size  = size
    self.color = color if color is not None else Color.Rand()
    self.rect  = pygame.Rect(x, y, w, h)

    self.xdir = 0 # 1 for left, 0 for right
    self.down = 0 # 0 for not y 1 for going y
    self.went = 0 # when reaches h, switch xdir

  def correct(self):
    """ Make sure monster doesn't go off screen """
    if self.rect.x < 0: self.rect.x = 0
    if self.rect.x + self.rect.w > self.size[0]:
      self.rect.x = self.size[0] - self.rect.w
    if self.rect.y < 0: self.rect.y = 0
    if self.rect.y + self.rect.h > self.size[1]:
      self.rect.y = self.size[1] - self.rect.h

  def update(self, delta):
    """ Monster movement """
    self.correct()

    if self.down == 1:
      self.rect.y += (self.speed / 2. * delta)
      self.went += (self.speed / 2. * delta)
      if self.went >= self.rect.h:
        self.went = 0
        self.down = 0
        self.xdir = 1 if self.xdir == 0 else 0
    else:
      if self.xdir == 1:
        self.rect.x -= (self.speed * delta)
      else:
        self.rect.x += (self.speed * delta)
      if self.rect.x < 1 or self.rect.x + self.rect.w > self.size[0] - 1:
        self.down = 1

  def draw(self, batch):
    """ Draw monster rects """
    x, y, w, h = self.rect.x, self.rect.y, self.rect.w, self.rect.h
    batch.set_color(self.color)
    batch.draw_rect(x          , h/2. + y   , w/8., h/2.   )
    batch.draw_rect(7.*w/8. + x, h/2. + y   , w/8., h/2.   )
    batch.draw_rect(w/8. + x   , y          , w/8., 6.*h/8.)
    batch.draw_rect(6.*w/8. + x, y          , w/8., 6.*h/8.)
    batch.draw_rect(w/4. + x   , y          , w/2., h/4.   )
    batch.draw_rect(w/4. + x   , h/2. + y   , w/2., 3.*h/8.)
    batch.draw_rect(3.*w/8. + x, 2.*h/8. + y, w/4., h/4.   )