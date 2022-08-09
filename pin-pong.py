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


racket1 = Player('object3.png', 5, 200, 30, 60, 10)
racket2 = Player('object4.png', 1150, 300, 30, 60, 10)
ball = GameSprite('object5.png', 100, 300, 50, 50, 10)
run = True
finish = False
while run:
    w.blit(bg, (0, 0))
    racket1.reset()
    racket2.reset()
    ball.reset()
    for e in event.get():
        if e.type == QUIT:
            run = False

    display.update()
    clock.tick(FPS)
