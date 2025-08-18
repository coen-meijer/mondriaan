import pygame
#import pygame.surface as surface
import pygame.gfxdraw
import random

#import numpy as np

# TURN_RIGHT = Matrix([ 0, -1], [1, 0])
# TURN_LEFT  = Matrix([ 0,1], [-1, 0])

UP    = (0 ,-1)   # np.array([[ 0], [-1]])
DOWN  = (0 , 1)   # np.array([[ 0], [ 1]])
LEFT  = (-1, 0)   # np.array([[-1], [0 ]])
RIGHT = ( 1, 0)   # np.array([[ 1], [0 ]])

# SCREEN_DIMENSIONS = Matrix((64, 64))   # np.array([[64],[64]])

RESOLUTION = (64, 64)

WHITE= (253, 253, 253)
BLACK = (0, 0, 0)
YELLOW = (238, 221, 0)
BLUE = (0, 51, 153)
RED = (204, 51, 0)
# MAYBE MELLOW OUT THE COLORS A BIT LATER.


class Mondriaan:

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
        self.was_on_black = False


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
            self.pos_x = (self.pos_x - 1)  # % RESOLUTION[0]
            self.direction = LEFT
            move = True
        elif self.right_pressed:
            self.pos_x = (self.pos_x + 1)  # % RESOLUTION[0]
            self.direction = RIGHT
            move = True
        elif self.up_pressed:
            self.pos_y = (self.pos_y - 1)  # % RESOLUTION[1]
            self.direction = UP
            move = True
        elif self.down_pressed:
            self.pos_y = (self.pos_y + 1)  # % RESOLUTION[1]
            self.direction = DOWN
            move = True

        if move:
            if self.on_border((self.pos_x, self.pos_y)):
                if not self.was_on_black:
                    rectangle = self.check_rectangle(turn(self.direction))
                    print("rectangle:", rectangle)
                    if rectangle is not None:
                        self.paint_rectangle(rectangle)
                    other_rectangle = self.check_rectangle(turn(turn(self.direction)))
                    print("other rectangle:", other_rectangle)
                    if other_rectangle is not None:
                        self.paint_rectangle(other_rectangle)
                    self.was_on_black = True
            else:
                self.was_on_black = False

        self.pos_x %= RESOLUTION[0]
        self.pos_y %= RESOLUTION[1]
        pygame.gfxdraw.pixel(self.canvas, self.pos_x, self.pos_y, BLACK)
        return self.canvas

    def paint_rectangle(self, rectangle):
        # first find the upper_left and the lower right corner
        upper_left = rectangle[0]
        lower_right = rectangle[0]
        for other in rectangle[1:]:
            if other[0] < upper_left[0] or other[1] < upper_left[1]:
                upper_left = other
            if other[0] > lower_right[0] or other[1] > lower_right[1]:
                lower_right = other

        color = random.choice([WHITE, WHITE, WHITE, WHITE, RED, YELLOW, BLUE])

        # we don't want to paint the line itself, so we scrink the area
        upper_left = pairwise_sum(upper_left, (1, 1))
        area = pairwise_sum(lower_right, turn(turn(upper_left)))
        if area[0] > 0 and area[1] > 0:
            rect = pygame.Rect(upper_left, area)
            pygame.gfxdraw.box(self.canvas, rect, color)

    def on_border(self, coords):
        x, y = coords
        return x < 0 or y < 0 or x >= RESOLUTION[0] or y >= RESOLUTION[1] or self.canvas.get_at(coords) == BLACK

    def check_rectangle(self, line_direction):
        corners = []
        position = (self.pos_x, self.pos_y)
        start_position = position
        right_turn = pairwise_sum(line_direction, turn(line_direction))
        while len(corners) < 4:
            turn_pixel = pairwise_sum(position, right_turn)
            straight_pixel = pairwise_sum(position, line_direction)
            if self.on_border(turn_pixel):
                position = pairwise_sum(position, line_direction)
                print("turn at:", position)
                corners.append(position)
                line_direction = turn(line_direction)
                right_turn = pairwise_sum(line_direction, turn(line_direction))
            elif self.on_border(straight_pixel):
                position = pairwise_sum(position, line_direction)
            else:
                return None
            print("walking the line, position is", position, "direction is", line_direction )
        # corners == 4, check if the position is in the origional place
        if position == start_position:
            return corners
        else:
            return None


def turn(pair):
    return pair[1], -pair[0]


def pairwise_sum(t, u):
    return t[0] + u[0], t[1] + u[1]
