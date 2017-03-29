import pygame
from color import Color
from bullet import Bullet

class Player(pygame.sprite.Sprite):

  def __init__(self, game):
    super(Player, self).__init__()
    self.speed = 300
    self.game  = game
    self.size  = game.size
    self.color = Color.WHITE()

    # bullet options
    self.spawnrate = self.game.fps / 1.5
    self.spawntick = 0

    # size dimensions
    w, h = 64, 32
    x = game.width  / 2. - (w / 2.)
    y = game.height / 10. * 9.
    self.rect = pygame.Rect(x, y, w, h)

  def center(self):
    """ Center the player to the screen """
    self.rect.x = self.game.size[0] / 2. - (self.rect.w / 2.)
    self.rect.y = self.game.size[1] / 10. * 9.

  def shoot(self):
    """ spawn a bullet """
    bullet = Bullet(0, 0)
    bullet.rect.y = self.rect.y - bullet.rect.h
    bullet.rect.x = self.rect.x + (self.rect.w / 2.) - (bullet.rect.w / 2.)
    self.game.bullets.add(bullet)

  def update(self, delta):
    """ handle keyboard events and movement """
    keys = pygame.key.get_pressed()

    # update bullets
    if keys[pygame.K_SPACE]:
      if self.spawntick == self.spawnrate:
        self.shoot()
        self.spawntick = 0
    if self.spawntick < self.spawnrate:
      self.spawntick += 1

    # update movement
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
      self.rect.x -= self.speed * delta
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
      self.rect.x += self.speed * delta
    if self.rect.x < 0: self.x = 0
    if self.rect.x + self.rect.w > self.size[0]:
      self.rect.x = self.size[0] - self.rect.w

  def draw(self, batch):
    """ Draw player to screen """
    x, y, w, h = self.rect.x, self.rect.y, self.rect.w, self.rect.h
    batch.set_color(self.color)
    batch.draw_rect(x          , h/2. + y   , w   , h/2.);
    batch.draw_rect(3.*w/8. + x, 2.*h/8. + y, w/4., h/4.);