import pygame
import random
import math
from pygame import mixer
#initialize
pygame.init()
mixer.init()
#create the game screen
screen = pygame.display.set_mode((800,600))

#background
background = pygame.image.load('theo.png')

#background sound
mixer.music.load('sound.mp3')
mixer.music.play(-1)

#player

playerImg = pygame.image.load('sword.png')
playerX = 370
playerY = 480
playerY_change = 0
playerX_change = 0
#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
textY = 10
#enemy
enemyImg = []
enemyX = []
enemyY = []
enemyY_change = []
enemyX_change = []
num_of_enemies = 6


for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('shield.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50, 200))
    enemyY_change.append(40)
    enemyX_change.append(4)

#bullet

#Ready - You can't see the bullet fo rit is stored.
#Fire - Bullet is moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 10
bulletX_change = 0
bullet_state = "ready"



#Game over text
over_font = pygame.font.Font('freesansbold.ttf',64)

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_text,(200, 250))

def show_score(x,y):
    score = font.render("Score:" + str(score_value), True, (255, 255, 255))
    screen.blit(score,(x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16, y+10))

def player(x, y):
    screen.blit(playerImg,(x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i],(x, y))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX,2)) + (math.pow(enemyY - bulletY, 2))
    if distance < 54:
        return True
    else:
        return False

#title and icon
pygame.display.set_caption("Xospaquest - A Xospalipso Adventure!")
icon = pygame.image.load("test.png")
pygame.display.set_icon(icon)
#game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background,(0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -5
        if event.key == pygame.K_RIGHT:
            playerX_change = 5
        if event.key == pygame.K_SPACE:
            if bullet_state is "ready":
                bullet_Sound = mixer.Sound('papapa.ogg')
                bullet_Sound.play()
                bulletX = playerX
                fire_bullet(playerX, bulletY)
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0
    playerY += playerY_change
    playerX += playerX_change
    enemyX += enemyX_change

    #Boundary Check

    if playerX <= 0 :
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    #Enemy Movement and Boundaries
    for i in range(num_of_enemies):
        #game over
        if enemyY[1] > 300:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
            
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 :
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]
     #Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound('fast.ogg')
            explosion_Sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0,800)
            enemyY[i] = random.randint(50, 200)

        enemy(enemyX[i],enemyY[i], i)
    #Bullet movement
    if bulletY <=0 :
        bulletY = 480
        bullet_state = "ready"
         
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change




    player(playerX,playerY)
    show_score(textX, textY)
    pygame.display.update()