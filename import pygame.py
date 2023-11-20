import pygame
import sys

# Initialize the game
pygame.init()
screen = pygame.display.set_mode((400, 600))
clock = pygame.time.Clock()

# Load game assets
background = pygame.image.load("background.png")
bird = pygame.image.load("bird.png")
pipe = pygame.image.load("pipe.png")

# Define game variables
bird_x = 50
bird_y = 300
bird_velocity = 0
gravity = 0.5
pipe_x = 400
pipe_y = 0
pipe_speed = 3
score = 0
font = pygame.font.Font(None, 36)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = -10

    # Update bird position
    bird_y += bird_velocity
    bird_velocity += gravity

    # Update pipe position
    pipe_x -= pipe_speed

    # Check for collision with pipes
    if bird_x + bird.get_width() > pipe_x and bird_x < pipe_x + pipe.get_width() and (
            bird_y < pipe_y + pipe.get_height() or bird_y + bird.get_height() > pipe_y + 200):
        pygame.quit()
        sys.exit()

    # Check for score
    if bird_x > pipe_x + pipe.get_width():
        score += 1

    # Render game objects
    screen.blit(background, (0, 0))
    screen.blit(bird, (bird_x, bird_y))
    screen.blit(pipe, (pipe_x, pipe_y))
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Check for game over
    if bird_y < 0 or bird_y + bird.get_height() > 600:
        pygame.quit()
        sys.exit()

    pygame.display.flip()
    clock.tick(60)
