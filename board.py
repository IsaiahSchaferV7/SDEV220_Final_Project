class draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, FIRST_GREY, [
                             600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, FIRST_GREY, [
                             700 - (column * 200), row * 100, 100, 100])
        pygame.draw.rect(screen, FIRST_GREY, [0, 800, screen_width, 100])
        pygame.draw.rect(screen, SECOND_GREY, [0, 800, screen_width, 100], 5)
        pygame.draw.rect(screen, SECOND_GREY, [800, 0, 200, screen_height], 5)
        for i in range(9):
            pygame.draw.line(screen, SECOND_GREY, (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(screen, SECOND_GREY, (100 * i, 0), (100 * i, 800), 2)
