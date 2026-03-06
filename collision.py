import pygame

PLAY_AREA = pygame.Rect(10, 10, 980, 780)

class Collision:
    @staticmethod
    def hit_wall(head_rect: pygame.Rect) -> bool:
        
        return not PLAY_AREA.contains(head_rect)

    @staticmethod
    def hit_apple(head_rect: pygame.Rect, apple_rect: pygame.Rect) -> bool:
        return head_rect.colliderect(apple_rect)

    @staticmethod
    def hit_self(head_rect: pygame.Rect, body_rects: list[pygame.Rect]) -> bool:
        
        return any(head_rect.colliderect(seg) for seg in body_rects)
