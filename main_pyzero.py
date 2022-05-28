import pgzrun
from pgzero.builtins import Actor, mouse, Rect
from pgzero.screen import Screen
import random
import sys
import time
screen: Screen

WIDTH = 800
HEIGHT = 600

cloud = Actor('chmurka_01')
BLACK = 0, 0, 0
RED = 255, 0, 0
WHITE = 255, 255, 255

rects = [[Rect(random.randint(0, WIDTH), 0, 20, 20), True] for _ in range(10)]
left = 10
LOST = False

start = 0
def close_game_after_3_seconds(now):
    global start
    if not start:
        start = now
    elif abs(start - now) > 3:
        sys.exit(0)

def on_mouse_down(pos, button):
    global left
    if button != mouse.LEFT:
        return
    for rect in rects:
        if rect[0].x <= pos[0] <= rect[0].x + 20 and \
            rect[0].y <= pos[1] <= rect[0].y + 20 and rect[1]:
            rect[1] = False
            left -= 1
            break

def update():
    global LOST
    cloud.x += 1
    for rect in rects:
        if not rect[1]:
            continue
        rect[0].x += random.randint(-1, 1)
        rect[0].y += 1
        if rect[0].x <= -20:
            rect[0].x += 1
        if rect[0].x >= WIDTH:
            rect[0].x -= 1
        if rect[0].y >= HEIGHT:
            LOST = True

def draw():
    screen.fill(BLACK)
    for rect in rects:
        if rect[1]:
            screen.draw.filled_rect(rect[0], RED)
    if left == 0:
        screen.draw.text('Wygrałeś', (0, 0), color=WHITE, fontsize=50, sysfontname='Tahoma')
    if LOST:
        screen.draw.text('Przegrałeś', (0, 0), color=WHITE, fontsize=50, sysfontname='Tahoma')
    if left == 0 or LOST:
        close_game_after_3_seconds(time.time())
    cloud.draw()

pgzrun.go()