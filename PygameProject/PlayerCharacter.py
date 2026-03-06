import pygame
pygame.init()

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        screen_width, screen_height = 980, 780
        if self.rect.left < 20:
            self.rect.left = 20
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 20:
            self.rect.top = 20
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height