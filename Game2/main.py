import pygame.time
from pygame import init
import ctypes
import threading
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
import sys
import time
from Game2.entities.unit import Unit
from Game2.entities.immovables import Starbase
from Game2.entities.Capitals import Capital
from Game2.engine.updater import update_frame, render_frame
screensize = (screensize[0], screensize[1])
unt = ["gunner ", "arty ", "fighter ", "starbase ", "battleship "]
unitimage_1 = pygame.image.load("images/Unit.bmp")
unitimage_1.set_colorkey((255, 0, 255))
artyimage_1 = pygame.image.load("images/Arty1.bmp")
artyimage_1.set_colorkey((255, 0, 255))
bulletimage_1 = pygame.image.load("images/bullet.bmp")
bulletimage_1.set_colorkey((255, 0, 255))
unitimage_2 = pygame.image.load("images/Unit2.bmp")
unitimage_2.set_colorkey((255, 0, 255))
artyimage_2 = pygame.image.load("images/Arty2.bmp")
artyimage_2.set_colorkey((255, 0, 255))
bulletimage_2 = pygame.image.load("images/bullet2.bmp")
bulletimage_2.set_colorkey((255, 0, 255))
artyproj = pygame.image.load("images/artyproj.bmp")
artyproj.set_colorkey((255, 0, 255))
artyplosion = pygame.image.load("images/artyplosion.bmp")
artyplosion.set_colorkey((255, 0, 255))
bulletdeath = pygame.image.load("images/bulletplosion.bmp")
bulletdeath.set_colorkey((255, 0, 255))
fighterimg_1 = pygame.image.load("images/Fighter1.bmp")
fighterimg_1.set_colorkey((255, 0, 255))
fighterimg_2 = pygame.image.load("images/Fighter2.bmp")
fighterimg_2.set_colorkey((255, 0, 255))
fighterbb1 = pygame.image.load("images/fighterbb1.bmp")
fighterbb2 = pygame.image.load("images/fighterbb2.bmp")
starbase1 = pygame.image.load("images/starbase1.bmp")
starbase1.set_colorkey((255, 0, 255))
starbase2 = pygame.image.load("images/starbase2.bmp")
starbase2.set_colorkey((255, 0, 255))
bs1 = pygame.image.load("images/battleship1.bmp")
bs1.set_colorkey((255, 0, 255))
bs2 = pygame.image.load("images/battleship2.bmp")
bs2.set_colorkey((255, 0, 255))
bsproj1 = pygame.image.load("images/bsprojectile1.bmp")
bsproj1.set_colorkey((255, 0, 255))
bsproj2 = pygame.image.load("images/bsprojectile2.bmp")
bsproj2.set_colorkey((255, 0, 255))
# define a main function



