class draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, FIRST_GREY, [ 700 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, SECOND_GREY, [600 - (column * 200), row * 100, 100, 100])
            pygame.draw.rect(screen, FIRST_GREY, [100, 800, 780, 340])
