import pygame
import sys

# Initialize Pygame
pygame.init()

# set up the display
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drawing Shapes with Pygame")

#Defin Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

#Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Main Loop
running = True
while running:
    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Fill the screen with white
    win.fill(WHITE)

    #Draw shapes
    #Circle: (x, y, radius)
    pygame.draw.circle(win, RED, (100, 100), 50)

    #Rectangle: (x, y, width, height)
    pygame.draw.rect(win, BLUE, (200, 50, 150, 100))

    #Ellipse: (x, y, width, height)
    pygame.draw.ellipse(win, GREEN, (400, 50, 150, 100))

    #Line: (start_pos, end_pos, width)
    pygame.draw.line(win, BLACK, (50, 300), (550, 300), 5)

    #Draw a polygon (e.g. a pentagon)
    polygon_points = [(300, 50), (350, 150), (450,150), (475, 250), (325, 250)]
    pygame.draw.polygon(win, RED, polygon_points)

    #Update the display
    pygame.display.flip()

    #Control the frame rate(60 frames per second)
    clock.tick(60)

#Quit Pygame
pygame.quit()
sys.exit()