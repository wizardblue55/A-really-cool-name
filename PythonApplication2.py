import os
import pygame
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
isGrounded = False

basePath = os.path.dirname(__file__)

egyptPath = os.path.join(basePath, "Textures&Images", "EGYPT.jpg")

bg = pygame.image.load(egyptPath)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("ChronoQuest 2: Very Chrono")

clock = pygame.time.Clock()

def changeScene():
    global currentScene
    currentScene = "egypt"

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
        changeScene()

    if keys[pygame.K_a]:
        playerVelX += playerSpeed
        playerX -= playerVelX

    if keys[pygame.K_d]:
        playerVelX += playerSpeed
        playerX += playerVelX
    

    if not jumping and keys[pygame.K_SPACE]:
        playerVelY = playerJumpHeight
        jumping = True

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
       isGrounded = True
       

    if isGrounded:
        playerVelY = 0


    if currentScene == "default":
        screen.fill((29, 220, 224))
    else: 
        if currentScene == "egypt":
            screen.blit(bg, (0, 0))


    pygame.draw.rect(screen, (16, 32, 16), (playerX, playerY, playerH, playerW))
    pygame.display.update()

pygame.quit()