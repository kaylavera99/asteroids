import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)
    
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
             return
        
        
        random_angle = random.uniform(20, 50)
        asteroid_new_rad = self.radius - ASTEROID_MIN_RADIUS

        velocity_1 = self.velocity.rotate(random_angle) * 1.2
        velocity_2 = self.velocity.rotate(-random_angle) * 1.2
     

        asteroid_1 = Asteroid(self.position.x, self.position.y, asteroid_new_rad)
        asteroid_2 = Asteroid(self.position.x, self.position.y, asteroid_new_rad)
        asteroid_1.velocity = velocity_1
        asteroid_2.velocity = velocity_2
		
		
