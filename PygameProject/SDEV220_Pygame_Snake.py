import pygame
from Apple import respawn_apple # type: ignore
from PlayerCharacter import Player # type: ignore

pygame.init()

screen_width = 1000
screen_height = 800

BLACK = (0, 0, 0)
RED = (255, 0, 0)
FIRST_GREY = (128, 128, 128)
SECOND_GREY = (140, 140, 140)

screen = pygame.display.set_mode((screen_width, screen_height))

border_color = BLACK
border_thickness = 10
inner_color = FIRST_GREY
my_rect = (10, 10, 980, 780)

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
    pygame.draw.rect(screen, inner_color, my_rect)
    pygame.draw.rect(screen, border_color, my_rect, border_thickness)
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
    
    all_sprites.update()

    all_sprites.draw(screen)
    
    pygame.display.flip()
    pygame.display.update()

    tick: (60)

pygame.quit()