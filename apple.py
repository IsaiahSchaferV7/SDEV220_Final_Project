APPLE_SIZE = 20

class Apple:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, APPLE_SIZE, APPLE_SIZE)
        self.respawn()