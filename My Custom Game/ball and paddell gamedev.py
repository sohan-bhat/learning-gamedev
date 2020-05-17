import pygame
import random

pygame.init()

# Screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('background.jpg')

# Paddle
paddleImg = pygame.image.load('paddle.png')
paddleX = 370
paddleY = 480
paddleX_change = 0

# Ball
ballImg = pygame.image.load('ball.png')
ballX = (random.randint(0, 735))
ballY = (random.randint(50, 150))
ballImg = pygame.transform.scale(ballImg, (50, 50))

# Functions

def paddle(x, y):
    screen.blit(paddleImg, (paddleX, paddleY))

def ball(x, y):
    screen.blit(ballImg, (ballX, ballY))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                paddleX_change = 1

            if event.key == pygame.K_LEFT:
                paddleX_change = -1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddleX_change = 0


    paddleX += paddleX_change

    if paddleX <=0:
        paddleX_change = 0
    elif paddleX >=736:
        paddleX = 736        

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    paddle(paddleX, paddleY)
    ball(ballX, ballY)
    pygame.display.update()

    
    