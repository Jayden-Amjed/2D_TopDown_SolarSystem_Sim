import pygame, math
from dataclasses import dataclass, field

Vec2 = pygame.math.Vector2
@dataclass
class Body:
    name: str
    color: tuple
    radius: int            # draw radius (px)
    mass: float            # simulation mass (arbitrary units)
    pos: Vec2              # position (px)
    vel: Vec2              # velocity (px/s)
    trail_len: int = 0     # set >0 to draw a trail

    # internal
    _acc: Vec2 = field(default_factory=lambda: Vec2(0, 0))
    _trail: list = field(default_factory=list)
    
    def __post_init__(self):
        if self._trail is None:
            self._trail = []

    def draw(self, drawer, screen):
        if self.trail_len > 0 and len(self._trail) > 1:
            # draw a faint trail
            for i in range(1, len(self._trail)):
                pygame.draw.line(screen, self.color, self._trail[i-1], self._trail[i], 1)
        drawer.drawCircle(screen, self.color, (int(self.pos.x), int(self.pos.y)), self.radius)
    