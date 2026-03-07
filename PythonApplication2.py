import os
import pygame
import time
pygame.init()

debugging = False

# Game/Window settings
WIDTH = 1000
HEIGHT = 1000
FPS = 60
GRAVITY = .05
currentScene = "default"
#player settings/stats

playerX = WIDTH/2
playerY = HEIGHT/2
playerW = 25
playerH = 25
playerVelX = 0
playerVelY = 0
PLAYERTERMVEL = 3
playerSpeed = 1
playerJumpHeight = 5
jumping = False
isGrounded = True

basePath = os.path.dirname(__file__)

egyptPath = os.path.join(basePath, "Textures&Images", "EGYPT.jpg")
scotPath = os.path.join(basePath, "Textures&Images", "Highlands.jpg")
cityPath = os.path.join(basePath, "Textures&Images", "City.jpg")

def bgResizer(x):
    x = pygame.transform.scale(x, (HEIGHT, WIDTH))
    return x

screen = pygame.display.set_mode((WIDTH, HEIGHT))

bg1 = pygame.image.load(egyptPath)
bg1 = bgResizer(bg1)
bg2 = pygame.image.load(scotPath)
bg2 = bgResizer(bg2)
bg3  = pygame.image.load(cityPath)
bg3 = bgResizer(bg3)

pygame.display.set_caption("ChronoQuest 2: Very Chrono")

sceneOrder = [bg1, bg2, bg3]
sceneNum = 0

clock = pygame.time.Clock()


screen.fill((29, 220, 224))

running = True
while running:

    keys = pygame.key.get_pressed()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #make sure ts is actually running
            running = False

    if keys[pygame.K_F5]:
        running = False

    if keys[pygame.K_e]:
        if sceneNum < len(sceneOrder)-1:
            sceneNum += 1
            time.sleep(.5)
        else:
            sceneNum = 0

    if keys[pygame.K_a]:
        playerVelX += playerSpeed
        playerX -= playerVelX

    if keys[pygame.K_d]:
        playerVelX += playerSpeed
        playerX += playerVelX
    
    if not jumping and keys[pygame.K_SPACE] and isGrounded:
        playerVelY = -playerJumpHeight
        jumping = True
        isGrounded = False
    if playerVelY >= PLAYERTERMVEL:
        playerVelY = PLAYERTERMVEL

    if playerX < 0:
        playerX = 0

    if playerX > WIDTH:
       playerX = WIDTH-playerW

    playerVelY += GRAVITY
    playerY += playerVelY

    if playerY >= HEIGHT:
       playerY = HEIGHT - playerH
       playerVelY = 0
       jumping = False
       GRAVITY = 0
       
    
    screen.blit(sceneOrder[sceneNum], (0, 0))

    pygame.draw.rect(screen, (16, 32, 16), (playerX, playerY, playerH, playerW))

    pygame.display.update()

pygame.quit()