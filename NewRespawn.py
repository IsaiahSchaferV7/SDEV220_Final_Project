if player.rect.colliderect(apple_rect):
    new_apple = respawn_apple()
    
    # Ensure apple does not spawn on player
    while player.rect.colliderect(new_apple):
        new_apple = respawn_apple()
    
    apple_rect = new_apple