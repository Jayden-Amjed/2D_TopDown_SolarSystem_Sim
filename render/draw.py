import random
import pygame

class Draw:
    def __init__(self):
        pass

    def drawCircle(self, screen, color, center, radius):
        pygame.draw.circle(screen, color, center, radius)

    def make_starfield_surface(self, size, n_stars=800, color=(255,255,255)):
        
        """
        Pre-render a starfield onto a transparent Surface and return it.
        - size: (width, height)
        - n_stars: how many stars to place
        - color: star color
        """
        width, height = size
        surf = pygame.Surface((width, height), pygame.SRCALPHA)

        seen = set()
        for _ in range(n_stars):
            # unique positions help avoid "fat" stars where we overlap
            x = random.randrange(width)
            y = random.randrange(height)
            if (x, y) in seen:
                continue
            seen.add((x, y))

            # 80% 1px, 20% 2px
            size_px = 1 if random.random() < 0.8 else 2
            # slightly vary brightness for depth
            if isinstance(color, str):
                star_color = color
            else:
                b = random.randint(-30, 30)  # tiny brightness jitter
                r = max(0, min(255, color[0] + b))
                g = max(0, min(255, color[1] + b))
                c = max(0, min(255, color[2] + b))
                star_color = (r, g, c)

            pygame.draw.rect(surf, star_color, (x, y, size_px, size_px))
        return surf
            
        