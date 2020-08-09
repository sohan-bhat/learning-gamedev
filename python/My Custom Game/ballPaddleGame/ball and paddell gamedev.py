import pygame, random, math
from pygame import mixer

pygame.init()

# Screen
screen = pygame.display.set_mode((800, 600))
height = 800
width = 736

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

# background
background = pygame.image.load('background.jpg')

# background Music
mixer.music.load('background.wav')
mixer.music.play(-1)

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
ballYVelocity = 0
ballXVelocity = 0


# Functions

def show_score(textX, textY):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (textX, textY))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (300, 250))

def paddle(x, y):
    screen.blit(paddleImg, (paddleX, paddleY))


def ball(x, y):
    screen.blit(ballImg, (ballX, ballY))


def isCollision(ballX, ballY, paddleX, paddleY):
    distance = math.sqrt(math.pow(ballX-paddleX, 2)) + \
        (math.pow(ballY-paddleY, 2))
    if distance < 56.5:
        return True
    else:
        return False



running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                paddleX_change = 3.2

            if event.key == pygame.K_LEFT:
                paddleX_change = -3.2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddleX_change = 0

    paddleX += paddleX_change

    if paddleX <= 0:
        paddleX = 0
    elif paddleX >= 736:
        paddleX = 736
    collision = isCollision(ballX, ballY, paddleX, paddleY)
    if collision:
        ballYVelocity = -ballYVelocity
        if paddleX < ballX:
            ballXVelocity = 1
        elif paddleX > ballX:
            ballXVelocity = -1
        else: ballXVelocity = 0
        score_value += 1

    if ballX < 0 or ballX >= width:
        ballXVelocity *= -1

    if ballY > height:
        game_over_text()
        break


    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    show_score(textX, textY)
    paddle(paddleX, paddleY)
    ball(ballX, ballY)
    ballYVelocity += 0.02
    ballY += ballYVelocity
    ballX += ballXVelocity
    pygame.display.update()