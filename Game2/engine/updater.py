from pygame import *
import threading
import sys
import random
def only_render(entities, screen):
    for i in entities:
        screen.blit(i.img, (i.x, i.y))

def render_frame(entities, screen):
    try:
        #thread1 = threading.Thread(target=find_collisions, args=[entities], daemon=True)
        #thread2 = threading.Thread(target=find_nearest_enemy, args=[entities], daemon=True)
        find_collisions(entities)
        find_nearest_enemy(entities)
        for i, item in enumerate(entities):
            if item.is_active:
                ret = item.update()
                if ret is not None:
                    if type(ret) == list:
                        for obj in ret:
                            entities.append(obj)
                    else:
                        entities.append(ret)
            screen.blit(item.img, (item.x, item.y))
    except IndexError:
        pass



def find_collisions(entities):
    for i, item in enumerate(entities):
        if item.hp <= 0:
            entities.pop(i)
            pass
        if item.is_projectile:
            for j, unit in enumerate(entities):
                if unit.is_unit and unit.team != item.team:
                    unit_rect = unit.get_collisionbox()
                    item_rect = item.get_collisionbox()
                    if item.team != unit.team:
                        if (unit_rect[0][0] <= (item_rect[0][0] + item_rect[1][0])/2 <= unit_rect[1][0]
                                and unit_rect[0][1] <= item_rect[1][1] <= unit_rect[1][1]):
                            entities[j].hp -= item.dmg
                            entities[i].hp -= 1
                    else:
                        pass


def find_nearest_enemy(entities):
    aimpos = []
    min_distance = sys.maxsize
    try:
        for unit_A in entities:
            if unit_A.is_unit and unit_A.timer <= 0:
                for unit_B in entities:
                    if unit_B.is_unit:
                        if unit_A.team is not unit_B.team:
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
