import pygame as pg
import sys

pg.init()

size = width, height = 800, 600
speed = [2, 2]
black = 0, 0, 0

screen = pg.display.set_mode(size)
pg.draw.rect(screen, (0, 0, 205), (395, 0, 10, 10))

while True:
    pg.draw.rect(screen, (0, 0, 205), (395, 0, 10, 10))
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()


