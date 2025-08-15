from enum import Enum

import pygame
import pygame.surface as surface
import pygame.gfxdraw
import numpy as np

TURN_RIGHT = np.array([[ 0, 1], [-1, 0]])
TURN_LEFT  = np.array([[ 0,-1], [ 1, 0]])

UP    = np.array([[ 0], [-1]])
DOWN  = np.array([[ 0], [ 1]])
LEFT  = np.array([[-1], [0]])
RIGHT = np.array([[ 1], [0]])

#class Direction(Enum):
#    UP = (0, -1)
#    RIGHT = (1, 0)
#    DOWN = (0, 1)
#    LEFT = (-1, 0)

#def clockwise(dir):
#    if dir == Direction.UP:
#        return Direction.RIGHT
#    elif dir == Direcion.RIGHT:
#        return Direction.DOWN
#    elif dir == Direcion.DOWN:
#        return Direcion.LEFT
#    elif dir == Direction.LEFT:
#        return Direction.UP
#
# def anti_clockwise(dir):
#    if dir == Direction.UP:
#        return Direction.LEFT
#    elif dir == Direcion.RIGHT:
#        return Direction.UP
#    elif dir == Direcion.DOWN:
#        return Direcion.RIGHT
#    elif dir == Direction.LEFT:
#        return Direction.DOWN


#238
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
        self.direction = None


    def frame(self, input):
        for event in input:
            print("event:", event)
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                key_down = (event.type == pygame.KEYDOWN)
                print(key_down, event.key)
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
            self.direction = Direcion.LEFT
        if self.right_pressed:
            self.pos_x = (self.pos_x + 1) % RESOLUTION[0]
            self.direction = Direcion.RIGHT
        if self.up_pressed:
            self.pos_y = (self.pos_y - 1) % RESOLUTION[1]
            self.direction = Direction.UP
        if self.down_pressed:
            self.pos_y = (self.pos_y + 1) % RESOLUTION[1]
            self.direction = Direcion.DOWN

        if pixel_at((self.pos_x, self.pos_y)) == BLACK:


        pygame.gfxdraw.pixel(self.canvas, self.pos_x, self.pos_y, BLACK)
#        print("3", self.canvas)
        return self.canvas
        # should return a pygame surface with dimensions 64 x 64

    def color_at(column_vector):
        return self.canvas.get_at(column_vector[0, 0], column_vector[1, 0])

    def check_rectangle(self, direction):
        corners = []
        position = np.array([[pos_x], [pos_y]])
        start_position = position
        while len(corners) < 4:
            right_turn = direction + TURN_RIGHT @ direction
            if color_at(position + right_turn) == BLACK:
                position += direction
                corners.apend[position]
                diretion = TURN_RIGHT @ direction
            elif color_at(positoin + direction) == BLACK:
                position += direction
            else:
                return False
        # corners == 4, check if the position is in the origional place
        retrun position == start_position



if __name__ == "__main__":
    print("test")
    print("when you go left and turn left you than go")
    print(TURN_LEFT @ LEFT)



