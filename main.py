import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	print("Starting asteroids!")
	print("Screen width:", SCREEN_WIDTH)
	print("Screen height:", SCREEN_HEIGHT)

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	py_clock = pygame.time.Clock()
	dt = 0

	

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (updatable, drawable, asteroids)
	AsteroidField.containers = (updatable)
	Shot.containers =  (updatable, drawable, shots)
	
	asteroidField = AsteroidField()
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)




	while (True):
		screen.fill((0, 0, 0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		dt = (py_clock.tick(60) / 1000)
		
		for sprite in updatable:
			sprite.update(dt)
		for asteroid in asteroids:
			if asteroid.collision(player) == True:
				print("Game over!")
				sys.exit()

			for shot in shots:
				if asteroid.collision(shot):
					asteroid.split()
					shot.kill()
		for sprite in drawable:
			sprite.draw(screen)
		pygame.display.flip()
if __name__ == "__main__":
    main()
