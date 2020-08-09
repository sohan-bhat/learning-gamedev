import pygame, random,math

# Screen
screen = pygame.display.set_mode((1000, 1000))
white = 255, 255, 255

# Player
playerX = 0
playerY = 0
width = 100
height = 100
player = pygame.draw.rect(screen, white, [400, 300, 10, 10])

# Functions

# Running the Game
running = True
while running:
    for event in pygame.event.get():
        
        screen.blit(screen, player)

        if event.type == pygame.QUIT:
            running = False
        
pygame.draw.rect(screen, white, (400, 300, 10,10))
pygame.display.update()