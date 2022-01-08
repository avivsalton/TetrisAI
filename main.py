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

# curr x, y positions of shape
finished_movedown = False
curr_x = 32
curr_y = 102

# Defining game's shapes variables
surfaces = []
s = shape.Shape()
surf = (s, curr_x, curr_y)
surfaces.append(surf)

# Function that gets shape down automatically every one second
def moveDown():
    global finished_movedown, curr_x, curr_y, surf, s
    while not finished_movedown:
        time.sleep(1)
        if curr_y < 672 and not isCurrentSurfColliding():
            curr_y = curr_y + 30
            changeSurfacePosition(s, curr_x, curr_y)
        else:
            finished_movedown = True

def changeSurfacePosition(surface, current_x, current_y):
    global surf
    surfaces.remove(surf)
    surf = (surface, current_x, current_y)
    surfaces.append(surf)

def isCurrentSurfColliding():
    for surft in surfaces:
        st, t_x, t_y = surft
        if surft is surf:
            continue
        if curr_y == t_y - 30 and (curr_x < t_x + 180 and curr_x > t_x - 180):
            return True
    return False

def getHighestYPoint():
    y_ret = 672
    for surft in surfaces:
        st, t_x, t_y = surft
        if surft is surf:
            continue
        if t_y <= y_ret and (curr_x < t_x + 180 and curr_x > t_x - 180):
            y_ret = t_y - 30
    return y_ret

t = threading.Thread(target=moveDown)
t.start()

while running:
    # Initializing basic stuff for the window
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(30, 100, width - 46, height - 146), 2)
    if finished_movedown:
        finished_movedown = False
        curr_x = 32
        curr_y = 102
        s = shape.Shape()
        surf = (s, curr_x, curr_y)
        surfaces.append(surf)
        t = threading.Thread(target=moveDown)
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
            if event.key == K_DOWN and curr_y < 672:
                curr_y = getHighestYPoint()
                changeSurfacePosition(s, curr_x, curr_y)
                t.join()
            if event.key == K_LEFT and curr_x > 32:
                curr_x = curr_x - 45
                changeSurfacePosition(s, curr_x, curr_y)
            if event.key == K_RIGHT and curr_x < 302:
                curr_x = curr_x + 45
                changeSurfacePosition(s, curr_x, curr_y)

    # Drawing shape to screen
    for surface, curr_x, curr_y in surfaces:
        screen.blit(surface.surf, (curr_x, curr_y))
    pygame.display.flip()


# Quits game when window's getting closed
pygame.quit()