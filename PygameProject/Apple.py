import random
import pygame

def respawn_apple():
    screen_width = 960
    screen_height = 760
    apple_size = 20
    cols = screen_width // apple_size
    rows = screen_height // apple_size

    x = random.randint(10, cols - 1) * apple_size

    y = random.randint(10, rows - 1) * apple_size

    return pygame.Rect(x, y, apple_size, apple_size)