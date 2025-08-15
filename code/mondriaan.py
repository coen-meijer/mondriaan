from enum import Enum

import pygame
import pygame.surface as surface
import pygame.gfxdraw
import numpy as np

TURN_RIGHT = np.array([[ 0, 1], [-1, 0]])
TURN_LEFT  = np.array([[ 0,-1], [ 1, 0]])

UP    = np.array([[ 0], [-1]])
DOWN  = np.array([[ 0], [ 1]])
LEFT  = np.array([[-1], [0 ]])
RIGHT = np.array([[ 1], [0 ]])

SCREEN_DIMENSIONS = np.array([[64],[64]])

RESOLUTION = (64, 64)

WHITE= (253, 253, 253)
BLACK = (0, 0, 0)
YELLOW = (238, 221, 0)
BLUE = (0, 51, 153)
RED = (204, 51, 0)
# MAYBE MELLOW OUT THE COLORS A BIT LATER.


class PofP:

    def __init__(self):
        self.canvas = pygame.Surface(RESOLUTION)
#        print("1", self.canvas)
        self.canvas.fill(WHITE)
        self.pos_x = 32
        self.pos_y = 32
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        self.direction = LEFT


    def frame(self, input):
        move = False
        for event in input:
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                key_down = (event.type == pygame.KEYDOWN)
                if event.key == pygame.K_LEFT:
                    self.left_pressed = key_down
                elif event.key == pygame.K_RIGHT:
                    self.right_pressed = key_down
                elif event.key == pygame.K_UP:
                    self.up_pressed = key_down
                elif event.key == pygame.K_DOWN:
                    self.down_pressed = key_down

        if self.left_pressed:
            self.pos_x = (self.pos_x - 1) % RESOLUTION[0]
            self.direction = LEFT
            move = True
        if self.right_pressed:
            self.pos_x = (self.pos_x + 1) % RESOLUTION[0]
            self.direction = RIGHT
            move = True
        if self.up_pressed:
            self.pos_y = (self.pos_y - 1) % RESOLUTION[1]
            self.direction = UP
            move = True
        if self.down_pressed:
            self.pos_y = (self.pos_y + 1) % RESOLUTION[1]
            self.direction = DOWN
            move = True

        if move and self.canvas.get_at((self.pos_x, self.pos_y)) == BLACK:
            rectangle = self.check_rectangle(TURN_RIGHT @ self.direction)
            print(rectangle)


        pygame.gfxdraw.pixel(self.canvas, self.pos_x, self.pos_y, BLACK)
#        print("3", self.canvas)
        return self.canvas
        # should return a pygame surface with dimensions 64 x 64

    def color_at(self, column_vector):
        return self.canvas.get_at((column_vector[0, 0], column_vector[1, 0]))

    def check_rectangle(self, direction):
        corners = []
        position = np.array([[self.pos_x], [self.pos_y]])
        start_position = position
        right_turn = direction + TURN_RIGHT @ direction
        while len(corners) < 4:
            if self.color_at(position + right_turn) == BLACK:
                position += direction
                corners.append(position)
                diretion = TURN_RIGHT @ direction
                right_turn = direction + TURN_RIGHT @ direction
            elif self.color_at(position + direction) == BLACK:
                position += direction
            else:
                return False
        # corners == 4, check if the position is in the origional place
        return position == start_position


if __name__ == "__main__":
    print("test")
    print("when you go left and turn left you than go")
    print(TURN_LEFT @ LEFT)



