# ---------- Self-collision: head hits any body segment ----------
head_rect = player_seg[-1]
if head_rect.collidelist(player_seg[:-1]) != -1:
    state = GAME_OVER