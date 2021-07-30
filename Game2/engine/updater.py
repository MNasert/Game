from pygame import *
import sys
import random
def render_frame(entities, screen):
    for i in entities:
        screen.blit(transform.rotate(i.img, i.angle), (i.x, i.y))
#enumerate is slooooow
#int i is faster
#direct pointer is fastest
def update_frame(entities):
    try:
        find_collisions(entities)
        find_nearest_enemy(entities)
        for item in entities:
            if item.is_active and item.is_alive:
                ret = item.update()
                if ret is not None:
                    if type(ret) == list:
                        for obj in ret:
                            entities.append(obj)
                    else:
                        entities.append(ret)

    except IndexError:
        pass


def find_collisions(entities):
    #in mehrere listen aus teams unterteilen
    #bulletdetection
    rng = len(entities)
    for item in range(rng):
        if entities[item].hp <= 0:#löschen nach allen anderen berechnungen
            entities.pop(item)
            pass
        if entities[item].is_projectile:
            for unit in range(rng):
                if entities[unit].is_unit and entities[unit].team != entities[item].team:
                    unit_rect = entities[unit].get_collisionbox()
                    item_rect = entities[item].get_collisionbox()
                    if (unit_rect[0][0] <= (item_rect[0][0] + item_rect[1][0])/2 <= unit_rect[1][0]
                            and unit_rect[0][1] <= item_rect[1][1] <= unit_rect[1][1]):
                        entities[unit].hp -= entities[item].dmg
                        entities[item].hp -= 1
                    else:
                        pass


def find_nearest_enemy(entities):
    aimpos = []
    min_distance = sys.maxsize
    try:
        for unit_A in entities:#graphen aufbauen?
            if unit_A.is_unit and unit_A.timer <= 0:
                for unit_B in entities:
                    if unit_B.is_unit:
                        if unit_A.team is not unit_B.team:#wenn a-b = dxy -> b-a = dxy
                            dst_A_B = ((unit_A.x - unit_B.x)**2 + (unit_A.y - unit_B.y)**2)**.5
                            if dst_A_B < min_distance:
                                min_distance = dst_A_B
                                aimpos = (unit_B.x + unit_B.rect[0]/2, unit_B.y + unit_B.rect[1]/2)
                                unit_A.dist_to_enemy = min_distance
            min_distance = sys.maxsize
            unit_A.targpos = aimpos
            aimpos = []

    except UnboundLocalError:
        pass
