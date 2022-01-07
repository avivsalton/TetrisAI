import pygame
import time
import threading
import shape
pygame.init()

# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Set up the drawing window + window's variables
width = 500
height = 750
screen = pygame.display.set_mode([width, height])
running = True

# Current x, y positions of shape
finished_movedown = False
curr_x = 32
curr_y = 102

# Function that gets shape down automatically every one second
def moveDown(surf_m):
    surface, curr_x, curr_y = surf_m
    global finished_movedown
    while True:
        time.sleep(1)
        if curr_y < 672:
            curr_y = curr_y + 30
        else:
            break
    changeSurfacePosition(surf_m, surface, curr_x, curr_y)

def changeSurfacePosition(surf_m, surface, curr_x, curr_y):
    surfaces.remove(surf_m)
    surfa, current_x, current_y = surf_m
    surf = (surface, curr_x, curr_y)
    surfaces.append(surf)

    finished_movedown = True
surfaces = []
surf = (shape.Shape(), curr_x, curr_y)
surfaces.append(surf)
t = threading.Thread(target=moveDown, args=[surf])
t.start()
print(surf)

while running:

    # Initializing basic stuff for the window
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(30, 100, width - 46, height - 146), 2)
    curr_shape, current_x, current_y = surf
    if finished_movedown:
        finished_movedown = False
        curr_x = 32
        curr_y = 102
        surf = (shape.Shape(), curr_x, curr_y)
        surfaces.append(surf)
        t = threading.Thread(target=moveDown, args=[surf])
        t.start()

    # For events happening in the game
    for event in pygame.event.get():
        # Closing game by click X button on window
        if event.type == pygame.QUIT:
            running = False

        if event.type == KEYDOWN:
            # Closing game by clicking ESC
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_DOWN and current_y < 672:
                current_y = 672
                changeSurfacePosition(surf, current_y, current_x)
            if event.key == K_LEFT and current_x > 32:
                current_x = current_x - 45
                changeSurfacePosition(surf, current_y, current_x)
            if event.key == K_RIGHT and current_x < 302:
                current_x = current_x + 45
                changeSurfacePosition(surf, current_y, current_x)

    # Drawing shape to screen
    for surf, curr_x, curr_y in surfaces:
        screen.blit(surf.surf, (curr_x, curr_y))
    pygame.display.flip()


# Quits game when window's getting closed
pygame.quit()