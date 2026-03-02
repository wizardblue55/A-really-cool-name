import math
from sre_constants import JUMP
import sys
import pygame
import pygame.display
#figuring out importing
pygame.init()
debugging = True

"""
print("Hello, World!")
x = 0
sevenSix = ["Oliver", "Eliot"]
#basic varibles, trying things i know from java and c#
while x<100:
    print(x)
    print(sevenSix[x % 2])
    x += 1

print(math.pi)
cunt = int(input())
chatGPT = math.sqrt(cunt)
chatGPT = int(chatGPT)
print(chatGPT)
#trying out the math class I imported earlier
"""

# Game/Window settings
WIDTH = 800
HEIGHT = 800
FPS = 60
GRAVITY = .05

#player settings/stats

playerX = WIDTH/2
playerY = HEIGHT/2
playerW = 25
playerH = 25
playerVelX = 0
playerVelY = 0
PLAYERTERMVEL = 3
playerSpeed = 5
playerJumpHeight = 5
jumping = False
isGrounded = False

screen = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.display.set_caption("Dih Destroyer 2: The Suckqul")
pygame.display.set_caption("Window")

clock = pygame.time.Clock()

running = True
while running:

    keys = pygame.key.get_pressed()


    if debugging:
        print(playerY)
        print(playerVelY)
        if(keys[pygame.K_d] or keys[pygame.K_a]):
            print("Keys are being pressed")

    clock.tick(FPS)
    print()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #make sure ts is actually running
            running == False

    
    
    if keys[pygame.K_a]:
        playerX -= playerVelX

    if keys[pygame.K_d]:
        playerX += playerVelX

    if not jumping and [pygame.K_SPACE]:
        playerVelY = playerJumpHeight
        jumping = True

    if playerVelY >= PLAYERTERMVEL:
        playerVelY = PLAYERTERMVEL

    if playerX < 0:
        playerX = 0

    if playerX > WIDTH:
       playerX = WIDTH

    playerVelY += GRAVITY
    playerY += playerVelY

    if playerY >= HEIGHT:
       playerY = HEIGHT - playerH
       playerVelY = 0
       jumping = False
       GRAVITY = 0
       isGrounded = True
    screen.fill((29, 220, 224))
    if isGrounded:
        playerVelY = 0

    pygame.draw.rect(screen, (16, 32, 16), (playerX, playerY, playerH, playerW))

    pygame.display.update()

pygame.quit()


