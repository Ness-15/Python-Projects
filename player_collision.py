import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 640
screen_height = 480

FPS = 60

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("My Game")

# Set the font for displaying text
font = pygame.font.Font(None, 36)

# Set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set the starting position of the player
player_x = 300
player_y = 400

# Set the size of the player
player_width = 40
player_height = 40

# Set the speed of the player
player_speed = 5

# Set the starting position of the enemy
enemy_x = random.randint(0, screen_width - player_width)
enemy_y = 0

# Set the size of the enemy
enemy_width = 40
enemy_height = 40

# Set the speed of the enemy
enemy_speed = 5

# Set the score
score = 0

# Set the game over flag
run = True
clock = pygame.time.Clock()
# Main game loop
while run:
    clock.tick(FPS)
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Move the enemy
    enemy_y += enemy_speed

    # Check for collision
    if player_x < enemy_x + enemy_width and player_x + player_width > enemy_x and player_y < enemy_y + enemy_height and player_y + player_height > enemy_y:
        score += 1
        enemy_x = random.randint(0, screen_width - player_width)
        enemy_y = 0

    # Check if enemy reached the bottom
    if enemy_y > screen_height:
        game_over = True

    # Fill the background color
    screen.fill(WHITE)

    # Draw the player
    pygame.draw.rect(screen, BLACK, (player_x, player_y, player_width, player_height))

    # Draw the enemy
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_width, enemy_height))

    # Draw the score
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
