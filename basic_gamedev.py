import pygame


pygame.init()

screen = pygame.display.set_mode((800, 600))


pygame.display.set_caption('Space invaders')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)


playerImg = pygame.image.load('gaming.png')
playerX = int(370)
playerY = int(480)
playerX_change = 0


enemyImg = pygame.image.load('space-ship.png')
enemyX = 370
enemyY = 50
enemyX_change = 0

def player(x, y):
    screen.blit(playerImg, (playerX, playerY))

def enemy(x, y):
    screen.blit(enemyImg, (enemyX, enemyY))


running = True
while running:

    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
