from pygame import *
from random import randint
winH = 700
winW = 500
window = display.set_mode((winH, winW))
#display.set_caption("Shooter")
background = transform.scale(image.load("bg.jpg"), (winH,winW))
lost = 0
count = 0
class GameSprite (sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_hp):
        sprite.Sprite.__init__(self)
        
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.hp = player_hp
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
        
class Player (GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys [K_LEFT] and self.rect.x > 5 or keys [K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys [K_RIGHT] and self.rect.x < winW-5 or keys [K_d] and self.rect.x < winW-5:
            self.rect.x += self.speed
    def fire(self):
        pass
    
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > winH:
            self.rect.x = randint(80, winW-80)
            self.rect.y = 0
            lost += 1
            
monsters = sprite.Group()
for i in range(3, 7):
    monster = Enemy("enemy.png", randint(80, winW-80), 0, randint(3, 5),randint(10, 50))
    monsters.add(monster)

hero = Player("hero.png", 200, 400, 7, 10)

game = True
finish = False
font.init()
font1 = font.Font(None, 36)
text_lose = font1.render("Пропущено: " + str(lost), 1, (255, 255, 255))
text_count = font1.render("Рахунок: " + str(count), 1, (255, 255, 255))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            
    if not finish:
        window.blit(background, (0, 0))
        window.blit(text_lose, (10,25))
        window.blit(text_count, (10,55))
        hero.reset()
        monsters.draw(window)
        
        monsters.update()
        hero.update()
        
        
        display.update()
    time.delay(50)
    
        