import pygame
from apple import respawn_apple # type: ignore

pygame.init()

screen_width = 1000
screen_height = 800
CELL_SIZE = 20

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GOLD = (255, 215, 0)


screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()



apple_rect = respawn_apple()

player_SPS = 300
head_pos = pygame.Vector2(100, 100)
player_seg = [pygame.Rect(head_pos.x, head_pos.y, 20, 20)]
p_direction = pygame.Vector2(player_SPS, 0)
segment_limit = 1

run = True
while run:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_a) and p_direction.x == 0:
                p_direction = pygame.Vector2(-player_SPS, 0)
            elif event.key in (pygame.K_RIGHT, pygame.K_d) and p_direction.x == 0:
                p_direction = pygame.Vector2(player_SPS, 0)
            elif event.key in (pygame.K_UP, pygame.K_w) and p_direction.y == 0:
                p_direction = pygame.Vector2(0, -player_SPS)
            elif event.key in (pygame.K_DOWN, pygame.K_s) and p_direction.y == 0:
                p_direction = pygame.Vector2(0, player_SPS)        
    screen.fill(BLACK)
    
    border_thickness = 10
    pygame.draw.rect(screen, GOLD, (0, 0, screen_width, screen_height), border_thickness)


    head_pos += p_direction * dt
    new_segment = pygame.Rect(head_pos.x, head_pos.y, 20,20)
    if new_segment != player_seg[-1]:
        player_seg.append(new_segment)

    if player_seg[-1].colliderect(apple_rect):
        apple_rect = respawn_apple()
        pygame.draw.rect(screen, (255, 0, 0), apple_rect)
        segment_limit += 10
    
    while len(player_seg) > segment_limit:
        player_seg.pop(0)

    for seg in player_seg:
        pygame.draw.rect(screen, GREEN, seg)


    if head_pos.x < 0:
        head_pos.x = screen_width - 20
    elif head_pos.x >= screen_width:
        head_pos.x = 0
        
    if head_pos.y < 0:
        head_pos.y = screen_height - 20
    elif head_pos.y >= screen_height:
        head_pos.y = 0
    


    pygame.draw.rect(screen, (255, 0, 0), apple_rect)
    pygame.display.update()

    tick: (60)

pygame.quit()