def main():
    entitylist = []
    team_A = []
    team_B = []
    chosen_unit = []
    timer = 0
    button_up = 0
    chosen_unit = 0
    # initialize the pygame module
    init()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
    # create a surface on screen that has the size of 640 x 480
    screen = pygame.display.set_mode(screensize)
    background = pygame.image.load("images/bg.bmp")
    # screen.blit(img, (x,y)) draw -> mit pygame.display.flip() dann neu rendern


    # define a variable to control the main loop
    running = True
    pause = False
    # main loop
    cntr = 0
    simspeed = 60
    fps = []
    txt_surface = font.render("--- fps", True, (0, 0, 0))
    txt_surface_2 = font.render("--- entities", True, (0, 0, 0))
    txt_surface_3 = font.render(str(unt[chosen_unit]) + "selected", True, (0, 0, 255))
    txt_surface_4 = font.render("Keyup = change unit; p=pause time; esc to exit; lmb-green team, rmb-orange", True, (0, 0, 255))
    txt_surface_5 = font.render("paused" if pause else "running", True, (0, 0, 255))
    txt_surface_6 = font.render("simspeed = 60", True, (0, 0, 255))
    while running:
        start_time = time.time()
        clock.tick(simspeed)
        if not pause:
            update_frame(entitylist)
        screen.blit(background, (0, 0))
        render_frame(entitylist, screen)

        for event in pygame.event.get():
            state = pygame.mouse.get_pressed()
            if event.__dict__.__contains__("key"):
                if event.__dict__["key"] == pygame.K_ESCAPE and event.type == 768:
                    sys.exit("Quit game")
                if event.__dict__["key"] == pygame.K_p and event.type == 768:
                    pause = True if not pause else False
                if event.__dict__["key"] == pygame.K_PLUS and event.type == 768:
                    simspeed *= 2
                if event.__dict__["key"] == pygame.K_MINUS and event.type == 768:
                    simspeed /= 2

                if event.__dict__["key"] == pygame.K_UP and event.type == 768:
                    if chosen_unit != 4:
                        chosen_unit += 1
                    elif chosen_unit == 4:
                        chosen_unit = 0

            if state[0] != 0:
                if chosen_unit == 0:
                    entitylist.append(Unit(*pygame.mouse.get_pos(), unitimage_1, hp=100,
                                           dmg=5, rng=450, team=0, projectile=bulletimage_1,
                                           projectile_death=bulletdeath, spd=1, firerate=60*(.2), unit_spd=4))
                if chosen_unit == 1:
                    entitylist.append(Unit(*pygame.mouse.get_pos(), artyimage_1, hp=20,
                                           dmg=50, rng=1200, team=0, projectile=artyproj,
                                           projectile_death=artyplosion,  spd=3, firerate=60*(3), unit_spd=3))
                if chosen_unit == 2:
                    entitylist.append(Unit(*pygame.mouse.get_pos(), fighterimg_1, hp=5,
                                           dmg=1, rng=100, team=0, projectile=fighterbb1,
                                           projectile_death=None,  spd=2, firerate=60*(.125), unit_spd=8))
                if chosen_unit == 3:
                    entitylist.append(Starbase(*pygame.mouse.get_pos(), starbase1, hp=5000,
                                           dmg=5, rng=800, team=0, projectile=bulletimage_1,
                                           projectile_death=None,  spd=3, firerate=60*(.25)))
                if chosen_unit == 4:
                    entitylist.append(Capital(*pygame.mouse.get_pos(), bs1, hp=1000,
                                           dmg=[5, 30], rng=[450, 1400], team=0, projectile=[bulletimage_1, bsproj1],
                                           projectile_death=None, spd=[2, 3], firerate=[60 * (.25), 60*(5)], unit_spd=3))

            if state[2] != 0:
                if chosen_unit == 0:
                    entitylist.append(Unit(*pygame.mouse.get_pos(), unitimage_2, hp=100,
                                           dmg=5, rng=450, team=1, projectile=bulletimage_2,
                                           projectile_death=bulletdeath,  spd=1, firerate=60*(.2), unit_spd=4))
                if chosen_unit == 1:
                    entitylist.append(Unit(*pygame.mouse.get_pos(), artyimage_2, hp=20,
                                           dmg=50, rng=1200, team=1, projectile=artyproj,
                                           projectile_death=artyplosion,  spd=4, firerate=60*(3), unit_spd=3))
                if chosen_unit == 2:
                    entitylist.append(Unit(*pygame.mouse.get_pos(), fighterimg_2, hp=5,
                                           dmg=1, rng=100, team=1, projectile=fighterbb2,
                                           projectile_death=None, spd=2, firerate=60 * (.125), unit_spd=8))
                if chosen_unit == 3:
                    entitylist.append(Starbase(*pygame.mouse.get_pos(), starbase2, hp=5000,
                                               dmg=5, rng=800, team=1, projectile=bulletimage_2,
                                               projectile_death=None, spd=3, firerate=60 * (.25)))
                if chosen_unit == 4:
                    entitylist.append(Capital(*pygame.mouse.get_pos(), bs2, hp=1500,
                                           dmg=[5, 30], rng=[450, 1400], team=1, projectile=[bulletimage_2, bsproj2],
                                           projectile_death=None, spd=[2, 3], firerate=[60 * (.25), 60*(5)], unit_spd=3))

        end_time = time.time()
        cntr += 1
        fps.append(end_time-start_time)
        if cntr % 60 == 0:
            fps = sum(fps)/len(fps)
            txt_surface = font.render(str(round(1/fps)) + "ups", True, (0, 0, 255))
            txt_surface_2 = font.render(str(round(len(entitylist))) + "entities", True, (0, 0, 255))
            txt_surface_3 = font.render(str(unt[chosen_unit]) + "selected", True, (0, 0, 255))
            txt_surface_5 = font.render("paused" if pause else "running", True, (0, 0, 255) if not pause else (255, 0, 0))
            txt_surface_6 = font.render("simspeed = " + str(simspeed), True, (0, 0, 255) if not pause else (255, 0, 0))
            cntr = 0
            fps = []
        screen.blit(txt_surface, (1855, 10))
        screen.blit(txt_surface_2, (1800, 50))
        screen.blit(txt_surface_3, (1740, 90))
        screen.blit(txt_surface_4, (10, 10))
        screen.blit(txt_surface_5, (1840, 140))
        screen.blit(txt_surface_6, (1680, 10))
        pygame.display.update()
game=threading.Thread(target=main, daemon=True)
game.start()
game.join()
