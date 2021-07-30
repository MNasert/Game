import numpy as np
import random
from Game2.entities.bullet import Bullet
class Capital:
    def __init__(self, x, y, img, hp, dmg, rng, team, projectile, projectile_death, spd, firerate, unit_spd, death_img=None):
        self.is_unit = True
        self.is_projectile = False
        self.is_active = True
        self.is_alive = True
        self.spd = spd
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
        self.team = team
        self.targpos = []
        self.xmov = 0
        self.ymov = 0
        self.angle = 0
        self.timer = 0
        self.artytimer = 0
        self.movtimer = 0
        self.unit_spd = unit_spd

    def firebat(self):
        blt = []
        if self.targpos and self.rng[0] > self.dist_to_enemy:
            blt.append(Bullet(self.x + 15, self.y + 7
                              , self.projectile[0],
                              self.dmg[0], targx=self.targpos[0], targy=self.targpos[1], spd=self.spd[0],
                              team=self.team, MAXDIST=self.rng[0], death_img=self.projectile_death))
            blt.append(Bullet(self.x + 26, self.y + 7, self.projectile[0],
                              self.dmg[0], targx=self.targpos[0], targy=self.targpos[1], spd=self.spd[0],
                              team=self.team, MAXDIST=self.rng[0], death_img=self.projectile_death))
            blt.append(Bullet(self.x + 15, self.y + 13, self.projectile[0],
                              self.dmg[0], targx=self.targpos[0], targy=self.targpos[1], spd=self.spd[0],
                              team=self.team, MAXDIST=self.rng[0], death_img=self.projectile_death))
            blt.append(Bullet(self.x + 26, self.y + 13, self.projectile[0],
                              self.dmg[0], targx=self.targpos[0], targy=self.targpos[1], spd=self.spd[0],
                              team=self.team, MAXDIST=self.rng[0], death_img=self.projectile_death))

        return blt

    def fireart(self):
        return Bullet(self.x + 7, self.y + 10, self.projectile[1],
                          self.dmg[1], targx=self.targpos[0], targy=self.targpos[1], spd=self.spd[1],
                          team=self.team, MAXDIST=self.rng[1], death_img=self.projectile_death, hp=10)

    def update(self):
        if self.dist_to_enemy > self.rng[1] * .5 and self.targpos:
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
                self.angle = -(180 + (np.arctan((self.targpos[1] - self.y) / (self.targpos[0] - self.x)) * convert))
            elif self.targpos[0] - self.x > 0:
                self.angle = -np.arctan((self.targpos[1] - self.y) / (self.targpos[0] - self.x)) * convert

        else:
            self.xmov = 0
            self.ymov = 0

        if self.movtimer <= 0:
            self.x += self.xmov * self.unit_spd
            self.y += self.ymov * self.unit_spd

        ret = []
        if self.timer <= 0 and self.targpos:
            ret = self.firebat()
            self.timer = self.firerate[0] + int(10 * random.random())
        else:
            self.timer -= 1
        if self.artytimer <= 0:
            ret.append(self.fireart())
            self.artytimer = self.firerate[1] + int(10 * random.random())
        else:
            self.artytimer -= 1
        return ret

    def get_collisionbox(self):
        upper_left = (self.x, self.y)
        lower_right = (self.x + self.rect[0], self.y + self.rect[1])
        return [upper_left, lower_right]