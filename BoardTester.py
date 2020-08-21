"""
Jake Martin
Python code to test board graphics using pygame
Created 2020
"""

# Import libraries
import pygame
import random

# Function to create a randomized color tuple
def rand_color()->(int,int,int):
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))


# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the height and width of the screen to accomodate 25x20 lightboard circles
size = ((30+5)*25+5, (30+5)*20+5)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Board Tester")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# The array to hold the board pixel values
colors = [[rand_color() for x in range(25)] for y in range(20)]


# Loop as long as done == False
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Clear the screen and set the screen background
    screen.fill(BLACK)
#===============================================================================
    # Code for looping

    # Iterates over each of the board pixels to display it
    for y in range(20):
        for x in range(25):
            pygame.draw.ellipse(screen, colors[y][x], [(30+5)*x+5,(30+5)*y+5,30,30])

    colors = [[rand_color() for x in range(25)] for y in range(20)]

#===============================================================================
    # Put updated pixels on the screen
    pygame.display.flip()

    # Limit loop to 60 fps
    clock.tick(60)


# Be IDLE friendly
pygame.quit()
