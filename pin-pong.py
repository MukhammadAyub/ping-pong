from pygame import *
from random import randint
win_width = 1200
win_height = 768
w = display.set_mode((win_width, win_height))
bg = transform.scale(image.load("background.jpg"), (win_width, win_height))
lose_text = transform.scale(image.load("661.jpg"), (win_width, win_height))
win_text = transform.scale(image.load("winner.jpg"), (win_width, win_height))
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, width, height, speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        w.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        pass
    def update_r(self):
        pass


run = True
finish = False
while run:
    w.blit(bg, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            run = False

    display.update()
    clock.tick(FPS)
