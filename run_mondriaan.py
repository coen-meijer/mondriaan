import pygame, sys

from code.mondriaan import Mondriaan

import random
import os

WINDOW_SIZE = (512, 512)
TITLE = "Mondriaan"

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
my_game = Mondriaan()

pygame.display.set_caption(TITLE)


def frame_loop():
    running = True
    count = 0
    while(running):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                break
        canvas = my_game.frame(events)
        pygame.transform.scale(canvas, WINDOW_SIZE, dest_surface=screen)

        pygame.display.update()
        clock.tick(30)


frame_loop()
