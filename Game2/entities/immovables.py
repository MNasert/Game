
import random
from Game2.entities.bullet import Bullet
class Starbase:
    def __init__(self, x, y, img, hp, dmg, rng, team, projectile, projectile_death, spd, firerate, death_img=None):
        self.is_unit = True
        self.is_projectile = False
        self.is_active = True
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
        self.timer = 0

    def fire(self):
        if self.targpos and self.rng > self.dist_to_enemy:
            blt = []
            blt.append(Bullet(self.x, self.y + self.rect[1]/2, self.projectile,
                         self.dmg, targx=self.targpos[0], targy=self.targpos[1], spd=self.spd,
                         team=self.team, MAXDIST=self.rng, death_img=self.projectile_death))
            blt.append(Bullet(self.x + self.rect[0] / 2, self.y, self.projectile,
                         self.dmg, targx=self.targpos[0], targy=self.targpos[1], spd=self.spd,
                         team=self.team, MAXDIST=self.rng, death_img=self.projectile_death))
            blt.append(Bullet(self.x + self.rect[0], self.y + self.rect[1] / 2, self.projectile,
                         self.dmg, targx=self.targpos[0], targy=self.targpos[1], spd=self.spd,
                         team=self.team, MAXDIST=self.rng, death_img=self.projectile_death))
            blt.append(Bullet(self.x + self.rect[0]/2, self.y + self.rect[1], self.projectile,
                         self.dmg, targx=self.targpos[0], targy=self.targpos[1], spd=self.spd,
                         team=self.team, MAXDIST=self.rng, death_img=self.projectile_death))
            return blt
        else:
            return None

    def update(self):
        if self.timer <= 0:
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
