import pygame
from color import Color

class Bullet(pygame.sprite.Sprite):

  def __init__(self, x=0, y=0):
    super(Bullet, self).__init__()
    self.speed = 400
    self.color = Color.WHITE()
    self.rect = pygame.Rect(x, y, 8, 16)

  def update(self, delta):
    """ Move bullet upwards """
    if self.rect.y < 0:
      self.kill()
    if self.alive():
      self.rect.y -= self.speed * delta

  def draw(self, batch):
    """ Draw bullet """
    batch.set_color(self.color)
    batch.draw_rect(self.rect.x, self.rect.y, self.rect.w, self.rect.h)
