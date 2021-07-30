from pygame import *
import numpy as np
import random
from Game2.entities.bullet import Bullet
class Unit:
    def __init__(self, x, y, img, hp, dmg, rng, team, projectile, projectile_death, spd, firerate, death_img=None, unit_spd=1):
        self.is_unit = True
        self.is_projectile = False
        self.is_active = True
        self.is_alive = True
        self.spd = spd
        self.unit_spd = unit_spd
        self.firerate = firerate
        self.projectile = projectile
        self.projectile_death = projectile_death
        self.death_img = img
        self.x = x
        self.y = y
        self.dist_to_enemy = 0
        self.img = img
        self.rect = [self.img.get_width(), self.img.get_height()]
        self.hp = hp
        self.dmg = dmg
        self.rng = rng
        self.xmov = 0
        self.ymov = 0
        self.team = team
        self.angle = 0
        self.targpos = []
        self.timer = 0
        self.movtimer = 0

    def fire(self):
        if self.targpos and self.rng > self.dist_to_enemy:
            blt = Bullet(self.x + self.rect[0]/2, self.y + self.rect[1]/2, self.projectile,
                         self.dmg, targx=self.targpos[0], targy=self.targpos[1], spd=self.spd,
                         team=self.team, MAXDIST=self.rng, death_img=self.projectile_death)
            return blt
        else:
            return None

    def update(self):
        if self.dist_to_enemy > self.rng*.25 and self.targpos:
            self.xmov = self.targpos[0] - self.x
            self.ymov = self.targpos[1] - self.y
            convert = 180 / np.pi

            if abs(self.xmov) > abs(self.ymov):
                self.ymov = self.ymov / abs(self.xmov)
                self.xmov = 1 if self.xmov > 0 else -1

            if abs(self.xmov) < abs(self.ymov):
                self.xmov = self.xmov / abs(self.ymov)
                self.ymov = 1 if self.ymov > 0 else -1

            if abs(self.xmov) == abs(self.ymov):
                self.xmov = 1 if self.xmov > 0 else -1
                self.ymov = 1 if self.ymov > 0 else -1

            if self.targpos[0] - self.x < 0:
                self.angle = -(180 + (np.arctan((self.targpos[1] - self.y)/(self.targpos[0] - self.x)) * convert))
            else:
                self.angle = -np.arctan((self.targpos[1] - self.y)/(self.targpos[0] - self.x)) * convert

        else:
            self.xmov = 0
            self.ymov = 0

        if self.movtimer <= 0:
            self.x += self.xmov*self.unit_spd
            self.y += self.ymov*self.unit_spd

        if self.timer <= 0 and self.targpos:
            ret = self.fire()
            self.timer = self.firerate + int(10 * random.random())
            return ret
        else:
            self.timer -= 1
            return None



    def get_collisionbox(self):
        upper_left = (self.x, self.y)
        lower_right = (self.x + self.rect[0], self.y + self.rect[1])
        return [upper_left, lower_right]
