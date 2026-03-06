import pygame
from Apple import respawn_apple # type: ignore

pygame.init()

## Screen information
screen_width = 1000
screen_height = 800
CELL_SIZE = 20

## Color RGB coding
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GOLD = (255, 215, 0)

## Screen initializer
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

## Apple information
my_rect = (980, 780)
apple_rect = respawn_apple()

## Player information
head_pos = pygame.Vector2(100, 100)
player_seg = [pygame.Rect(head_pos.x, head_pos.y, 20, 20)]
p_direction = pygame.Vector2(CELL_SIZE, 0)
next_direction = p_direction
player_step_time = 150
segment_limit = 3

last_move = 0
delay = 50

## Screen ending/retry
pygame.font.init()
font_score = pygame.font.SysFont("Times New Roman", 24)
font_game_over = pygame.font.SysFont("Times New Roman", 72, bold=True)

score = 0
game_over = False

## Main loop
run = True
while run:
    ## Frame rate and time control
    dt = clock.tick(60) / 1000.0
    time = pygame.time.get_ticks()
    ## Window start for game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_r:
                player_seg = [pygame.Rect(head_pos.x, head_pos.y, 20, 20)]
                p_direction = pygame.Vector2(CELL_SIZE, 0)
                segment_limit = 3
                score = 0
                game_over = False
            ## Key conttrols for snake-player
            if not game_over:
                if event.key in (pygame.K_LEFT, pygame.K_a) and p_direction.x == 0:
                    p_direction = pygame.Vector2(-CELL_SIZE, 0)
                elif event.key in (pygame.K_RIGHT, pygame.K_d) and p_direction.x == 0:
                    p_direction = pygame.Vector2(CELL_SIZE, 0)
                elif event.key in (pygame.K_UP, pygame.K_w) and p_direction.y == 0:
                    p_direction = pygame.Vector2(0, -CELL_SIZE)
                elif event.key in (pygame.K_DOWN, pygame.K_s) and p_direction.y == 0:
                    p_direction = pygame.Vector2(0, CELL_SIZE)        
    screen.fill(BLACK)

    border_thickness = 20
    pygame.draw.rect(screen, GOLD, (0, 0, screen_width, screen_height), border_thickness)
    ## Beginning of the game info
    if not game_over:
        if (time - last_move) > delay:
            head_pos += p_direction

            new_head_x = player_seg[-1].x + p_direction.x
            new_head_y = player_seg[-1].y + p_direction.y
            ## Wrap control for borders
            if new_head_x < border_thickness:
                new_head_x = screen_width - border_thickness - CELL_SIZE
            elif new_head_x >= screen_width - border_thickness:
                new_head_x = border_thickness
                
            if new_head_y < border_thickness:
                new_head_y = screen_height - border_thickness - CELL_SIZE
            elif new_head_y >= screen_height - border_thickness:
                new_head_y = border_thickness
            ## Controls the body of the snake for wrapping
            new_segment = pygame.Rect(new_head_x, new_head_y, CELL_SIZE, CELL_SIZE)
            ## Game over statement
            if new_segment.collidelist(player_seg) != -1:
                game_over = True
            ## Apple respawn statement
            if player_seg[-1].colliderect(apple_rect):
                apple_rect = respawn_apple()
                pygame.draw.rect(screen, (255, 0, 0), apple_rect)
                segment_limit += 1
                score += 20

            player_seg.append(new_segment)
            ## Another snake body control to continue moving with main head
            while len(player_seg) > segment_limit:
                player_seg.pop(0)

            last_move = time
    ## Player head initializer
    for seg in player_seg:
        pygame.draw.rect(screen, GREEN, seg)
    ## Apple initializer
    pygame.draw.rect(screen, (255, 0, 0), apple_rect)
    ## Menu screen initializer
    score_surf = font_score.render(f"Score: {score}", True, WHITE)
    screen.blit(score_surf, (border_thickness + 10, border_thickness + 10))
    ## Game over screen creation
    if game_over:
        go_surf = font_game_over.render("GAME OVER", True, (255, 50, 50))
        restart_surf = font_score.render("Press 'R' to restart", True, WHITE)
        screen.blit(go_surf, ((screen_width // 2) - (go_surf.get_width() // 2), (screen_height // 2) - 50))
        screen.blit(restart_surf, ((screen_width // 2) - (restart_surf.get_width() // 2), (screen_height // 2) + 30))
    ## Update method
    pygame.display.update()
    ## Window refresh rate
    tick: (60)

## Close the window
pygame.quit()
