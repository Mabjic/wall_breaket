import pygame
import config as c

from game_object import GameObject


class Brick(GameObject):
    def __init__(self, x, y, w, h, color, type, special_effect=None):
        GameObject.__init__(self, x, y, w, h)
        self.color = color
        self.special_effect = special_effect
        self.type = type

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)

    def decrement_brick_life(self):
        print("brick decremented")
        self.type -= 1
        self.color = c.brick_color[self.type]
        self.update()
