import pygame as pg
from config import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        # initiate sprites
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0


    def used_keys(self):
        # sets keys for the movement and the speed at which they will cause the player to move
        self.vx = 0
        self.vy = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx= -PLAYER_SPEED
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx= PLAYER_SPEED
        elif keys[pg.K_UP] or keys[pg.K_w]:
            self.vy= -PLAYER_SPEED
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy= PLAYER_SPEED

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def update(self):
        # updates sprites when moving (also matches them to game speed)
        self.used_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.bottomright= (self.x,self.y)

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE