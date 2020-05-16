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
    
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    paddle(paddleX, paddleY)
    ball(ballX, ballY)
    pygame.display.update()