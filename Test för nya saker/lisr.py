import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 700
BALL_RADIUS = 25
BALL_COLOR = (255, 0, 0)
GRAVITY = 1
BOUNCE_FACTOR = -0.4

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("3D Physics Simulation")

# Ball properties
ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
ball_speed_x, ball_speed_y = 5, 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update ball position and velocity
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    ball_speed_y += GRAVITY

    # Bounce off the ground
    if ball_y + BALL_RADIUS > SCREEN_HEIGHT:
        ball_y = SCREEN_HEIGHT - BALL_RADIUS
        ball_speed_y *= BOUNCE_FACTOR

    # Bounce off the walls
    if ball_x + BALL_RADIUS > SCREEN_WIDTH or ball_x - BALL_RADIUS < 0:
        ball_speed_x *= -1

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the ball
    pygame.draw.circle(screen, BALL_COLOR, (int(ball_x), int(ball_y)), BALL_RADIUS)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
