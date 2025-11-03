import pygame
import sys
from constants import *
from player import *
from circleshape import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    #player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    #asteroids = pygame.sprite.Group()
    #shots = pygame.sprite.Group()
    #bullets = pygame.sprite.Group()
    
    #Asteroid.containers = (asteroids, updatable, drawable)
    #Shot.containers = (shots, updatable, drawable)
    
    #AsteroidField.containers = updatable
    #asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        updatable.update(dt)

        for entity in drawable:
            entity.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60) / 1000  # seconds

    print ("  *** Welcome to Dragon Tactics! ***  ")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    print ("\n")
    print ("  Use the arrow keys to move your dragon around the screen.  ")
    print ("  *** Thank you for playing! ***  ")

if __name__ == "__main__":
    main()
