import os
import sys
import pygame
from player import Player
from level import LevelData
from renderer import Renderer
from pygame.locals import RESIZABLE
from pygame.locals import HWSURFACE
from pygame.locals import DOUBLEBUF
from pygame.locals import VIDEORESIZE

class Game:
  """ Space invaders main game class """

  def __init__(self):
    self.running = True
    self.width   = 640
    self.height  = 480
    self.fps     = 30

    # initialize game
    self.init()

  def init(self):
    # initialize the module
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()

    # create the window
    self.size   = (self.width, self.height)
    self.w_init = HWSURFACE | DOUBLEBUF | RESIZABLE
    self.window = pygame.display.set_mode(self.size, self.w_init)
    pygame.display.set_caption("Space Invaders")

    # create renderer
    self.batch = Renderer(self)

    # create the sprites
    self.player   = Player(self)
    self.data     = LevelData(self)
    self.bullets  = pygame.sprite.Group()
    self.monsters = pygame.sprite.Group()
    self.data.reset(self)
    
  def update(self, delta):
    """ Update game logic """
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False
      if event.type == VIDEORESIZE:
        self.width  = int(event.dict['size'][0])
        self.height = int(event.dict['size'][1])
        self.size   = (self.width, self.height)
        self.window = pygame.display.set_mode(self.size, self.w_init)

    # only update when renderer is ready
    if self.batch.ready[0]:

      # update movement
      self.monsters.update(delta)
      self.player.update(delta)
      self.bullets.update(delta)

      # collision checking
      bullets, sprites = self.bullets.sprites(), self.monsters.sprites()
      for sprite in sprites:
        if self.player.rect.colliderect(sprite.rect):
          self.data.reset(self)
          break
        for i, bullet in enumerate(bullets):
          if bullet.rect.colliderect(sprite.rect):
            bullet.kill()
            sprite.kill()
            self.data.score += 1

      # update level data
      self.data.update(self)

  def draw(self):
    """ Draw to sreen """
    self.batch.begin()

    # only draw when renderer is ready
    if self.batch.ready[0]:

      # draw text
      self.data.draw(self.batch)

      # draw sprites
      for sprite in self.monsters.sprites():
        sprite.draw(self.batch)
      for sprite in self.bullets.sprites():
        sprite.draw(self.batch)
      self.player.draw(self.batch)

    self.batch.sync(self.fps)
    self.batch.end()

  def dispose(self):
    """ Dispose any memory """
    self.bullets.empty()
    self.monsters.empty()
    del self.player
    del self.batch
    del self.data
    del self.window
    pygame.quit()
    sys.exit()

  def run(self):
    """ Basic game loop """
    while self.running:
      self.update(self.batch.delta)
      self.draw()
    self.dispose()

""" Start game """
if __name__ == '__main__':
  Game().run()