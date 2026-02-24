import pygame
from Apple import respawn_apple # type: ignore
from PlayerCharacter import Player # type: ignore

pygame.init()

screen_width = 1000
screen_height = 800
CELL_SIZE = 20

BLACK = (0, 0, 0)
RED = (255, 0, 0)
FIRST_GREY = (128, 128, 128)
SECOND_GREY = (200, 200, 200)

screen = pygame.display.set_mode((screen_width, screen_height))

class draw_board():
    screen.fill((FIRST_GREY))
    for x in range(0, screen_width - 20, CELL_SIZE):
        pygame.draw.line(screen, SECOND_GREY, (x, 0), (x, screen_height))
    for y in range(0, screen_height - 20, CELL_SIZE):
        pygame.draw.line(screen, SECOND_GREY, (0, y), (screen_width, y))
    pygame.display.update()

border_thickness = 30
my_rect = (20, 20, 980, 780)

player = Player(440, 340)
clock = pygame.time.Clock()
player_speed_per_second = 300
apple_rect = respawn_apple()
all_sprites = pygame.sprite.Group(player)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    all_sprites.draw(screen)
    pygame.draw.rect(screen, BLACK, my_rect, border_thickness)
    pygame.draw.rect(screen, (255, 0, 0), apple_rect)
    dt = clock.tick(60) / 1000.0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.rect.x -= player_speed_per_second * dt
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.rect.x += player_speed_per_second * dt
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.rect.y -= player_speed_per_second * dt
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.rect.y += player_speed_per_second * dt

    player.update()

    if player.rect.colliderect(apple_rect):
        apple_rect = respawn_apple()
        pygame.draw.rect(screen, (255, 0, 0), apple_rect)
    # Ensure apple does not spawn on player

    pygame.display.update()

    tick: (60)

pygame.quit()