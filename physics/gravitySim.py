import pygame, math
from pygame.math import Vector2 as Vec2

class GravSim:
    def __init__(self, bodies, gravitational_constant=100.0):
        self.bodies = bodies
        self.G = gravitational_constant  # gravitational constant in "px^3 / (mass * s^2)"

    def _compute_accelerations(self):
        # reset accelerations
        for body in self.bodies:
            body._acc = Vec2(0, 0)

        # pairwise gravity
        num_bodies = len(self.bodies)
        for i in range(num_bodies):
            for j in range(i + 1, num_bodies):
                body_i = self.bodies[i]
                body_j = self.bodies[j]

                displacement = body_j.pos - body_i.pos
                distance_squared = displacement.length_squared()

                # softening to avoid singularities at very small distances
                softening_squared = 1.0
                inv_distance_cubed = 1.0 / ((distance_squared + softening_squared) ** 1.5) if distance_squared > 0 else 0.0

                gravitational_vector = self.G * displacement * inv_distance_cubed
                body_i._acc += gravitational_vector * body_j.mass
                body_j._acc -= gravitational_vector * body_i.mass

    def step(self, delta_time):
        # Leapfrog (velocity-Verlet): 
        # v(t+1/2)=v(t)+a(t)*dt/2; 
        # x(t+1)=x(t)+v(t+1/2)*dt; 
        # a(t+1); 
        # v(t+1)=v(t+1/2)+a(t+1)*dt/2
        self._compute_accelerations()
        for body in self.bodies:
            velocity_half_step = body.vel + 0.5 * body._acc * delta_time
            body.pos += velocity_half_step * delta_time
            body.vel = velocity_half_step  # temporarily stores half-step velocity

        # recompute accelerations at new positions
        self._compute_accelerations()
        for body in self.bodies:
            body.vel += 0.5 * body._acc * delta_time

            # trail
            if body.trail_len > 0:
                body._trail.append((int(body.pos.x), int(body.pos.y)))
                if len(body._trail) > body.trail_len:
                    body._trail.pop(0)
