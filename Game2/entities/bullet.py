from pygame import *
import random
class Bullet:
    def __init__(self, x, y, img, dmg, targx, targy, spd, team, MAXDIST, death_img):
        self.is_unit = False
        self.is_projectile = True
        self.is_active = True
        self.MAXDIST = MAXDIST
        self.start_x = x
        self.hp = 1
        self.x = x
        self.team = team
        self.start_y = y
        self.y = y
        self.img = img
        self.rect = [self.img.get_width(), self.img.get_height()]
        self.dmg = dmg
        self.death_img = death_img
        spd_y = targy - self.start_y
        spd_x = targx - self.start_x

        if abs(spd_x) > abs(spd_y):
            spd_y = spd_y/abs(spd_x)
            spd_x = 1 if spd_x > 0 else -1

        if abs(spd_x) < abs(spd_y):
            spd_x = spd_x/abs(spd_y)
            spd_y = 1 if spd_y > 0 else -1

        if abs(spd_x) == abs(spd_y):
            spd_y = 1 if spd_y > 0 else -1
            spd_x = 1 if spd_x > 0 else -1

        self.spd_x = spd_x * spd + .25*(.5-random.random())
        self.spd_y = spd_y * spd + .25*(.5-random.random())

    def update(self):
        self.x += self.spd_x
        self.y += self.spd_y
        self.MAXDIST -= abs(self.spd_y) + abs(self.spd_x)
        if self.MAXDIST <= 0:
            self.hp = -1


    def get_collisionbox(self):
        upper_left = (self.x, self.y)
        lower_right = (self.x + self.rect[0], self.y + self.rect[1])
        return [upper_left, lower_right]
