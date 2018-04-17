import random
from datetime import datetime, timedelta

import os
import time
import pygame
from pygame.rect import Rect

from ball import Ball
from brick import Brick
from button import Button
from paddle import Paddle
import config as c
import colors
from game import Game
from text_object import TextObject

button = dict(
    Space_invader=('Space invader', 0),
    Pac_man=('Pac Man', 1),
    Batman=('Batman', 2),
    Cesi=('CESI', 3),
    Superman=('Superman', 4),
    Mario=('Mario', 5),
    Spider=('Spiderman', 6),
    Quitter=('Quitter', 99))

map = dict(
    dispSpace=([[0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
               [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
               [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
               [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0]]),

    dispPac=([[0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
             [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1],
             [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1],
             [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
             [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1]]),

    dispBat=([[0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
             [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
             [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1],
             [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
             [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
             [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]]),

    dispCESI=([[0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0],
              [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
              [0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0],
              [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
              [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0]]),

    dispSuperman=([[0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                   [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0],
                   [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                   [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
                   [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                   [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]),

    dispMario=([[0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
                [0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0],
                [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0]]),

    dispSpide=([[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
                [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
                [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
                [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
                [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1],
                [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]]),

    # onlyOne=([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]),
)

special_effects = dict(
        long_paddle=(colors.WHITE, 1,
                     lambda g: g.paddle.bounds.inflate_ip(c.paddle_width // 2, 0),
                     lambda g: g.paddle.bounds.inflate_ip(-c.paddle_width // 2, 0)),
        tripple_points=(colors.RED1, 1,
                        lambda g: g.set_points_per_brick(3),
                        lambda g: g.set_points_per_brick(1)
                        ),
        extra_life=(colors.GOLD1, 1,
                    lambda g: g.add_life(c.uplife),
                    lambda g: None),
        short_paddle=(colors.WHITE, 1,
                      lambda g: g.paddle.bounds.inflate_ip(c.paddle_width // -2, 0),
                      lambda g: g.paddle.bounds.inflate_ip(-c.paddle_width // -2, 0)))

assert os.path.isfile('sound_effects/brick_hit.wav')


class Breakout(Game):
    def __init__(self):
        Game.__init__(self, 'Breakout', c.screen_width, c.screen_height, c.background_image, c.frame_rate)
        self.sound_effects = {name: pygame.mixer.Sound(sound) for name, sound in c.sounds_effects.items()}
        self.reset_effect = None
        self.effect_start_time = None
        self.score = 0
        self.lives = c.initial_lives
        self.start_level = False
        self.paddle = None
        self.bricks = None
        self.brickLifes = []
        self.ball = None
        self.menu_buttons = []
        self.is_game_running = False
        self.create_objects()
        self.points_per_brick = 1

    def add_life(self, uplife):
        self.lives += uplife

    def set_points_per_brick(self, points):
        self.points_per_brick = points

    def create_menu(self):
        def on_play(button):
            for b in self.menu_buttons:
                self.objects.remove(b)

            self.is_game_running = True
            self.start_level = True
            self.menu_buttons.clear()
            self.create_bricks(button.choice)

        def on_quit(button):
            self.game_over = True
            self.is_game_running = False

        self.menu_buttons.clear()
        for i in range(0, len(button)):
            name, choice = list(button.values())[i]
            if choice == 99:
                handler = on_quit
            else:
                handler = on_play

            b = Button(c.menu_offset_x,
                       c.menu_offset_y + 40*i,
                       c.menu_button_w,
                       c.menu_button_h,
                       name,
                       choice,
                       handler,
                       padding=5)
            self.objects.append(b)
            self.menu_buttons.append(b)
            self.mouse_handlers.append(b.handle_mouse_event)

    def create_objects(self):
        self.create_paddle()
        self.create_ball()
        self.create_labels()
        self.create_menu()

    def create_labels(self):
        self.score_label = TextObject(c.score_offset,
                                      c.status_offset_y,
                                      lambda: f'SCORE: {self.score}',
                                      c.text_color,
                                      c.font_name,
                                      c.font_size)
        self.objects.append(self.score_label)
        self.lives_label = TextObject(c.lives_offset,
                                      c.status_offset_y,
                                      lambda: f'LIVES: {self.lives}',
                                      c.text_color,
                                      c.font_name,
                                      c.font_size)
        self.objects.append(self.lives_label)

    def create_ball(self):
        speed = (random.randint(-2, 2), c.ball_speed)
        #speed = (0, c.ball_speed)
        self.ball = Ball(c.screen_width // 2,
                         400,
                         c.ball_radius,
                         c.ball_color,
                         speed)
        self.objects.append(self.ball)

    def create_paddle(self):
        self.paddle = None

        paddle = Paddle((c.screen_width - c.paddle_width) // 2,
                        c.screen_height - c.paddle_height * 2,
                        c.paddle_width,
                        c.paddle_height,
                        c.paddle_color,
                        c.paddle_speed)
        self.keydown_handlers[pygame.K_LEFT].append(paddle.handle)
        self.keydown_handlers[pygame.K_RIGHT].append(paddle.handle)
        self.keyup_handlers[pygame.K_RIGHT].append(paddle.handle)
        self.keyup_handlers[pygame.K_LEFT].append(paddle.handle)
        self.paddle = paddle
        self.objects.append(self.paddle)

    def create_bricks(self, choice):
        if self.bricks is not None:
            for b in self.bricks:
                self.objects.remove(b)
            self.bricks.clear()

        w = c.brick_width
        h = c.brick_height
        brick_count = c.screen_width // (w + 1)
        offset_x = (c.screen_width - brick_count * (w + 1)) // 2
        disp = list(map.values())[choice]

        bricks = []

        for row in range(len(disp)):
            myRow = disp[row]
            for col in range(len(myRow)):

                if myRow[col] == 1:
                    brick_effect = None
                    brick_rand = random.randint(0, 2)
                    brick_color = c.brick_color[brick_rand]
                    brick_lifes = brick_rand + 1
                    index = random.randint(0, 50)
                    if index < len(special_effects):
                        print("brick power ", list(special_effects)[index])
                        brick_color, brick_lifes, start_effect_func, reset_effect_func = list(special_effects.values())[
                            index]
                        brick_effect = start_effect_func, reset_effect_func
                    brick = Brick(offset_x + col * (w + 1),
                                  c.offset_y + row * (h + 1),
                                  w,
                                  h,
                                  brick_color,
                                  brick_lifes,
                                  brick_lifes,
                                  brick_effect)
                    bricks.append(brick)
                    self.objects.append(brick)
        self.bricks = bricks

    # Gère les collisions de la balle
    def handle_ball_collisions(self):
        def intersect(obj, ball):
            edges = dict(
                left=Rect(obj.left, obj.top, 1, obj.height),
                right=Rect(obj.right, obj.top, 1, obj.height),
                top=Rect(obj.left, obj.top, obj.width, 1),
                bottom=Rect(obj.left, obj.bottom, obj.width, 1))
            collisions = set(edge for edge, rect in edges.items() if ball.bounds.colliderect(rect))
            if not collisions:
                return None

            if len(collisions) == 1:
                return list(collisions)[0]

            if 'top' in collisions:
                if ball.centery >= obj.top:
                    return 'top'
                if ball.centerx < obj.left:
                    return 'left'
                else:
                    return 'right'

            if 'bottom' in collisions:
                if ball.centery >= obj.bottom:
                    return 'bottom'
                if ball.centerx < obj.left:
                    return 'left'
                else:
                    return 'right'

        # Hits Paddle
        s = self.ball.speed
        edge = intersect(self.paddle, self.ball)
        if edge is not None:
            self.sound_effects['paddle_hit'].play()
        if edge == 'top':
            speed_x = s[0]
            speed_y = -s[1]
            if self.paddle.moving_left:
                speed_x -= 1
            elif self.paddle.moving_left:
                speed_x += 1
            self.ball.speed = speed_x, speed_y
        elif edge in ('left', 'right'):
            self.ball.speed = (-s[0], s[1])

        # Hits floor
        if self.ball.top > c.screen_height:
            self.lives -= 1
            if self.lives == 0:
                self.show_message('GAME OVER !', centralized=True)
                self.is_game_running = False
                if self.bricks is not None:
                    for b in self.bricks:
                        self.objects.remove(b)
                    self.bricks.clear()
                self.lives = 3
                self.objects.clear()
                self.create_objects()
            else:
                self.create_ball()
        # Hits ceiling
        if self.ball.top < 0:
            self.ball.speed = (s[0], -s[1])

        # Hits wall
        if self.ball.left < 0 or self.ball.right > c.screen_width:
            self.ball.speed = (-s[0], s[1])

        # Hits brick
        for index, brick in enumerate(self.bricks):
            edge = intersect(brick, self.ball)

            if not edge:
                continue
            else:
                self.sound_effects['brick_hit'].play()
                brick.decrement_brick_life()

            print("brick lifes : ", brick.type)

            if brick.type == 0:
                self.bricks.remove(brick)
                self.objects.remove(brick)
                self.score += brick.life * self.points_per_brick

                if brick.special_effect is not None:
                    if self.reset_effect is not None:
                        self.reset_effect(self)

                    # Trigger special effect
                    self.effect_start_time = datetime.now()
                    brick.special_effect[0](self)
                    # Set current reset effect function
                    self.reset_effect = brick.special_effect[1]

            if edge in ('top', 'bottom'):
                self.ball.speed = (s[0], -s[1])
            else:
                self.ball.speed = (-s[0], s[1])

    def update(self):
        if not self.is_game_running:
            return

        if self.start_level:
            self.start_level = False
            self.show_message('GET READY !', centralized=True)

        if not self.bricks:
            self.show_message('YOU WIN !', centralized=True)
            self.is_game_running = False
            # self.game_over = True
            self.objects.clear()
            self.create_objects()
            return

        if self.reset_effect:
            if datetime.now() - self.effect_start_time >= timedelta(seconds=c.effect_duration):
                self.reset_effect(self)
                self.reset_effect = None

        self.handle_ball_collisions()
        super().update()

        if self.game_over:
            self.show_message('GAME OVER !', centralized=True)

    def show_message(self,
                     text,
                     color=colors.WHITE,
                     font_name='Arial',
                     font_size=20,
                     centralized=False):
        message = TextObject(c.screen_width // 2,
                             c.screen_height // 2,
                             lambda: text, color, font_name, font_size)
        self.draw()
        message.draw(self.surface, centralized)
        pygame.display.update()
        time.sleep(c.message_duration)

    def paused(self, key):
        if not self.is_game_running:
            return

        self.show_message("PAUSE", centralized=True)
        # pygame.display.update()

        while self.pause:
            for event in pygame.event.get():
                if key == pygame.K_p and event.type == pygame.KEYDOWN:
                    self.pause = False


def main():
    Breakout().run()


if __name__ == '__main__':
    main()

