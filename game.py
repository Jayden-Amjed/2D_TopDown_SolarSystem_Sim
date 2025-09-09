import math, pygame
from pygame.math import Vector2 as Vec2
from render.draw import Draw
from entities.nBody import Body
from physics.gravitySim import GravSim

class Game:
    def __init__(self, width=1280, height=720, title="2D Solar System (N-body)"):
        pygame.init()
        info = pygame.display.Info()
        self.screen = pygame.display.set_mode((info.current_w -50, info.current_h - 50))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True

        self.drawer = Draw()
        self._setup_scene()

    @property
    def center(self):
        return (self.screen.get_width()//2, self.screen.get_height()//2)

    def _setup_scene(self):
        cx, cy = self.center

        # Choose a unit system. We'll keep it simple:
        # - pixels are distance
        # - seconds are time
        # - masses are arbitrary; tune G to get nice scales
        sun = Body("Sun", (255,200,0), 150, mass=1500.0, pos=Vec2(cx, cy), vel=Vec2(0,0), trail_len=300)

        # Place Earth-like body at a distance with tangential velocity (vis-viva-ish, tuned)
        earth_r = 360
        # circular speed v = sqrt(G*M/r). We'll estimate using Sun mass only to start:
        G = 100.0
        v_earth = math.sqrt(G * sun.mass / earth_r)
        earth = Body("Earth", (80,160,255), 8, mass=1.0,
                     pos=Vec2(cx + earth_r, cy),
                     vel=Vec2(0, -v_earth*0.95),   # 0.95 -> slightly elliptical
                     trail_len=700)

        # Mars-ish
        mars_r = 480
        v_mars = math.sqrt(G * sun.mass / mars_r)
        mars = Body("Mars", (227, 83, 53), 6, mass=0.1,
                    pos=Vec2(cx + mars_r, cy),
                    vel=Vec2(0, -v_mars*0.97),
                    trail_len=700)
        
        # Mercury
        mercury_r = 200
        v_mercury = math.sqrt(G * sun.mass / mercury_r)
        mercury = Body("Mercury", (200,200,200), 3, mass=0.055,
                    pos=Vec2(cx + mercury_r, cy),
                    vel=Vec2(0, -v_mercury*0.97),
                    trail_len=700)
        
         # Venus
        venus_r = 280
        v_venus = math.sqrt(G * sun.mass / venus_r)
        venus = Body("Venus", (255,152,15), 8, mass=0.82,
                    pos=Vec2(cx + venus_r, cy),
                    vel=Vec2(0, -v_venus*0.97),
                    trail_len=700)
        #Jupiter
        jupiter_r = 570
        v_jupiter = math.sqrt(G * sun.mass / jupiter_r)
        jupiter = Body("Jupiter", (180,180,180), 16, mass=2.9,
                    pos=Vec2(cx + jupiter_r, cy),
                    vel=Vec2(0, -v_jupiter*0.97),
                    trail_len=700)
        
        saturn_r = 700
        v_saturn = math.sqrt(G * sun.mass / saturn_r)
        saturn = Body("Saturn", (255,152,15), 16, mass=2.65,
                    pos=Vec2(cx + saturn_r, cy),
                    vel=Vec2(0, -v_saturn*0.97),
                    trail_len=700)
        
        uranus_r = 840
        v_uranus = math.sqrt(G * sun.mass / uranus_r)
        uranus = Body("Uranus", (100, 149, 237), 16, mass=1.3,
                    pos=Vec2(cx + uranus_r, cy),
                    vel=Vec2(0, -v_uranus*0.97),
                    trail_len=700)
        
        neptune_r = 980
        v_neptune = math.sqrt(G * sun.mass / neptune_r)
        neptune = Body("Neptune", (0, 71, 171), 16, mass=1.3,
                    pos=Vec2(cx + neptune_r, cy),
                    vel=Vec2(0, -v_neptune*0.97),
                    trail_len=700)
        
        

        self.bodies = [sun, earth, mars,mercury,venus,jupiter,saturn,uranus,neptune]
        self.sim = GravSim(self.bodies, gravitational_constant=G)

    def handle_events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False

    def update(self, dt):
        # slow down or speed up sim time as you like:
        time_scale = 1.0
        self.sim.step(dt * time_scale)

    def render(self):
        self.screen.fill("black")
        for b in self.bodies:
            b.draw(self.drawer, self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000.0
            self.handle_events()
            self.update(dt)
            self.render()
        pygame.quit()