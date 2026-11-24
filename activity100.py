
import math
import random
import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED = 10
COLLISION_DISTANCE = 27

# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()

# Load Images
backgroundImg = pygame.image.load("background.png")
backgroundImg = pygame.transform.scale(
    backgroundImg, (SCREEN_WIDTH, SCREEN_HEIGHT)
)

playerImg = pygame.image.load("player.png")
enemyImg = pygame.image.load("enemy.png")
bulletImg = pygame.image.load("bullet.png")

# Player
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# Enemies
num_of_enemies = 6

enemyImg_list = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

for i in range(num_of_enemies):
    enemyImg_list.append(enemyImg)
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# Bullet
bulletX = 0
bulletY = PLAYER_START_Y
bulletY_change = BULLET_SPEED
bullet_state = "ready"

# Score, Level, Lives and Level Banner
score_value = 0
level = 1
lives = 3
banner = 0

font = pygame.font.Font(None, 32)
over_font = pygame.font.Font(None, 64)

# Game Over
game_over = False

# Functions

def show_score(x, y):
    score = font.render(
        "Score : " + str(score_value) +
        "   Level : " + str(level),
        True,
        (255, 255, 255)
    )
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg_list[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(
        (enemyX - bulletX) ** 2 +
        (enemyY - bulletY) ** 2
    )

    return distance < COLLISION_DISTANCE


# Game Loop
running = True

while running:

    screen.blit(backgroundImg, (0, 0))

    # Event Handling
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if not game_over:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    playerX_change = -5

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    playerX_change = 5

                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)

            if event.type == pygame.KEYUP:

                if event.key in [
                    pygame.K_LEFT,
                    pygame.K_RIGHT,
                    pygame.K_a,
                    pygame.K_d
                ]:
                    playerX_change = 0

    if not game_over:

        # Player Movement - A Faster Rocket
        playerX += playerX_change * (1 + level / 10)

        if playerX <= 0:
            playerX = 0

        elif playerX >= 736:
            playerX = 736

        # Enemy Movement - Lives and Faster Enemies
        for i in range(num_of_enemies):

            if enemyY[i] > 340:
                lives -= 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = ENEMY_START_Y_MIN

                if lives <= 0:
                    game_over = True
                    break

            # Enemy Movement
            enemyX[i] += enemyX_change[i] * (
                1 + (level - 1) / 5
            )

            if enemyX[i] <= 0:
                enemyX_change[i] = abs(enemyX_change[i])
                enemyY[i] += enemyY_change[i]

            elif enemyX[i] >= 736:
                enemyX_change[i] = -abs(enemyX_change[i])
                enemyY[i] += enemyY_change[i]

            # Collision Check - Level Up Every 5 Points
            collision = isCollision(
                enemyX[i], enemyY[i], bulletX, bulletY
            )

            if collision:
                bulletY = PLAYER_START_Y
                bullet_state = "ready"

                score_value += 1

                if score_value % 5 == 0:
                    level += 1
                    banner = 60

                    # Faster Bullet
                    bulletY_change = min(
                        bulletY_change + level, 20
                    )

                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(
                    ENEMY_START_Y_MIN,
                    ENEMY_START_Y_MAX
                )

            enemy(enemyX[i], enemyY[i], i)

        # Bullet Movement
        if bulletY <= 0:
            bulletY = PLAYER_START_Y
            bullet_state = "ready"

        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        # Draw Player
        player(playerX, playerY)

        # Display Score and Level
        show_score(10, 10)

        # Draw Remaining Lives
        for k in range(lives):
            screen.blit(
                pygame.transform.scale(playerImg, (32, 32)),
                (750 - k * 40, 10)
            )

        # Display Level Banner
        if banner > 0:

            level_text = over_font.render(
                "LEVEL " + str(level),
                True,
                (255, 255, 0)
            )

            screen.blit(level_text, (250, 200))
            banner -= 1

    else:

        # Game Over Screen
        game_over_text = over_font.render(
            "GAME OVER",
            True,
            (255, 255, 255)
        )

        screen.blit(game_over_text, (250, 250))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
