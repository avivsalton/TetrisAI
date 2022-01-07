import random
import pygame

class Shape:
    def __init__(self):
        self.surf = pygame.Surface((180, 30))
        self.surf.fill((0, 0, 0))
