import Py3D, sys
import pygame as pg

#CONSTS
WIDTH, HEIGHT = 800, 1200

#pygame setup
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT), 0, 32)
mainClock = pg.time.Clock()

while True:
    screen.fill((0, 0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    mainClock.tick(60)
