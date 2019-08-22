import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Bermude Tringle Time")

walkRight = [pygame.image.load('sprites/right_1.png'), pygame.image.load('sprites/right_2.png'), pygame.image.load('sprites/right_3.png'), pygame.image.load('sprites/right_4.png'), pygame.image.load('sprites/right_5.png'), pygame.image.load('sprites/right_6.png')]

walkLeft = [pygame.image.load('sprites/left_1.png'), pygame.image.load('sprites/left_2.png'), pygame.image.load('sprites/left_3.png'), pygame.image.load('sprites/left_4.png'), pygame.image.load('sprites/left_5.png'), pygame.image.load('sprites/left_6.png')]

playerStand = pygame.image.load('sprites/stop.png')
bgi = pygame.image.load('sprites/bg.jpg')

clock = pygame.time.Clock()

x = 50
y = 425

left = False
right = False
animCount = 0

lastMove = 'right'

class snaryad():
    def _init_(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
        
def draw(self, win):
    pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

def drawWindow():
    global animCount
    
    win.blit(bgi, (0, 0))
    
    if animCount + 1 >= 30:
        animCount = 0
        
    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))
    
    for bullet in bullets:
        bullet.draw(win)
    
    pygame.display.update()

width = 60
height = 71
speed = 5

run = True
bullets = []
while run:
    
    clock.tick(30)
    
    for work in pygame.event.get():
        if work.type == pygame.QUIT:
            run = False
    
    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
            
    
    
    keys = pygame.key.get_pressed()
    
    if keys [pygame.K_f]:
        if lastMove == 'right':
            facing = 1
        else:
            facing = -1
        if len(bullets) < 5:
            bullets.append(snaryad(round(x + width // 2), round(y + height // 2), 3, (189, 183, 107), facing))
    
    if keys [pygame.K_a] and x > 5:
        x -= speed
        left = True
        right = False
        lastMove = 'left'
    elif keys [pygame.K_d] and x < 500 - width - 5:
        x += speed
        left = False
        right = True
        lastMove = 'right'
    else:
        left = False
        right = False
        animCount = 0
    if keys [pygame.K_w] and y > 5:
        y -= speed
    if keys [pygame.K_s] and y < 500 - height - 5:
        y += speed
        
    drawWindow()

pygame.quit()