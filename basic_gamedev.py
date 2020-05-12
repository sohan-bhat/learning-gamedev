import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))

background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (800, 600))

pygame.display.set_caption('Space invaders')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player

playerImg = pygame.image.load('gaming.png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.8)
    enemyY_change.append(40)

# bullet

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480   
bulletX_change = 0
bulletY_change = 5
bullet_state = 'ready'

score = 0

def player(x, y):
    screen.blit(playerImg, (playerX, playerY))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (enemyX[i], enemyY[i]))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 5))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2))+ (math.pow(enemyY-bulletY,2))
    if distance < 27:
        return True
    else: return False
 
running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1

            if event.key == pygame.K_RIGHT:
                playerX_change = 1

            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for i in range(num_of_enemies): 
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.8
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.8
            enemyY[i] += enemyY_change[i]
            
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = 'ready'
            score += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)    
 
    if bulletY <= 0:
        bulletY =480
        bullet_state = 'ready'

    if bullet_state == 'fire':
        fire_bullet (bulletX, bulletY)
        bulletY -= bulletY_change



    player(playerX, playerY)
    pygame.display.update()
