from pygame import *
winH = 700
winW = 500
window = display.set_mode(winH, winW)
display.set_caption("Shooter")
background = transform.scale(image.load("360_F_386827376_uWOOhKGk6A4UVL5imUBt20Bh8cmODqzx.jpg"), (winH,winW))

class GameSprite (sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_hp):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    