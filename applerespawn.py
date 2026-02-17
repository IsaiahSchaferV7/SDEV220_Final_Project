

def respawn_apple():
    play_area = pygame.Rect(10, 10, 980, 780)
    apple_size = 20

    x = random.randint(play_area.left,
                       play_area.right - apple_size)

    y = random.randint(play_area.top,
                       play_area.bottom - apple_size)

    return pygame.Rect(x, y, apple_size, apple_size)
