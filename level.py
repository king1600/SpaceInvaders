import random
from text import Text
from monster import Monster

class LevelData:
  """ Handle level data """

  def __init__(self, game):
    # spawning amount
    self.start_amount = 5
    self.next_amount  = self.start_amount
    self.amount_inc   = .3

    # spawn timer
    self.spawn_delay  = game.fps/2
    self.spawn_tick   = self.spawn_delay
    self.spawn_alive  = 0
    self.spawn_count  = 0

    # choosing fast monsters
    self.fast_amount  = 0
    self.fast_slots   = []

    # score and level counting
    self.score = 0
    self.level = 1

    # score and level display
    w, h = 96, 16
    self.score_text = Text("Score: 0", 0, 0, w, h)
    self.level_text = Text("Level: 0", game.width - w, 0, w, h)

  def spawn(self, game):
    """ Spawn monster """
    if self.spawn_tick < self.spawn_delay:
      return
    self.spawn_tick = 0

    # spawn the monster
    monster = Monster(game.size, 0, 0, 32, 32)
    self.spawn_alive = len(game.monsters.sprites())
    if self.spawn_count in self.fast_slots:
      monster.speed += monster.speed * (random.randint(38, 80)) / 100.
    game.monsters.add(monster)
    self.spawn_count += 1

  def reset(self, game):
    """ Reset the everything """
    game.bullets.empty()
    game.monsters.empty()
    game.player.center()
    self.score       = 0
    self.level       = 1
    self.next_amount = self.start_amount
    self.spawn_tick  = self.spawn_delay
    self.spawn_alive = 0
    self.spawn_count = 0

  def draw(self, batch):
    """ Draw level info to screen """
    self.score_text.set_text("Score: " + str(self.score))
    self.level_text.set_text("Level: " + str(self.level))
    self.score_text.draw(batch)
    self.level_text.draw(batch)

  def update(self, game):
    """ update the level and monster info """

    # update enemy spawn cooldown timer
    self.spawn_alive = len(game.monsters.sprites())
    if self.spawn_tick < self.spawn_delay:
      self.spawn_tick += 1

    # spawn in amount of enemies per level
    else:
      if self.spawn_count < self.next_amount:
        self.spawn(game)

      # move on to next level
      else:
        if self.spawn_alive <= 0:
          self.level += 1
          self.next_amount += int(self.next_amount * self.amount_inc)

          # choose fast monsters
          self.fast_amount = int((35. * self.next_amount) / 100.)
          slots = range(self.next_amount)
          random.shuffle(slots)
          self.fast_slots  = [slots[i] + 1 for i in range(self.fast_amount)]
          self.spawn_count = 0