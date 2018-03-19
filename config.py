import colors

screen_width = 800
screen_height = 600
background_image = 'img/fond.jpg'

frame_rate = 90

row_count = 9
brick_width = 75
brick_height = 20
brick_color = [colors.AQUAMARINE1, colors.DEEPSKYBLUE2, colors.DEEPPINK2]
offset_y = brick_height + 10

ball_speed = 4
ball_speed_up = 30
ball_speed_down = 1
ball_radius = 8
ball_color = colors.WHITE

paddle_width = 100
paddle_height = 20
paddle_image = 'img/paddle.png'
paddle_color = colors.WHITE
paddle_speed = 10

status_offset_y = 5

text_color = colors.WHITE
initial_lives = 3
lives_right_offset = 85
lives_offset = screen_width - lives_right_offset
score_offset = 5

font_name = 'comicsansms'
font_size = 14

effect_duration = 20

sounds_effects = dict(
    brick_hit='sound_effects/brick_hit.wav',
    effect_done='sound_effects/effect_done.wav',
    paddle_hit='sound_effects/paddle_hit.wav',
    level_complete='sound_effects/level_complete.wav',
)

message_duration = 2

button_text_color = colors.WHITE,
button_normal_back_color = colors.GRAY74
button_hover_back_color = colors.GRAY74
button_pressed_back_color = colors.GRAY74

menu_offset_x = 320
menu_offset_y = 300
menu_button_w = 75
menu_button_h = 30

uplife = 1
